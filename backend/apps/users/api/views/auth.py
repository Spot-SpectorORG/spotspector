from apps.users.api.serializers.auth import (
    RegisterUserSerializer,
    RegisterResponseSerializer,
)

from drf_spectacular.utils import extend_schema

from rest_framework.permissions import AllowAny

from rest_framework.response import Response

from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework import generics, status


class RegisterView(generics.CreateAPIView):
    """Takes a set of user credentials and create a new user"""

    permission_classes = [AllowAny]
    serializer_class = RegisterUserSerializer

    @extend_schema(responses={201: RegisterResponseSerializer})
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        refresh = RefreshToken.for_user(user)

        return Response(
            {
                "user": serializer.data,
                "access": str(refresh.access_token),
                "refresh": str(refresh),
            },
            status=status.HTTP_201_CREATED,
        )
