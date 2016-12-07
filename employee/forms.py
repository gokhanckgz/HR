from django import forms as form
from django.forms import *
from company.models import Employe
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit,Layout,Field,HTML,Fieldset
from crispy_forms.bootstrap import InlineField


class ProfileEditForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProfileEditForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.form_action = 'submit_survey'
        self.helper.add_input(Submit('submit', 'Kaydet'))
        self.helper.layout = Layout(
            Field('name'),
            Field('surname'),
            HTML("<b>Kredi</b>"),
            InlineField('credit', readonly=True),
            Field('image'),
        )
    class Meta:
        model = Employe
        fields = ['name','surname','credit','image']

class CreditTransferForm(Form):
    username = form.CharField()
    credit = form.IntegerField()
    def __init__(self, *args, **kwargs):
        super(CreditTransferForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.form_action = ''
        self.helper.add_input(Submit('submit', 'Gonder'))