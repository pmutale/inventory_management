
from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.utils.translation import ugettext as _

from access_control.models import Employee
from access_control.validators import ValidatePasswordStrength


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True,
                                     'validators': [ValidatePasswordStrength('password')]}}

    def create(self, validated_data):
        context = {'username': None, 'success': False, 'error': False}
        try:
            user = User(
                    email=validated_data['email'],
                    username=validated_data['username'],
                    first_name=validated_data['last_name'],
                    last_name=validated_data['last_name']
                )
            user.set_password(validated_data['password'])
            user.save()
            Employee.objects.create(user=user)
            Token.objects.create(user=user)
            setattr(JsonResponse, 'username', _(F'User with username, {user.username} has been successfully created.'))
            return JsonResponse
        except Exception as e:
            context['error'] = str(e)
            return JsonResponse(context, json_dumps_params={'indent': 4})


