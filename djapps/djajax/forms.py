from django import forms

class ContactForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        CHOICES3 = (('1','First'),('2','Second'),)
        self.fields['field1'] = forms.CharField(label='Field Text', max_length=64)
        self.fields['field2'] = forms.CharField(label='Field Long Text', max_length=240, widget=forms.Textarea)
        self.fields['field3'] = forms.ChoiceField(label='Field MultiChoices', widget=forms.CheckboxSelectMultiple, choices=CHOICES3 )        