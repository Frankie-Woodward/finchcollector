from django.urls import path 
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('evs/', views.all_evs, name='index'),
  path('evs/<int:ev_id>/', views.evs_detail, name='detail'),
  path('evs/create/', views.EvCreate.as_view(), name='evs_create'),
  path('evs/<int:pk>/update/', views.EvUpdate.as_view(), name='edit_ev'),
  path('evs/<int:pk>/delete/', views.EvDelete.as_view(), name='evs_delete'),
  path('evs/<int:ev_id>/add_charging/', views.add_charging, name='add_charging'),

]