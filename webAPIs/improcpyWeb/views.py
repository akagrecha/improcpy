from django.http import HttpResponse
from serializers import ImageSerializer
from improcpy.enhancement.toonify import toonify
from rest_framework.decorators import api_view
import urllib


@api_view(['POST'])
def toonified_image(request):

    if request == 'POST':
        image = urllib.urlretrieve(ImageSerializer.image_url)
        result = toonify(image)

        return HttpResponse(result, content_type=image)





