from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from rest_framework import serializers

User = get_user_model()


# Serializer는 용도별로 나뉜다. 모델에 따라 결정되는 것이 아니라 한 serializer당 한 종류의 json 형태를 주로 해야한다.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class SignupSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            'username',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'email',
            'token'
        )

    def validate_username(self, username):
        # 이미 존재하는 유저네임일 경우
        if User.objects.filter(username=username).exists():
            raise ValidationError('Username already exists. Try a different username.')
        return username

    def validate(self, data):
        password1 = data.get('password1')
        password2 = data.get('password2')
        if password1 != password2:
            raise ValidationError('Passwords are not matching. Check your passwords.')
        return data

    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password1'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
        )

    def to_representation(self, instance):
        """
        최종 결과 - search "how to add element at end of serializer"
        :param instance:
        :return:
        """
        ret = super().to_representation()
        data = {
            'user': ret,
            'token': instance.token
        }
        return data
