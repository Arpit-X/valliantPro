from .models import UserProfile, User, Events, Participations
from rest_framework import serializers
from django.contrib.auth.validators import UnicodeUsernameValidator

class UserSerialiser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username",'email','password']
        extra_kwargs = {
            'username': {
                'validators': [UnicodeUsernameValidator()],
            }
        }


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerialiser()
    class Meta:
        model = UserProfile
        fields = '__all__'
    def create(self, validated_data):
        user_data = validated_data.pop("user")
        user = User.objects.create_user(**user_data)
        profile = UserProfile.objects.create(user=user, **validated_data)
        return profile

    def update(self, instance, validated_data):
        print("called")
        user_data = validated_data.pop("user")
        instance.phone = validated_data.get("phone",instance.phone)
        instance.college = validated_data.get("college",instance.college)
        instance.joinedOn = validated_data.get("joinedOn",instance.joinedOn)
        instance.isCoordinator = validated_data.get("isCoordinator",instance.isCoordinator)
        instance.isFaculty = validated_data.get("isFaculty",instance.isFaculty)
        instance.save()
        #print(user_data)
        user = User.objects.get(username=user_data["username"])
        user.username = user_data.get("username",user.username)
        user.password = user_data.get("password",user.password)
        user.email = user_data.get("email",user.email)
        user.save()
        return instance

class EventSerialiser(serializers.ModelSerializer):
    facultyCoordinator = ProfileSerializer()
    studentCoordinator = ProfileSerializer()
    class Meta:
        model = Events
        fields = '__all__'

class ParticipationSerialiser(serializers.ModelSerializer):
    participant = ProfileSerializer()
    event  = EventSerialiser()
    class Meta:
        model = Participations
        fields = "__all__"


