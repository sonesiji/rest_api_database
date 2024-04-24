from django.shortcuts import render

# Create your views here.
from rest_framework import generics,permissions
from ApiApp.models import Language
from .serializers import LanguageSerializer
from django.db import IntegrityError
from django.contrib.auth.models import User
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate



class LanguageListCreateView(generics.ListCreateAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    
    # permission_classes = [permissions.IsAuthenticated]


class LanguageRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

    # def get_queryset(self):
    #     user = self.request.user
    #     # user can only update, delete own posts
    #     return Product.objects.filter(user=user)
    
# @csrf_exempt
# def signup(request):
#     if request.method == 'POST':
#         try:
#             data = JSONParser().parse(request)  # data is a dictionary
#             user = User.objects.create_user(username=data['username'], password=data['password'])
#             user.save()
#             token = Token.objects.create(user=user)
#             return JsonResponse({'token': str(token)}, status=201)
#         except IntegrityError:
#             return JsonResponse({'error': 'Username taken. Choose another username.'}, status=400)

# @csrf_exempt
# def login(request):
#     if request.method == 'POST':
#         data = JSONParser().parse(request)
#         user = authenticate(request, username=data['username'], password=data['password'])
        
#         if user is None:
#             return JsonResponse({'error': 'Unable to login. Check username and password.'}, status=400)
#         else:
#             # Return user token
#             try:
#                 token = Token.objects.get(user=user)
#             except Token.DoesNotExist:
#                 # If token not in DB, create a new one
#                 token = Token.objects.create(user=user)
            
#             return JsonResponse({'token': str(token)}, status=200)
    
