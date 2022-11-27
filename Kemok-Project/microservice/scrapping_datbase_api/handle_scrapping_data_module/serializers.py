from rest_framework import serializers

from handle_scrapping_data_module.models import ScrappingData


class ScrappingDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScrappingData
        fields = '__all__'
