from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField(label='Select an Excel/CSV file')