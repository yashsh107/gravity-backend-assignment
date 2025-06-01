from rest_framework.response import Response
from rest_framework import generics 
from user.models import *
from helper import functions
from rest_framework.permissions import IsAuthenticated
from user.serializers import * 
from helper.functions import *
from helper import messages
from rest_framework.views import APIView




class RegisterUser(generics.CreateAPIView):
    """
    API to register user
    """
    serializer_class = RegisterUserSerializer
   
    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid(raise_exception=False):
            errors = serializer.errors
            err = error_message_function(errors)
            return Response(ResponseHandling.failure_response_message(err, ""), status=status400)
        serializer.save()
        return Response(ResponseHandling.success_response_message(messages.OPERATION_SUCCESS, ""), status=status200)
    
