from main.models import Offers
from django.forms import ModelForm, TextInput, FileInput, Textarea

class OffersForm(ModelForm):
    class Meta:
        model = Offers
        fields = ['name', 'number', 'mail', 'social_nets', 'description', 'files']
        
        widgets = {
            "name": TextInput(attrs={
                'class' : '__input',
                'placeholder' : 'Имя'
            }),
             "number": TextInput(attrs={
                'class' : '__input',
                'placeholder' : 'Телефон'
            }),
              "mail": TextInput(attrs={
                'class' : '__input',
                'placeholder' : 'Элетронная почта'
            }),
               "social_nets": TextInput(attrs={
                'class' : '__input',
                'placeholder' : 'Социальные сети'
            }),
                "description": Textarea(attrs={
                'class' : '',
                'placeholder' : 'Опишите заказ',
                'rows': '1',
                'cols' : '1'
            }),
                 "files": FileInput(attrs={
                'class' : '__input',
                'placeholder' : 'Файл'
            }),
            
        }