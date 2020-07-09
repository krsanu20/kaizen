from django  import forms
from oc.models import Customer,StudentDetail

class CustomerForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields='__all__'
class StudentForm(forms.ModelForm):
    email=forms.EmailField(required=False)
    class Meta:
        model=StudentDetail
        fields='__all__'