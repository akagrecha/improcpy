from rest_framework import serializers


class ImageSerializer(serializers.ModelSerializer):

    image_url = serializers.ImageField(max_length=None, allow_empty_file=False)

