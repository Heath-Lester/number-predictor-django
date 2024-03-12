from rest_framework.serializers import ModelSerializer
from mega_api.models.mega_ball import MegaBall


class MegaBallSerializer(ModelSerializer):
    """JSON serializer for Mega Balls"""
    class Meta:
        """Mega Ball Meta"""
        model: type = MegaBall
        fields: tuple[str] = (
            'id', 'number'
        )
