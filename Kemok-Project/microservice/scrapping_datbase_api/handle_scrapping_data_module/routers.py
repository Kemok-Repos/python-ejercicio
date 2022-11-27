from rest_framework.routers import DefaultRouter

from handle_scrapping_data_module.views import ScrappingDataViewSet

router = DefaultRouter()

router.register(r'handle', ScrappingDataViewSet, basename='handle')

urlpatterns = router.urls
