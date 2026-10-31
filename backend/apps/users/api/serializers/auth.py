from apps.users.models.user import CustomUser

from rest_framework import serializers


class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser

        fields = [
            "id",
            "username",
            "password",
            "email",
        ]

        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)


class RegisterResponseSerializer(serializers.Serializer):
    user = RegisterUserSerializer()
    access = serializers.CharField()
    refresh = serializers.CharField()
