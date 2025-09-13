from django.urls import path
from . import views

#token view imports
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
	#USER MANAGEMENT API ENDPOINTS
	path('api/developer', views.Developer.as_view(), name='api-developer'),
	path('api/developer/get-followers', views.Get_Followers.as_view(), name='api-developer-get-followers'),
	path('api/register-developer', views.Register_Developer.as_view(), name='api-register-developer'),
]
