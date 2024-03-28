from rest_framework import status
import datetime

from backend.helpers.error_response import error_response
from .models import User

# Checks for authorization by https method 
# if the token is not set, return error message
# if the token is expired, return error message
# if the token is valid, return the user


class CustomLoginRequiredMixin():

    def dispatch(self, request, *args, **kwargs):
        if 'Authorization' not in request.headers:
            return error_response('Please set Auth-Token.', status.HTTP_401_UNAUTHORIZED)

        token = request.headers['Authorization']
        now = datetime.datetime.now()
        login_user = User.objects.filter(token=token, token_expires__gt=now)
        if len(login_user) == 0:
            return error_response('The token is invalid or expired.', status.HTTP_401_UNAUTHORIZED)

        request.login_user = login_user[0]
        return super().dispatch(request, *args, **kwargs)