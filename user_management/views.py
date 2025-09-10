import re
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api_management.serializers import UserSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
import uuid

from .neo4j_utils import create_developer_node, get_developers


def developer(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)  # Parse JSON data correctly
            
            first_name = data.get('first_name')
            last_name = data.get('last_name')
            email = data.get('email')
            password = data.get('password')
            confirm_password = data.get('confirm_password')
            username = data.get('username')
            id = str(uuid.uuid4())  # string id for developer in neo4j

            # Check if email already exists
            if User.objects.filter(email=email).exists():
                return JsonResponse(
                    {"message": "Email already exists.", "status": "error"},
                    status=400
                )
            
            # Check if username already exists
            if User.objects.filter(username=username).exists():
                return JsonResponse(
                    {"message": "Username already exists.", "status": "error"},
                    status=400
                )

            # Validate password match
            if password != confirm_password:
                return JsonResponse(
                    {"message": "Passwords do not match.", "status": "error"},
                    status=400
                )

            # Create and save the new user
            new_user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                password=password  # `create_user` automatically hashes the password
            )

            # Create developer node in Neo4j
            create_developer_node(
                dev_id=id,
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username
            )

            return JsonResponse(
                {"message": "Developer registered successfully!", "status": "success"},
                status=201
            )

        except json.JSONDecodeError:
            return JsonResponse(
                {"message": "Invalid JSON format.", "status": "error"},
                status=400
            )

    elif request.method == 'GET':
        # Require the current user to be logged in
        if not request.user.is_authenticated:
            return JsonResponse(
                {"message": "Authentication required.", "status": "error"},
                status=401
            )

        # Fetch developers except the current user
        developers = get_developers(exclude_username=request.user.username)

        return JsonResponse(
            {"developers": developers, "status": "success"},
            status=200
        )

    return JsonResponse(
        {"message": "Invalid request method. Use POST or GET."},
        status=405
    )
