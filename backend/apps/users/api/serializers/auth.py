from apps.users.models.user import User

from rest_framework import serializers


class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

        fields = [
            "id",
            "username",
            "password",
            "email",
        ]

        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class RegisterResponseSerializer(serializers.Serializer):
    user = RegisterUserSerializer()
    access = serializers.CharField()
    refresh = serializers.CharField()
