from django import forms

from .models import Help,Offer




class OfferForm(forms.ModelForm):

    class Meta:
        model=Offer
        fields = ['need_help', 'description',
                  'title',  'neighborhood']


class HelpForm(forms.ModelForm):
    

    class Meta:
        model = Help
        fields = ['need_help',  'description', 'title',  'neighborhood']
        labels = {'title':'Type of Item (please choose)', 'description': 'Brief Description of item you need help with', 'need_help':'Type of Help (Need or Offer)'}


