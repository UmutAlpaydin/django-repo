from django import forms
options = (
    ("1", "Add"),
    ("2", "Sub"),
    ("3", "Mul"),
    ("4", "Div"),
)

class Operation(forms.Form):
    first = forms.IntegerField()
    second = forms.IntegerField()
    opt_field = forms.ChoiceField(choices = options)