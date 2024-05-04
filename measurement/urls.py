from django.urls import path
from measurement.views import SensorsView, MeasurementView, SensorPatchGetView

urlpatterns = [
    path('sensors/', SensorsView.as_view()),
    path('sensors/<pk>/', SensorPatchGetView.as_view()),
    path('measurements/', MeasurementView.as_view())

]
