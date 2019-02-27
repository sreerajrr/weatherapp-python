from django.forms import ModelForm,TextInput,forms
from  .models import city
class CityForm(ModelForm):
    class Meta:
        model = city
        fields = ['name']
        widgets = {
            'name' : TextInput(attrs={'class' : 'input' , 'placeholder': 'City Name'})
        }
    def clean_name(self,*args ,**kwargs):
        name = self.cleaned_data.get('name')
        name_qs = city.objects.filter(name=name)
        if name_qs.exists():
            return 'as'

        return name
