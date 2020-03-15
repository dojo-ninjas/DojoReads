from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('apps.log_reg.urls')),
    url(r'^books/', include('apps.app1.urls')),
]