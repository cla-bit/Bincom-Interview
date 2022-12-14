from django.urls import path
from .views import HomeView, AddVoterView, AddWardView

app_name = "poll"

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('add-user/', AddVoterView.as_view(), name='voter'),
    path('add-ward/', AddWardView.as_view(), name='ward')
]
