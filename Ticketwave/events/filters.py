from .models import Event
from django_filters import rest_framework as filters


class eventFilter(filters.FilterSet):

    class Meta:
        model = Event

        fields = {
            'id': ['exact', 'in'],
            'name': ['exact'],
            'owner': ['exact'],
            'category': ['exact'],
            'view_counter': ['exact', 'gte', 'lte'],
            'status': ['exact'],

            'start': ['exact', 'gte', 'lte'],
            'end': ['exact', 'gte', 'lte'],
            'created': ['exact', 'gte', 'lte'],
            'changed': ['exact', 'gte', 'lte'],

            'category': ['exact', 'in'],
            'category__parent_category': ['exact'],

            'venue': ['exact', 'in'],
            'venue__name': ['exact'],
            'venue__city': ['exact'],
            'venue__country': ['exact'],
            'venue__address': ['exact'],
            'venue__latitude': ['gte', 'lte'],
            'venue__longitude': ['gte', 'lte'],

        }

        # 'field1': ['in'], for multiple values example ?field1__in=value1,value2,value3
        # date range example ?created_at__gte=2022-01-01&created_at__lte=2022-01-31

        # went with specifying fields instead
        # exclude = ['summary', 'description', 'online_event', 'hide_start_date', 'hide_end_date', 'free', 'waitlist', \
        #    'listed', 'shareable', 'invite_only', 'show_remaining', 'password', 'capacity', 'capacity_is_custom']
        # removing boolean field filtiring cause djongo error and doing it manually
        # removing sensitive fields and other fields not appropriate to search

        # 'capacity': ['exact'], #removed capacity filtering as i didn't find it in eventbrite
