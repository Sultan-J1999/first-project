from django import forms



class MemberForms(forms.Form):
    date =forms.DateField(label="Date ")
    Location =forms.CharField(label="Location ",max_length=255)
    salary =forms.CharField(label="salary  ",max_length=255)
    description =forms.CharField(label="Descriptions ",max_length=255)