from django.http import HttpResponseForbidden
from home.models import Store

ALLOWED_IPS = ["127.0.0.1"]


class IPBlockingMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            ip = x_forwarded_for.split(",")[0]
        else:
            ip = request.META.get("REMOTE_ADDR")
        return ip

    def __call__(self, request):
        ip = self.get_client_ip(request)
        print("Client IP:", ip)
        if ip not in ALLOWED_IPS:
            return HttpResponseForbidden("Forbidden IP address.")
        return self.get_response(request)


class CheckBMPHeaderMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print(request.headers)

        headers = dict(request.headers)

        if "bmp_id" not in headers:
            return HttpResponseForbidden("Missing bmp_id header.")
        else:
            bmp_id = headers.get("bmp_id")
            if not Store.objects.filter(bmp_id=bmp_id).exists():
                return HttpResponseForbidden("Invalid bmp_id.")

        return self.get_response(request)
