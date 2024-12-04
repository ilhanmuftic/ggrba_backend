from django.http import HttpResponse
from django.views import View


class OkView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse(status=200)
