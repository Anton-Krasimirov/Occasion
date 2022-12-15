from django.http import HttpResponse

from Occasion import urls
from Occasion.accounts.helpers import InternalErrorView


def handle_exception(get_response):
    def middleware(request):
        response = get_response(request)
        if response.status_code >= 400:
            return InternalErrorView.as_view()(request)
        return response
    return middleware
