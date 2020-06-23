from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet)

urlpatterns = [
    url('hello-view/', views.HelloApiView.as_view()),
    url('login/', views.UserLoginApiView.as_view()),
    url('', include(router.urls))
]
