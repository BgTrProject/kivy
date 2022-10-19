from django import forms

GEEKS_CHOICES = (
    ("1", "Anytime"),
    ("2", "Two"),
    ("3", "Three"),
    ("4", "Four"),
    ("5", "Five"),
)



class GeeksForm(forms.Form):
    geeks_field = forms.ChoiceField(choices=GEEKS_CHOICES)