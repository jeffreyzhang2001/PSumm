from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import FormActions

class UnsummarizedTextForm(forms.Form):
    unsummarized_text = forms.CharField(widget=forms.Textarea(attrs={'rows': 17}), label='')
