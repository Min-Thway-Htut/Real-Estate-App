from django.urls import path
from .views import (AgentListAPIView, GetProfileAPIView, TopAgentListAPIVIew, UpdateProfileAPIView)

urlpatterns = [
    path("me/", GetProfileAPIView.as_view(), name="get_profile"),
    path("update/<str:username>/", UpdateProfileAPIView.as_view(),
    name="update_profile"),
    path("agents/all/", AgentListAPIView.as_view(), name="all-agents"),
    path("top-agents/all/", TopAgentListAPIVIew.as_view(), name="top-agents")
]
