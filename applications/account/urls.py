from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from applications.account.views import RegisterApiView, ChangePasswordApiView, ActivationApiView, ForgotPasswordAPIView, \
    ForgotPasswordCompleteAPIView, LoginApiView

urlpatterns = [
    path('register/', RegisterApiView.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', LoginApiView.as_view()),
    path('change_password/', ChangePasswordApiView.as_view()),
    path('activate/<uuid:activation_code>/', ActivationApiView.as_view()),
    path('forgot_password/', ForgotPasswordAPIView.as_view()),
    path('forgot_password_complete/', ForgotPasswordCompleteAPIView.as_view())

]
