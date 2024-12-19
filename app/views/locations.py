from rest_framework.generics import ListAPIView
from rest_framework.pagination import CursorPagination
from app.models import Location
from app.serializers.location import LocationSerializer


class LocationListView(ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer