from rest_framework import serializers
from leaderboard.models import User, Winner

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'age', 'address', 'points']

class WinnerSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Winner
        fields = ['user', 'points', 'timestamp']
