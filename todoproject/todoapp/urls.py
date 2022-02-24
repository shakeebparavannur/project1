from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('',views.home,name='home'),
    # path('details',views.details,name='details')
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:taskid>/',views.update,name='update'),
    path('cbvhome/',views.TaskViewList.as_view(),name='cbvhome'),
    path('cbvdetail/<int:pk>/',views.DetailsView.as_view(),name='cbvdetail'),
    path('cbvupdate/<int:pk>/',views.TaskUpdate.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>/',views.DeleteView.as_view(),name='cbvdelete')


]
