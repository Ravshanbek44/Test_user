from rest_framework import generics
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .models import Account
from .serializers import RegisterSerializer, LoginSerializer


class RegisterAPIView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        phone = self.request.data['phone']
        if Account.objects.filter(phone=phone).first():
            return Response({'success': False, "message": "User already registered"})
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": True, "message": "User created"})
        return Response(serializer.errors)


class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        phone = self.request.data['phone']
        password = self.request.data['password']
        print(password)
        user = Account.objects.filter(phone=phone, password=password).first()
        if not user:
            return Response({'success': False, "message": "Phone or password incorrect"})
        token, created = Token.objects.get_or_create(user=user)
        data = {
            'success': True,
            'message': 'User logged',
            'token': str(token),
        }
        return Response(data)
