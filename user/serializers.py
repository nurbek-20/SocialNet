from rest_framework import serializers
from .models import MyUser


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('username', 'phone_number', 'password')

    def create(self, validated_data):
        user = MyUser(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            if field == 'password':
                instance.set_password(value)
            else:
                setattr(instance, field, value)
        instance.save()
        return instance


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = '__all__'


class ProfileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('id', 'username', 'phone_number', 'profile_picture', 'bio')


class ProfileUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyUser
        fields = ('username', 'phone_number', 'profile_picture', 'bio')



