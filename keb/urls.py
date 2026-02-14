from django.urls import path

from . import views
urlpatterns = [
    path("",views.Home.as_view(),name="home"),
    path("<int:pk>/",views.detail_kteb,name="detail_kteb"),
    path("add_new/",views.add_kteb,name="add_kteb"),
    path("<int:pk>/update/",views.Update_kteb.as_view(),name="update_kteb"),
    path("<int:pk>/delete/",views.Delete_kteb.as_view(),name="delete_kteb"),
]
