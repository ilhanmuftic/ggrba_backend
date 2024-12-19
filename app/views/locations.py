from rest_framework.generics import ListAPIView, RetrieveAPIView
from app.models import Location
from app.serializers.location import LocationSerializer


class LocationListView(ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class RandomLocationView(RetrieveAPIView):
    serializer_class = LocationSerializer

    def get_object(self):
        return Location.objects.order_by('?').first()    