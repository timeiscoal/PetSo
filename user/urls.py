from django.urls import path, include
from user import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


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
    path("pet/<int:pet_id>/", views.PetView.as_view(), name="pet_view"),

    path("google/login/", views.google_login, name="google_login"),
    path("google/callback/", views.google_callback, name="google_callback"),
    path("google/login/finish/", views.GoogleLogin.as_view(), name="google_login_todjango"),
    

]