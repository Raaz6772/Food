from .import views
from django.urls import path

app_name = 'food'
urlpatterns = [
    path("index/",views.IndexClassView.as_view(),name="index"),
    path("it/",views.it,name="it"),
    path("<int:pk>/",views.FoodDetail.as_view(),name="detail"),
    path("add/",views.createitem.as_view(),name="create_form"),
    path("update/<int:pk>/",views.updateitem.as_view(),name='update_item'),
    path("delete/<int:id>/",views.delete_item,name="delete_item"),
    ]