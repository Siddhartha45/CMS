import importlib
from django.shortcuts import render
from rest_framework import views
from rest_framework.response import Response
from rest_framework import status
from mail.tasks import nuke


# Create your views here.
class MailViewSet(views.APIView):
    
    def post(self, request, format=None):
        nuke.delay()
        return Response(data={"detail": "Mail Sent"}, status=status.HTTP_200_OK)
