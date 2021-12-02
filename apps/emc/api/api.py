import json

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import EmcSerializer

@api_view(['POST'])
def emc(request) -> Response:
    serializer = EmcSerializer(data = request.data, many = True)
    if serializer.is_valid():
        emc = calculoEmc(serializer.data)
        return Response(emc, status = status.HTTP_201_CREATED)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


def calculoEmc(data:dict) -> float:
    trueData = cargaJson()
    emc = 0
    for i in range(0, len(data)):
        emc += (trueData[i] - data[i]['predict'])**2
    return emc



def cargaJson() -> list:
    with open('true.json') as file:
        trueData = json.load(file)
        return trueData


[
    {"predict":374.9303382},
    {"predict":231.7836556}
]
