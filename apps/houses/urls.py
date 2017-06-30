from django.conf.urls import url, include
from apps.houses.api import house_cards, index_house_cards, devices, index_school_cards, filter_devices

extra_urlpatterns = [
    url(r'^index_house_cards', index_house_cards),
    url(r'^index_school_cards', index_school_cards),
    url(r'^house_cards/(?P<school>.+)$', house_cards),
    url(r'^devices', devices),
    url(r'^selected_devices', filter_devices),
]

urlpatterns = [
    url(r'^api/v1.0/', include(extra_urlpatterns))
]