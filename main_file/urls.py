from django.urls import path
from .views import create_store,redirect_short_url
urlpatterns = [
    path("create/",create_store,name="create_data"),
    path("call/<str:code>/",redirect_short_url,name="call"),
]
    # path("get/",get,name="get"),
    # path('delete/',delete,name="delete")
