from django.urls import path, include
from .views import home_view, predict_view, predicted_list_view
urlpatterns = [
    path('', home_view),
    path('predict', predict_view),
    path('predicted', predicted_list_view, name='predicted')
]