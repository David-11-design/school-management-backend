from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from ..core import models

class AuthView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response({
                "error": "Username and password are required"},
                status= status.HTTP_400_BAD_REQUEST
            )

        admin = models.Admin.objects.filter(username=username, password=password).first()
        
        if admin:
            return Response({
                "message": "Login successful",
                "user_type": "admin",
                "user_id": admin.id
            }, status=status.HTTP_200_OK)
        
        teacher = models.Teacher.objects.filter(username=username, password=password).first()

        if teacher:
            return Response({
                "message": "Login successful",
                "user_type": "teacher",
                "user_id": teacher.id
            }, status=status.HTTP_200_OK)
        
        return Response({
            "error": "Invalid username or password"},
            status=status.HTTP_401_UNAUTHORIZED)
    