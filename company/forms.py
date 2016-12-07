from django.forms import *
from .models import Company
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from company.models import Benefit


class ProfileEditForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProfileEditForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'
        self.helper.add_input(Submit('submit', 'Kaydet'))

    class Meta:
        model = Company
        fields = '__all__'


class ServiceUseForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ServiceUseForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Kaydet'))

    class Meta:
        model = Benefit
        fields = ('supplier_service',)

    def save(self, **kwargs):
        benefit = super(ServiceUseForm, self).save(commit=False)
        benefit.employe_id = kwargs.get('employe_id')
        benefit.save()
