from bson import ObjectId
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django_filters import rest_framework as filters
from rest_framework import viewsets, mixins
from rest_framework.exceptions import NotFound
from rest_framework.filters import SearchFilter
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from mozio.infrastructure import pymongo
from providers.models import Provider, ServiceArea
from providers.serializers import ProviderSerializer, ServiceAreaSerializer


class CreateListViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    pass


class ProviderViewSet(viewsets.ModelViewSet):
    serializer_class = ProviderSerializer
    queryset = Provider.objects.all()
    lookup_field = '_id'
    lookup_value_regex = '[0-9a-f]{24}'
    filter_backends = (filters.DjangoFilterBackend, SearchFilter)
    filterset_fields = ('name', 'email', 'phone_number', 'language', 'currency',)
    search_fields = ('name', 'email', 'phone_number',)

    @method_decorator(cache_page(60))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return self.queryset.order_by('-name')

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = get_object_or_404(queryset, _id=ObjectId(self.kwargs['_id']))

        self.check_object_permissions(self.request, obj)

        return obj


class ServiceAreaViewSet(viewsets.ModelViewSet):
    serializer_class = ServiceAreaSerializer
    queryset = ServiceArea.objects.all()
    lookup_field = '_id'
    lookup_value_regex = '[0-9a-f]{24}'
    filter_backends = (filters.DjangoFilterBackend, SearchFilter)
    filterset_fields = ('name', 'price')
    search_fields = ('name',)

    @method_decorator(cache_page(60))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def validate_provider_id(self, provider_id):
        provider = Provider.objects.filter(_id=ObjectId(provider_id)).exists()
        if not provider:
            raise NotFound('Provider not found')

    def get_queryset(self):
        return self.queryset.order_by('-name')

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = get_object_or_404(queryset, _id=ObjectId(self.kwargs['_id']))

        self.check_object_permissions(self.request, obj)

        return obj


class ProvidersByServiceAreaLocation(APIView):
    @method_decorator(cache_page(60))
    def get(self, request):
        lat = self.request.query_params.get('lat')
        lng = self.request.query_params.get('lng')

        if lat is None or lng is None:
            return Response([])

        providers = pymongo.get_collection('providers_provider').aggregate([
            {
                '$lookup': {
                    'from': 'providers_servicearea',
                    'as': 'service_areas',
                    'localField': '_id',
                    'foreignField': 'provider_id',
                    'pipeline': [
                        {
                            '$match': {
                                'location': {
                                    '$geoIntersects': {
                                        '$geometry': {'type': 'Point', 'coordinates': [float(lng), float(lat)]}}}
                            }
                        }
                    ]
                }
            },
            {'$match': {'service_areas': {'$exists': True, '$ne': []}}}
        ])

        providers = list(providers)
        for p, provider in enumerate(providers):
            providers[p]['_id'] = str(provider['_id'])
            providers[p]['created_at'] = str(provider['created_at'])
            providers[p]['updated_at'] = str(provider['updated_at'])

            for s, service_area in enumerate(provider['service_areas']):
                providers[p]['service_areas'][s].pop('provider_id')
                providers[p]['service_areas'][s]['_id'] = str(service_area['_id'])
                providers[p]['service_areas'][s]['created_at'] = str(service_area['created_at'])
                providers[p]['service_areas'][s]['updated_at'] = str(service_area['updated_at'])

        return HttpResponse(providers, content_type='application/json')
