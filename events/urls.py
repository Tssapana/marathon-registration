from django.urls import path
from . import views
app_name='events'
urlpatterns = [
    path('', views.show_events, name='show_events'),
    path('event/<int:id>/', views.event_details, name='event_details'),
]
