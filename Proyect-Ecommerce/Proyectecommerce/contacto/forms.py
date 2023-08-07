from django import forms

class FormContacto(forms.Form):

    name = forms.CharField(label="Nombre:",  required=True)

    surname = forms.CharField(label="Apellido:", required=True)

    email = forms.EmailField(label="Email:", required=True)
    
    consulta = forms.CharField(label="Consulta:",  required=True, widget=forms.Textarea)

