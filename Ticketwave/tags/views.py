from .models import Tags
from .serializers import tags_Serializer
from .pagination import StandardResultsSetPagination
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly, IsAuthenticated


class tag_List(ListAPIView):

    queryset = Tags.objects.all()

    serializer_class = tags_Serializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

class tag_Retrieve(RetrieveAPIView):
    queryset = Tags.objects.all()
    serializer_class = tags_Serializer
    permission_classes = [IsAuthenticated]


class tag_Update(UpdateAPIView):
    queryset = Tags.objects.all()
    lookup_field = 'pk'
    serializer_class = tags_Serializer
    permission_classes = [IsAuthenticated]

    def put(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)


class tag_Destroy(DestroyAPIView):
    queryset = Tags.objects.all()
    serializer_class = tags_Serializer
    permission_classes = [IsAuthenticated]


class tag_Create(CreateAPIView):
    queryset = Tags.objects.all()
    serializer_class = tags_Serializer
    permission_classes = [IsAuthenticated]
