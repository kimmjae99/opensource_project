from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
import requests
import io
import base64

# Create your views here.
from django.shortcuts import render


@api_view(["POST"])
def get_tags(request):
    image = request.data["image"]
    image = bytes(image, 'utf-8')
    image = image[image.find(b'/9'):]
    image = base64.b64decode(image)

    url = "https://dapi.kakao.com/v2/vision/multitag/generate"

    headers = {
        'Authorization': 'KakaoAK 8577b6ff738de95cbb9732af84eedbdf'
    }

    data = io.BytesIO(image)
    response = requests.post(url, headers=headers, files={"image": data})

    return Response(response.json()["result"]["label_kr"])
