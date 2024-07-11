from django.urls import path
from .views import InterestListCreateView, InterestUpdateView

urlpatterns = [
    path('', InterestListCreateView.as_view(), name='interest_list_create'),
    path('<int:pk>/', InterestUpdateView.as_view(), name='interest_update'),
]
