from django.urls import path
from Travel_blog.app.views.create import CreateDestinationView
from Travel_blog.app.views.index import IndexView
from Travel_blog.app.views.delete import destination_delete
from Travel_blog.app.views.details import destination_details
from Travel_blog.app.views.edit import destination_edit
from Travel_blog.app.views.likes import destination_likes
from Travel_blog.app.views.list import DestinationListView

urlpatterns = [
    path('list/', DestinationListView.as_view(), name='destination list'),
    path('details/<int:pk>/', destination_details, name='destination details'),
    path('edit/<int:pk>/', destination_edit, name='destination edit'),
    path('delete/<int:pk>/', destination_delete, name='destination delete'),
    path('like/<int:pk>/', destination_likes, name='destination likes'),
    path('', IndexView.as_view(), name='index'),
    path('create/', CreateDestinationView.as_view(), name='destination create'),
]
