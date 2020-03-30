from django.urls import path
from . import views
                    
urlpatterns = [
    path('', views.index),
    path('register/',views.register),
    path('login/',views.login),
    path('success/',views.success),
    path('logout/',views.logout),
    path('users/<int:my_id>/',views.userPage)
    #path('bears/<int:my_val>', views.another_method),
]