from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import User, Pet


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        user = User(
            email=validated_data["email"],
        )
        user.set_password(validated_data["password"])
        user.is_active = True
        user.save()
        return user

    def update(self, validated_data):
        user = User(
            email=validated_data["email"],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["email"] = user.email
        return token


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email", "introduce", "profile_img")


class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("introduce", "profile_img")

class PetSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    class Meta:
        model = Pet
        fields = ("pet_name", "pet_age", "pet_sex", "pet_species", "pet_desc", "pet_image")
