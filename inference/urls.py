from django.urls import path
from inference import views

urlpatterns = [
    path("", views.InferenceView.as_view(), name="inference_view"),
]