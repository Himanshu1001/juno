from django.shortcuts import render
from rest_framework import viewsets, permissions, status, generics, views
from .serializers import *
import random
import requests
from .models import *
from rest_framework.response import Response
from oauth2_provider.views.generic import ProtectedResourceView
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from rest_framework import filters
from django_filters import rest_framework as djfilters

# Create your views here.
class ValidatePhoneSendOtp(views.APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        phone_number = request.data.get('phone_number')
        country_code = request.data.get('country_code')

        if phone_number:
            phone_number = str(phone_number)
            country_code = str(country_code)
            user = User.objects.filter(username=phone_number)
            
            print(phone_number)
            key = send_otp(phone_number, country_code)
            if key:
                old = PhoneOTP.objects.filter(
                    phone_number__iexact=phone_number)
                if old.exists():
                    old = old.first()
                    count = old.count
                    if count > 10:
                        return Response({
                            'status': False,
                            'detail': 'Sending OTP Error. Limit Exceeded.Please contact Customer Support'
                        })

                    old.count = count + 1
                    old.otp = key
                    old.save()
                    return Response({
                        'status': True,
                        'detail': 'OTP send successfully!!'
                    })

                else:
                    PhoneOTP.objects.create(
                        phone_number=phone_number,
                        otp=key,
                    )
                    return Response({
                        'status': True,
                        'detail': 'OTP send successfully!!'
                    })
            else:
                return Response({
                    'status': False,
                    'detail': 'Sending OTP error'
                })

        else:
            return Response({
                'status': False,
                'detail': 'Phone Number is not given!'
            })


def send_otp(phone_number, country_code):
    if phone_number:
        key = random.randint(999, 9999)
        api_key = "a86a24ff-eb05-11e8-a895-0200cd936042"
        template_name = "GIGZO"
        link = f"https://2factor.in/API/V1/{api_key}/SMS/{country_code+phone_number}/{key}/{template_name}"
        payload = ""
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = requests.request(
            "GET", link, data=payload, headers=headers)
        print(key)
        # print(response.text)
        return key
    else:
        return False

class ValidateOTP(views.APIView):
    """
    If user have received the OTP, he/she will post a request with phone and that OTP and then the user 
    will be direct to set the password.
    """
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        phone_number = request.data.get('phone_number')
        country_code = request.data.get('country_code')
        otp_sent = request.data.get('otp')
        phone_number = str(phone_number)
       
        if phone_number and otp_sent:
            old = PhoneOTP.objects.filter(
                phone_number__iexact=phone_number).order_by('created_at')
            if old.exists():
                old = old[0]
                if str(otp_sent) == str(old.otp):
                    old.is_verified = True
                    old.save()
                    user = User.objects.filter(username=phone_number)
                    print (user)
                    print (phone_number)
                    if user.exists(): 
                        return Response({ 'status': 1, 
                                        'detail': 'User exists. Login' 
                                        })
                    else:
                        return Response({
                            'status': 2,
                            'detail': "OTP Matched. User doesn't exist. Please proceed for Registration",
                        })
                else:
                    return Response({
                        'status': False,
                        'detail': 'OTP Incorrect'
                    })
            else:
                return Response({
                    'status': False,
                    'detail': 'First verify your Phone number'
                })

        else:
            return Response({
                'status': False,
                'detail': 'Please provide both Phone number and OTP'
            })

class ApiEndpoint(ProtectedResourceView):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, OAuth2!')

class CommenViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    filter_backends = (filters.OrderingFilter,
                       filters.SearchFilter, djfilters.DjangoFilterBackend,)
    filterset_fields = '__all__'
    search_fields = '__all__'
    ordering_fields = '__all__'
    extra_permissions = None

class UserViewSet(CommenViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class Custom_UserViewSet(CommenViewSet):
    queryset = Custom_User.objects.filter()
    serializer_class = Custom_UserSerializer


class UserTasksViewSet(CommenViewSet):
    queryset = UserTasks.objects.all()
    serializer_class = UserTasksSerializer
    
class ContentViewSet(CommenViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer

class ChallangesViewSet(CommenViewSet):
    queryset = Challanges.objects.all()
    serializer_class = ChallangesSerializer

class UserChallangesViewSet(CommenViewSet):
    queryset = UserChallanges.objects.all()
    serializer_class = UserChallangesSerializer

@login_required()
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.", status=200)