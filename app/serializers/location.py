from rest_framework import serializers
from app.models import Location
from app.constants.validation import MAX_LAT, MAX_LNG, MIN_LAT, MIN_LNG

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class CreateLocationSerializer(serializers.ModelSerializer):
    city = serializers.CharField(max_length=255, required=False)

    class Meta:
        model = Location
        fields = ['name', 'lat', 'lng', 'city']  # Specify only the fields you want to send

    def validate_lat(self, value):
        """Ensure latitude is within the valid range for Bosnia and Herzegovina."""
        if not (MIN_LAT <= value <= MAX_LAT):
            raise serializers.ValidationError(
                f"Latitude must be between {MIN_LAT} and {MAX_LAT} for Bosnia and Herzegovina."
            )
        return value

    def validate_lng(self, value):
        """Ensure longitude is within the valid range for Bosnia and Herzegovina."""
        if not (MIN_LNG <= value <= MAX_LNG):
            raise serializers.ValidationError(
                f"Longitude must be between {MIN_LNG} and {MAX_LNG} for Bosnia and Herzegovina."
            )
        return value        