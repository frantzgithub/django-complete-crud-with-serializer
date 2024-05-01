from django.urls import path
from .views import UserView, UserDetail

app_name = 'user'

urlpatterns = [
    path('users/', UserView.as_view(), name='user'),
    path('user/<int:user_id>/', UserDetail.as_view(), name="user_detail")
]
