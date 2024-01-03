from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from dj_rest_auth.serializers import TokenSerializer
from rest_framework.authtoken.serializers import AuthTokenSerializer

class RegisterSerializer(serializers.ModelSerializer):
   username = serializers.CharField(
      write_only=True, 
      required=True,
      style={"input_type" : "username"}
      )
   email = serializers.EmailField(required=True, 
                                  validators=[UniqueValidator(queryset=User.objects.all())])
   password = serializers.CharField(
      write_only=True,
      style={"input_type" : "password"}
      )
   password2 = serializers.CharField(
      write_only=True, 
      required=True,
      style={"input_type" : "password"}
      )

   class Meta:
      model = User
      fields = (
         'id',
         'username',
         'first_name',
         'last_name',
         'email',
         'password',
         'password2',
      )

   def get_token(self, obj):
      token = Token.objects.get(User=obj)
      return token.key

   def validate(self, data):
       if data['password'] != data['password2']:
          raise serializers.ValidationError({
             "message" : "Password fields did not match."
          })
       
       return data
   
   def create(self, validated_data):
      # password2 was deleted
      validated_data.pop('password2')
      # password was deleted temporary
      password = validated_data.pop('password')
      # user with first name, last name and email info was created 
      user = User.objects.create(**validated_data)
      # password was added to inf of user
      user.set_password(password)

      user.save()
      return user
   
class UserTokenSerializer(serializers.ModelSerializer):
      class Meta:
          model = User
          fields = (
              'id',
              'first_name',
              'last_name',
              'email',
      )

class CustomTokenSerializer(TokenSerializer):
    user = UserTokenSerializer

    class Meta:
        model = Token
        fields = ('key', 'user')