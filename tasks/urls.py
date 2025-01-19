from django.urls import path
from .views import RegisterView, TaskListView, TaskDetailView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    #path('login/', TokenObtainPairView.as_view(), name='login'),
    #path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', obtain_auth_token, name='api_token_auth'),
    path('api/token/', obtain_auth_token, name='api_token_auth'),
    path('tasks/', TaskListView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
]
