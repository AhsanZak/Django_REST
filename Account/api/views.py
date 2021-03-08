from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from Account.api.serializers import RegistrationSerializers

@api_view(['POST'])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializers(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializers.save()
            data['response'] = "Successfully registered a new user"
            data['email'] = account.email
            data['username'] = account.username
        else:
            data = serializers.errors
        return Response(data)