from django.http import request
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .serializers import CustomerSerializer, HotelAdminSerializer, DeliveryPersonSerializer
from .models import Customer, HotelAdmin, DeliveryPerson, User
from django.http import JsonResponse
from django.contrib.auth import authenticate, get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, logout

import re
import random
# Create your views here.


def generate_session_tokens(length=10):
    token_chars_list = [chr(i) for i in range(97, 123)] \
        + [str(i) for i in range(10)] \
        + [chr(i) for i in range(65, 91)]
    return ''.join(random.SystemRandom().choice(token_chars_list) for _ in range(length))

@csrf_exempt # This decorator marks a view as being free from the protection ensured by the middleware.
def customer_signin(request):
    if not request.method == 'POST':
        return JsonResponse({'error': 'Send a post request with valid parameters'})

    username = request.POST['email']
    password = request.POST['password']

    # Validation Part
    if not re.match(r'\b[\w\.-]+@[\w\.-]+\.\w{2,4}\b', username):
        return JsonResponse({'error': 'Enter a valid email'})

    if len(password) < 3:
        return JsonResponse({'error': 'Password errors must be atleast 3 chars long'})

    UserModel = User # This method will return the currently active User model – the custom User model if one is specified, or User otherwise.

    # get() returns the object of the model
    # all() returns the QuerySet containing objects of the model
    # filter() returns the QuerySet containing objects of the model with some filers applied to it
    # values() is the method of QuerySet that returns QuerySet of dictionaries rather than model instances
    # first() returns the first object matched by the queryset
    # objects is the instance of the Manager of the model which contains helper methods like get(), filter()
    try:
        user = UserModel.objects.get(email=username) # Get the user object from current email

        if user.check_password(password): # Check is password entered by user is matching with 'user' or not
            user_dict = UserModel.objects.filter(email=username).values().first()
            # values() Returns queryset of the dict of users with the username containing all info, in which we are selecting the first dict
            user_dict.pop('password') # Don't need to travel further at frontend

            if user.session_token != '0':
                user.session_token = '0' # If previous session exists, make sure to delete session
                user.save()
                return JsonResponse({'error': 'Previous session exists'})

            token = generate_session_tokens()
            user.session_token = token
            user.save()
            user_dict['session_token'] = token

            user = authenticate(username=username, password=password)
            login(request, user) # Heavylifting by Django
            return JsonResponse({'token': token, 'user': user_dict})
        else:
            return JsonResponse({'error': 'Invalid password'})

    except UserModel.DoesNotExist():
        return JsonResponse({'error': 'Invalid email'})


def customer_signout(request, id): # It takes ID of user as well
    logout(request)

    UserModel = User

    try:
        user = UserModel.objects.get(pk=id) # Get the user object with the current ID
        user.session_token = '0'
        user.save()
    except UserModel.DoesNotExist:
        return JsonResponse({'error': 'Invalid user ID'})

    return JsonResponse({'success': 'Logout success'})

@csrf_exempt
def hotel_signin(request):
    if not request.method == 'POST':
        return JsonResponse({'error': 'Send a post request with valid parameters'})

    username = request.POST['email']
    password = request.POST['password']

    # Validation Part
    if not re.match(r'\b[\w\.-]+@[\w\.-]+\.\w{2,4}\b', username):
        return JsonResponse({'error': 'Enter a valid email'})

    if len(password) < 3:
        return JsonResponse({'error': 'Password errors must be atleast 3 chars long'})

    UserModel = User

    try:
        user = UserModel.objects.get(email=username)

        if user.check_password(password):
            user_dict = UserModel.objects.filter(email=username).values().first()

            user_dict.pop('password')

            if user.session_token != '0':
                user.session_token = '0'
                user.save()
                return JsonResponse({'error': 'Previous session exists'})

            token = generate_session_tokens()
            user.session_token = token
            user.save()
            user_dict['session_token'] = token
            
            user = authenticate(username=username, password=password)
            login(request, user)
            return JsonResponse({'token': token, 'user': user_dict})
        else:
            return JsonResponse({'error': 'Invalid password'})

    except UserModel.DoesNotExist():
        return JsonResponse({'error': 'Invalid email'})


def hotel_signout(request, id):
    logout(request)

    UserModel = User

    try:
        user = UserModel.objects.get(pk=id)
        user.session_token = '0'
        user.save()
    except UserModel.DoesNotExist:
        return JsonResponse({'error': 'Invalid user ID'})

    return JsonResponse({'success': 'Logout success'})


@csrf_exempt
def delivery_signin(request):
    if not request.method == 'POST':
        return JsonResponse({'error': 'Send a post request with valid parameters'})

    username = request.POST['email']
    password = request.POST['password']

    # Validation Part
    if not re.match(r'\b[\w\.-]+@[\w\.-]+\.\w{2,4}\b', username):
        return JsonResponse({'error': 'Enter a valid email'})

    if len(password) < 3:
        return JsonResponse({'error': 'Password errors must be atleast 3 chars long'})

    UserModel = User

    try:
        user = UserModel.objects.get(email=username)

        if user.check_password(password):
            user_dict = UserModel.objects.filter(email=username).values().first()

            user_dict.pop('password')

            if user.session_token != '0':
                user.session_token = '0'
                user.save()
                return JsonResponse({'error': 'Previous session exists'})

            token = generate_session_tokens()
            user.session_token = token
            user.save()
            user_dict['session_token'] = token
            
            user = authenticate(username=username, password=password)
            login(request, user)
            return JsonResponse({'token': token, 'user': user_dict})
        else:
            return JsonResponse({'error': 'Invalid password'})

    except UserModel.DoesNotExist():
        return JsonResponse({'error': 'Invalid email'})


def delivery_signout(request, id):
    logout(request)

    UserModel = User

    try:
        user = UserModel.objects.get(pk=id)
        user.session_token = '0'
        user.save()
    except UserModel.DoesNotExist:
        return JsonResponse({'error': 'Invalid user ID'})

    return JsonResponse({'success': 'Logout success'})


class CustomerViewSet(viewsets.ModelViewSet):
    permission_classes_by_action = {'create': [AllowAny]}

    queryset = Customer.objects.all().order_by('user_id')
    serializer_class = CustomerSerializer

    # Because of this method, Permissions will be restricted like, user cannot explictly make is_superuser true and if it is made then also, the changes are not gonna made in the database
    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]

class HotelAdminViewSet(viewsets.ModelViewSet):
    permission_classes_by_action = {'create': [AllowAny]}

    queryset = HotelAdmin.objects.all().order_by('user_id')
    serializer_class = HotelAdminSerializer

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]

class DeliveryPersonViewSet(viewsets.ModelViewSet):
    permission_classes_by_action = {'create': [AllowAny]}

    queryset = DeliveryPerson.objects.all().order_by('user_id')
    serializer_class = DeliveryPersonSerializer

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]
