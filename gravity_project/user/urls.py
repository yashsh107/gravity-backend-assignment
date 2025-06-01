from django.urls import path
from user.apis import *


from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView



urlpatterns = [

    path('api/register/', RegisterUser.as_view()), 
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), 
    
      
]