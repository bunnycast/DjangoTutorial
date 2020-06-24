from django.urls import path, include

from quickstart import views

# urlpatterns = [
#     path('users/', views.UserList.as_view()),
#     path('users/<int:pk>/', views.UserDetail.as_view()),
# ]

# from quickstart.views import UserViewSet
#
# user_list = UserViewSet.as_view({
#     'get': 'list'
# })
# user_derail = UserViewSet.as_view({
#     'get': 'retrieve'
# })
from snippets.urls import router

router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]