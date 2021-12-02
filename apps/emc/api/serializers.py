from rest_framework import serializers

class EmcSerializer(serializers.Serializer):
    predict = serializers.FloatField()
