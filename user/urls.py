from django.urls import path, include
from user import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("signup/", views.UserView.as_view(), name="user_view"),
    path("api/token/", views.CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),


    path('kakao/login/', views.kakao_login, name='kakao'),
    path('kakao/callback/', views.kakao_callback, name='kakao'),
    path('kakao/login/finish/', views.KakaoLogin.as_view(), name='kakao'),

    
    path("follow/<int:user_id>/", views.FollowView.as_view(), name="follow_view"),
    path("profile/", views.MyProfileView.as_view(), name="my_profile_view"),
    path("profile/<int:user_id>/", views.ProfileView.as_view(), name="profile_view"),
    path("pet/", views.PetListView.as_view(), name="pet_view"),
    path("pet/<int:pet_id>/", views.PetView.as_view(), name="pet_view"),
    path("mypet/", views.MyPetView.as_view(), name="my_pet_view"),

    path("google/login/", views.google_login, name="google_login"),
    path("google/callback/", views.google_callback, name="google_callback"),
    path("google/login/finish/", views.GoogleLogin.as_view(), name="google_login_todjango"),

    path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
    # path('send_email/', views.send_email, name='send_email'),
]