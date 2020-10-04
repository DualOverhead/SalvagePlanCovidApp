from django.urls import path

from .views import HelpDeleteView

from . import views

urlpatterns = [
path('<int:pk>/delete', HelpDeleteView.as_view(), name='helpapp_delete')
]