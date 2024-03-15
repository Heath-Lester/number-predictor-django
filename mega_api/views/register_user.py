import json
from json import loads
from requests import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.http import HttpResponseBadRequest, HttpResponseNotAllowed, HttpResponseServerError
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.request import Request


@csrf_exempt
def register_user(request: Request) -> Response:
    '''Handles the creation of a new user for authentication

    Method arguments:
      request -- The full HTTP request object
    '''
    if request.method != 'POST':
        return HttpResponseNotAllowed(permitted_methods=['POST'])
    if request.body is None:
        return HttpResponseBadRequest({'message': 'request body must include user information'})

    # Load the JSON string of the request body into a dict
    body: json = json.loads(request.body.decode('utf-8'))

    # Create a new user by invoking the `create_user` helper method
    # on Django's built-in User model
    try:
        new_user: User = User.objects.create_user(
            username=body['username'],
            email=body['email'],
            password=body['password'],
            first_name=body['first_name'],
            last_name=body['last_name']
        )

        # Use the REST Framework's token generator on the new user account
        token: Token = Token.objects.create(user=new_user)

        # Return the token to the client
        data: str = json.dumps({"token": token.key, "id": new_user.id})
        return Response(data, content_type='application/json', status=status.HTTP_201_CREATED)

    except Exception as exception:
        return HttpResponseServerError(exception)
