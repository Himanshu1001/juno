"""juno URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from mainApp import views
from rest_framework.documentation import include_docs_urls
import oauth2_provider.views as oauth2_views
from django.conf import settings
from mainApp.views import ApiEndpoint
from mainApp.views import UserViewSet, UserTasksViewSet, Custom_UserViewSet, ContentViewSet, ChallangesViewSet, UserChallangesViewSet


app_name = 'mainApp'

router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet)
router.register(r'task', views.UserTasksViewSet)
router.register(r'custom_user', views.Custom_UserViewSet)
router.register(r'content', views.ContentViewSet)
router.register(r'challanges', views.ChallangesViewSet)
router.register(r'user_challanges', views.UserChallangesViewSet)


oauth2_endpoint_views = [
    path('authorize/', oauth2_views.AuthorizationView.as_view(), name="authorize"),
    path('token/', oauth2_views.TokenView.as_view(), name="token"),
    path('revoke-token/', oauth2_views.RevokeTokenView.as_view(), name="revoke-token"),

]

if settings.DEBUG:
    # OAuth2 Application Management endpoints
    oauth2_endpoint_views += [
        path('applications/', oauth2_views.ApplicationList.as_view(), name="list"),
        path('applications/register/', oauth2_views.ApplicationRegistration.as_view(), name="register"),
        path('applications/<pk>/', oauth2_views.ApplicationDetail.as_view(), name="detail"),
        path('applications/<pk>/delete/', oauth2_views.ApplicationDelete.as_view(), name="delete"),
        path('applications/<pk>/update/', oauth2_views.ApplicationUpdate.as_view(), name="update"),
    ]

    # OAuth2 Token Management endpoints
    oauth2_endpoint_views += [
        path('authorized-tokens/', oauth2_views.AuthorizedTokensListView.as_view(), name="authorized-token-list"),
        path('authorized-tokens/<pk>/delete/', oauth2_views.AuthorizedTokenDeleteView.as_view(),
            name="authorized-token-delete"),
    ]


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^request_otp/', views.ValidatePhoneSendOtp.as_view(),name='validate_phone'),
	url(r'^validate_otp/', views.ValidateOTP.as_view(),name='validate_otp'),
	url(r'^', include(router.urls)),
    path("o/", include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('authorize/', oauth2_views.AuthorizationView.as_view(), name="authorize"),
    path('token/', oauth2_views.TokenView.as_view(), name="token"),
    path('revoke-token/', oauth2_views.RevokeTokenView.as_view(), name="revoke-token"),
    path('api/hello', ApiEndpoint.as_view()),  # an example resource endpoint
    path('index', views.index, name='index'),
     url(r'^docs/', include_docs_urls(title='My API title')),
	# path('', include('social_django.urls', namespace='social')),
  	# path('logout/', logout, {'next_page': settings.LOGOUT_REDIRECT_URL},
    # name='logout'),

]