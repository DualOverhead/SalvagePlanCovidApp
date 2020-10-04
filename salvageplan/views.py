from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView,DeleteView
from .forms import HelpForm,OfferForm
from .models import Help,Offer
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import UserManager
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required


class HomePageView(TemplateView):
    template_name='home.html'


@login_required
def offer_page(request):
    form=OfferForm()
    user = request.user
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return render(request, 'home.html', {})
    else:
        
        return render(request, 'offer.html', {'form': form,"user":user})


@login_required
def help_page(request):
    form = HelpForm
    return render(request, 'help.html', {'form': form})


@login_required
def form_submit(request):
    form = OfferForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        fs= form.save(commit=False)
        fs.user= request.user
        fs.save()
        return HttpResponseRedirect(reverse('offer_posts'))
    else:
        form = OfferForm
    
    return render(request, 'offerpostview.html', {'form': form})



class OfferPostView(ListView):
    model=Offer
    template_name='offerpostview.html'
    ordering = ['-created_at']


class HelpPostView(ListView):
    model = Help
    template_name = 'helppostview.html'
    ordering = ['-created_at']


# VALIDATE FORM ENTRIES
def form_valid(self, form):
        form.instance.author = self.request.user


# CREATE POSTING FOR OFFER
class OfferCreateView(CreateView):
    model=Offer
    template_name='anotheroffer.html'
    fields = ('description', 'title', 'neighborhood')
    def form_valid(self,form):
        form.instance.author=self.request.user
        return super() .form_valid(form)


class OfferDeleteView(DeleteView):
    model=Offer
    template_name='offer_delete.html'
    success_url=reverse_lazy('home')


class HelpDeleteView(DeleteView):
    model = Help
    template_name = 'help_delete.html'
    success_url = reverse_lazy('home')

class DeletePostView(ListView):
    model = Offer
    template_name = 'deletepost.html'
    success_url = reverse_lazy('home')

class DeleteHelpPostView(ListView):
    model = Help
    template_name = 'help_delete.html'
    success_url = reverse_lazy('home')

# CREATE POSTING FOR HELP
class HelpCreateView(CreateView):
    model = Help
    template_name = 'anotheroffer.html'
    fields = ('description', 'title', 'neighborhood')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super() .form_valid(form)
    
# RESPOND TO POST
@login_required
def sendMessage(request):
    if request.method == 'POST':
	    email = request.POST['author_email']
    name = request.POST.get('author_name','')
    subject = request.POST.get('subject', '')
    
    print(email)  
    print(name)  
    print(subject)
    return render(request, 'send_message.html', {'email': email, 'name': name,'subject':subject})

# SEND RESPONSE EMAIL TO POST RESPONSE
@login_required
def sendEmail(request):
    email = request.user.email

    print(email)
    if request.method == 'POST':
        your_message = request.POST['your_message']
    rec_email = request.POST['email']

    print(your_message+"This is from sendmail")
    print(rec_email)

    send_mail(
        'You have a response from Salvage Plan',  # message
        your_message,  # subject
        email,  # from email
        [rec_email],  # To Email
    )

    return render(request, 'message_sent.html')



    
