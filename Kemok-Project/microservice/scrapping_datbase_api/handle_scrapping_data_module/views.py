from general_views import GeneralViewSet
from handle_scrapping_data_module.serializers import ScrappingDataSerializer


class ScrappingDataViewSet(GeneralViewSet):
    serializer_class = ScrappingDataSerializer
