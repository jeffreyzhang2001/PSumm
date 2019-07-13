from django.urls import path
from PSumm import views

urlpatterns = [
    path('', views.index, name='PSumm'),
    path('summarize/', views.summarize, name="PSumm")
]