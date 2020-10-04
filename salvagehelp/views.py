from django.shortcuts import render
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from salvageplan.models import Help

class HelpDeleteView(DeleteView):
    model = Help
    template_name = 'offer_delete.html'
    success_url = reverse_lazy('home')


