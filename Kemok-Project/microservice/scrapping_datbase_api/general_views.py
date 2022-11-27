from rest_framework import  viewsets


class GeneralViewSet(viewsets.ModelViewSet):
    serializer_class = None

    def get_queryset(self):
        model = self.get_serializer().Meta.model
        return model.objects.filter()
