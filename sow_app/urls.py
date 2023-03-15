from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('<int:year>/<str:month>/', views.home, name="home"),
    path('all_clients', views.all_clients, name= 'all-clients'),
    path('show_client/<client_id>', views.show_client, name= 'show-client'),
    path('all_agents', views.all_agents, name= 'all-agents'),
    path('all_prop', views.all_prop, name= 'all-prop'),
    path('add_client', views.add_client, name= 'add-client'),
    path('add_property', views.add_property, name= 'add-property'),
    path('add_agent', views.add_agent, name= 'add-agent'),
    path('update_client/<client_id>', views.update_client, name= 'update-client'),
    path('update_agent/<agent_id>', views.update_agent, name= 'update-agent'),
    path('update_propert/<property_id>', views.update_property, name= 'update-property'),
    path('delete_client/<client_id>', views.delete_client, name= 'delete-client'),
    path('delete_property/<property_id>', views.delete_property, name= 'delete-property'),
    path('delete_agent/<agent_id>', views.delete_agent, name= 'delete-agent'),
    path('dashboard', views.dashboard, name= 'dashboard'),
    
]
