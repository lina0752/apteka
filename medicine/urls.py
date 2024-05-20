
from django.views.generic import TemplateView
from django.urls import path

from medicine.views import MedListView, MedDetailView, MedCreateView, MedUpdateView, MedDeleteView

app_name = 'medicine'

urlpatterns = [
    path('', MedListView.as_view(), name='list'),
    path('medicine/<int:pk>/', MedDetailView.as_view(), name='detail'),
    path('medicine/create/', MedCreateView.as_view(), name='create'),
    path('medicine/<int:pk>/update/', MedUpdateView.as_view(), name='update'),
    path('medicine/<int:pk>/delete/', MedDeleteView.as_view(), name='delete'),
]