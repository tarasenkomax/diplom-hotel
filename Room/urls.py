from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from Room import views

urlpatterns = [
    # ----- Комнаты -----
    path('all_rooms', views.all_rooms, name='all_rooms'),
    path('room/<int:number>', views.detail_room, name='detail_room'),
    path('list_free_rooms', views.list_free_rooms, name='list_free_rooms'),
    path('reserve_room/<int:number>', views.reserve_room, name='reserve_room'),
    path('all_reserves', views.all_reserves, name='all_reserves'),
    path('cancel/<int:pk>', views.cancel, name='cancel'),
    path('pay/<int:number>', views.pay, name='pay'),
    # ----- Отзывы -----
    path('add_review/<int:pk>', views.add_review, name='add_review'),

    path('help_page', views.help_page, name='help_page'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
