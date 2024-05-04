from rest_framework.generics import ListAPIView, RetrieveAPIView
from measurement.models import Sensor, Measurement
from measurement.serializers import MeasurementSerializer, SensorDetailSerializer, SensorsSerializer
from rest_framework.response import Response
import json

# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView


class SensorsView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorsSerializer

    def post(self, request):
        data = json.loads(request.body)

        name, description = data.get('name'), data.get('description')
        Sensor(name=name, description=description).save()
        return Response({'status': 'OK'})


class SensorPatchGetView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def patch(self, request, pk):
        data = json.loads(request.body)
        new_description = data.get('description')
        new_name = data.get('name')
        if new_description:
            number = Sensor.objects.filter(id=pk).update(
                description=new_description)
        if new_name:
            number = Sensor.objects.filter(id=pk).update(name=new_name)
        return Response({'status': f'Обновлен {number} датчик с id {pk}'})


class MeasurementView(ListAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def post(self, request):
        data = json.loads(request.body)
        id_sensor = Sensor.objects.filter(id=data.get('sensor'))[0]
        temperature = data.get("temperature")
        Measurement(id_sensor=id_sensor, temperature=temperature).save()
        return Response({'status': 'OK'})
