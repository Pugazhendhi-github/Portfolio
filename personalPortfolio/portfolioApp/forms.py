from django import forms
from portfolioApp.models import PortfolioForm


class PortfolioForm(forms.ModelForm):
    class Meta:
        model = PortfolioForm
        fields = '__all__'



