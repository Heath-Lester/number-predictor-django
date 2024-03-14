from rest_framework.serializers import HyperlinkedModelSerializer, HyperlinkedIdentityField
from django.contrib.auth.models import User


class UserSerializer(HyperlinkedModelSerializer):
    """JSON serializer for Users"""
    class Meta:
        model: type = User
        url = HyperlinkedIdentityField(
            view_name='user',
            lookup_field='id'
        )
        fields: tuple[str] = ('id', 'url', 'username', 'password', 'first_name',
                              'last_name', 'email', 'is_active', 'date_joined')
