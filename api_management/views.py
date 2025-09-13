from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated

# User management functionality imports
from user_management.views import *
import json


# API ENDPOINT FOR SIGNUP/REGISTER + LIST DEVELOPERS
class Register_Developer(APIView):
    print("OKAY")
    permission_classes = [AllowAny]

    def post(self, request):
        # Call the regular function
        response = developer(request)

        if isinstance(response, JsonResponse):
            return JsonResponse(json.loads(response.content), status=response.status_code)

        return JsonResponse({"error": "Unexpected response type"}, status=500)

class Developer(APIView):
    permission_classes = [IsAuthenticated]  # or [IsAuthenticated] if you want GET restricted

    def get(self, request):
        # Call the same developer() function for GET
        response = developer(request)

        if isinstance(response, JsonResponse):
            return JsonResponse(json.loads(response.content), status=response.status_code)

        return JsonResponse({"error": "Unexpected response type"}, status=500)

class Get_Followers(APIView):
    permission_classes = [IsAuthenticated]  # or [IsAuthenticated] if you want GET restricted

    def post(self, request):
        # Call the same developer() function for GET
        response = developer_follow_data(request)

        if isinstance(response, JsonResponse):
            return JsonResponse(json.loads(response.content), status=response.status_code)

        return JsonResponse({"error": "Unexpected response type"}, status=500)