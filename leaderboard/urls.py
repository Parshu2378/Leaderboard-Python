"""
URL configuration for leaderboard_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
    openapi.Info(
        title="Leaderboard API",
        default_version="v1",
        description="API documentation for the Leaderboard project",
    ),
    public=True,
    permission_classes=(AllowAny,),
)


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('leaderboard/', views.get_leaderboard, name='leaderboard'),
    path('winners/', views.get_winners, name='winners'),
    path('user/', views.add_user, name='add_user'),
    path('user/<int:user_id>/points/', views.update_points, name='update_points'),
    path('user/<int:user_id>/', views.get_user_details, name='get_user_details'),
    path('user/delete/', views.delete_user, name='delete_user'),
    path('grouped/', views.grouped_by_score, name='grouped_by_score'),
    
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),


]