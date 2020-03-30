from django.urls import path, include

urlpatterns = [
    path('', include('log_reg.urls')),
    path('books/', include('app1.urls')),
]