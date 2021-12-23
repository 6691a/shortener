import json
from urllib.parse import unquote

from log.models import BackOfficeLog

class BackOfficeLogMiddleware():
    
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        """
        request
        """
        response = self.get_response(request)

        """
        response
        """
        if request.method not in ["GET", "OPTIONS"]:

            try:
                body = json.loads(request.body) if request.body else None
            except json.decoder.JSONDecodeError:
                body = self.form_data_to_dict(request.body)
            end_point = request.get_full_path_info()
            ip = (
                request.headers["X-Forwarded-For"].split(",")[0]
                if "x-forwarded-for" in request.headers.keys()
                else request.META.get("REMOTE_ADDR", None)
            )
                # X-Forwarded-For: <supplied-value>,<client-ip>,<load-balancer-ip>
            ip = ip.split(",")[0] if "," in ip else ip
            
            BackOfficeLog.objects.create(
                end_point=end_point,
                body=body,
                ip=ip,
                user_id=1,
                status_code=response.status_code,
                method=request.method,
            )
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        request_data = getattr(request, '_body', request.body)
        request_data = json.loads(request_data)

        
    @staticmethod
    def form_data_to_dict(body: bytes):
        UNLOGGABLES = ["csrfmiddlewaretoken", "password"]
        body = body.decode("utf-8")
        body = unquote(body).split("&")
        rtn = {}
        for b in body:
            body_list = b.split("=")
            if body_list[0] not in UNLOGGABLES:
                rtn[body_list[0]] = body_list[1]
            else: 
                rtn[body_list[0]] = "hidden"
        return rtn