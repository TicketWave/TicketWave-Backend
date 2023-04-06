from .models import Order
from .serializers import order_Serializer
from .filters import orderfilter
from .pagination import StandardResultsSetPagination
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, RetrieveAPIView, UpdateAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from authentication.permissions import Is_orderowner
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly, IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class order_List(ListAPIView):

    queryset = Order.objects.all()

    serializer_class = order_Serializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = orderfilter

    ordering_fields = ['cost', 'created', 'first_name', 'last_name', 'status']


class order_count_by_event(APIView):
    queryset = Order.objects.all()
    #permission_classes = [IsAuthenticated, Is_orderowner]

    def get(self, request, event, *args, **kwargs):
        count = self.queryset.filter(event=event).count()
        content = {'order_count': count}
        return Response(content, status=200)


class order_Retrieve(RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = order_Serializer
    #permission_classes = [IsAuthenticated, Is_orderowner]


class order_Update(UpdateAPIView):
    queryset = Order.objects.all()
    lookup_field = 'pk'
    serializer_class = order_Serializer
    #permission_classes = [IsAuthenticated, Is_orderowner]

    def put(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)


class order_Destroy(DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = order_Serializer
    #permission_classes = [IsAuthenticated, Is_orderowner]


class order_Create(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = order_Serializer
    #permission_classes = [IsAuthenticated]
