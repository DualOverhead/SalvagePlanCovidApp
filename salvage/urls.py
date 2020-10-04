
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('changedforgithubrepo/', admin.site.urls),
    path('changedforgithubrepo/', include('django.contrib.auth.urls')),
    path('changedforgithubrepo/', include('accounts.urls')),
    path('help/', include('salvagehelp.urls')),
    path('', include('salvageplan.urls'))
]
