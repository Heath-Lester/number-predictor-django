
import json
from json import loads
from requests import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from django.contrib.auth.models import AbstractBaseUser


@csrf_exempt
def login_user(request) -> Response:
    '''Handles the authentication of a user

    Method arguments:
      request -- The full HTTP request object
    '''
    if request.method != 'POST':
        return HttpResponseNotAllowed(permitted_methods=['POST'], status=status.HTTP_405_METHOD_NOT_ALLOWED)
    if request.body is None:
        return HttpResponseBadRequest({'message': 'request body must include user information'}, status=status.HTTP_400_BAD_REQUEST)

    body: json = loads(request.body.decode('utf-8'))

    # Use the built-in authenticate method to verify
    name: str = body['username']
    pass_word: str = body['password']
    authenticated_user: AbstractBaseUser = authenticate(
        username=name, password=pass_word)

    # If authentication was successful, respond with their token
    if authenticated_user is not None:
        try:

            token: Token = Token.objects.get(user=authenticated_user)
            data: str = json.dumps(
                {"valid": True, "token": token.key, "id": authenticated_user.id})
            return HttpResponse(data, content_type='application/json', status=status.HTTP_200_OK)

        except Token.DoesNotExist as exception:
            return HttpResponseNotFound({'message': exception.args[0]}, status=status.HTTP_404_NOT_FOUND)
    else:
        # Bad login details were provided. So we can't log the user in.
        data: str = json.dumps({"valid": False})
        return HttpResponse(data, content_type='application/json', status=status.HTTP_401_UNAUTHORIZED)
