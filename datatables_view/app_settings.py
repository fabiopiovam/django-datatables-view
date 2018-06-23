from django.conf import settings

MAX_COLUMNS = getattr(settings, 'DATATABLES_VIEW_MAX_COLUMNS', 30)
ENABLE_QUERYDICT_TRACING = getattr(settings, 'DATATABLES_VIEW_ENABLE_QUERYDICT_TRACING', False)
ENABLE_QUERYSET_TRACING = getattr(settings, 'DATATABLES_VIEW_ENABLE_QUERYSET_TRACING', False)
