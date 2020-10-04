from django.urls import path
from .views import HomePageView, OfferCreateView, OfferPostView, OfferDeleteView, DeletePostView, DeleteHelpPostView, HelpCreateView, HelpPostView
from salvagehelp.views import HelpDeleteView
from . import views

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('offer/', OfferCreateView.as_view(), name='offer'),
    path('help/', HelpCreateView.as_view(), name='help'),
    path('offer_posts/', OfferPostView.as_view(), name='offer_posts'),
    path('help_posts/', HelpPostView.as_view(), name='help_posts'),
    path('delete_posts/', DeletePostView.as_view(), name='delete_posts'),
    path('delete_help_posts/', DeleteHelpPostView.as_view(),
         name='delete_help_posts'),
    path('submit/',views.form_submit, name='form_submit'),
    path('send_message/', views.sendMessage, name='message'),
    path('message_sent/', views.sendEmail, name='message_sent'),
    path('<int:pk>/delete',OfferDeleteView.as_view(),name='offer_delete'),
    path('help/<int:pk>/delete',HelpDeleteView.as_view(), name='help_delete')
]



