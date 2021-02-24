from django.urls import path
from .views.screenshot_views import Screenshots, ScreenshotDetail
from .views.user_views import SignUp, SignIn, SignOut, ChangePassword

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  	# Restful routing
    path('screenshots/', Screenshots.as_view(), name='screenshots'),
    path('screenshots/<int:pk>/', ScreenshotDetail.as_view(), name='screenshot_detail'),
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-pw/', ChangePassword.as_view(), name='change-pw'),
]
