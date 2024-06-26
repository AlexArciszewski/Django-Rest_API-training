from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """To się wyświetli w API w http://127.0.0.1:8000/users/ wjsonie"""


    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

