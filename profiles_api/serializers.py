from rest_framework import serializers

# like django forms, define a serializer and specify the field you want to accept in your input
# validates the input of a api view
class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)


