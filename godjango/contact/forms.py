from django import forms
from django.forms import ModelForm

from .models import Suggestion, Question

class FeedbackForm(forms.Form):
    email = forms.EmailField(label="Your email")
    name = forms.CharField(label="Name")
    message = forms.CharField(label="Body",widget=forms.Textarea)

class SuggestionForm(ModelForm):
    class Meta:
        model = Suggestion
        exclude = ('approved',)

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        exclude = ('answered',)
