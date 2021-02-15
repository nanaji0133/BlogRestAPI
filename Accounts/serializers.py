from django.contrib.auth import get_user_model, authenticate

from rest_framework import serializers, validators
from rest_framework.serializers import SerializerMethodField


User = get_user_model()

User._meta.get_field('email')._unique = True

class RegisterSerializer(serializers.ModelSerializer):
    email2 = serializers.EmailField(label='confirm mail')
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'email2']
        
        extra_kwargs = {"password": {"write_only":True}}

    def validate_email2(self, value):
        data = self.get_initial()
        email = data.get("email")
        if email != value:
            raise validators.ValidationError("both the emails are not same")
        return value

    def create(self, validated_data):
        user_obj = User.objects.create_user(username=validated_data['username'], email=validated_data['email'],
                                    password=validated_data['password'])
        # password = password=validated_data['password']
        # user_obj.set_password('password')
        # user_obj.save()
        return validated_data


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=False)
    username = serializers.CharField(required=False)
    password = serializers.CharField()

    class Meta:
        model = User
        fields = ["email", "password", "username"]

    def validate(self, data):
        username = data.get("username", None)
        email = data.get("email", None)
        password = data.get("password",  None)

        if (username or email) and password:
            if username:
                user = authenticate(username=username, password=password)
            if email:
                user = authenticate(email=email, password=password)
            if user:
                data["user"] = user
            else:
                raise validators.ValidationError("email/username and password are not matching")
        else:
            raise validators.ValidationError("please enter credentials")
        return data

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "username"]

        
