from django.urls import path
from .views import RoomView, ListRoomView

urlpatterns = [
    path('createroom', RoomView.as_view()),
    path('listroom', ListRoomView.as_view())
]
