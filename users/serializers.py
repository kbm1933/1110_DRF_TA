from rest_framework import serializers
from users.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self,validated_data):
        user = super().create(validated_data)
        password = user.password
        user.set_password(password)
        user.save()
        return user

    # def update(self,validated_data):
    #     user = super().create(validated_data)
    #     password = user.password
    #     user.set_password(password)
    #     user.save()
    #     return user

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):   # email로 로그인하는 jwt 커스터마이징 하기위한 serializer
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['name'] = user.email
        token['token_message'] = 'sparta_time_attack'
        return token