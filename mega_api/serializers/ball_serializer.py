from rest_framework.serializers import ModelSerializer
from mega_api.models.ball import Ball


class BallSerializer(ModelSerializer):
    """JSON serializer for Balls"""
    class Meta:
        """Ball Meta"""
        model: type = Ball
        fields: tuple[str] = (
            'id', 'number'
        )
