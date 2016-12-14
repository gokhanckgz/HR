from django.forms import *
from .models import Supplier
from company.models import Benefit
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, HTML, Field


class ProfileEditForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProfileEditForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'
        self.helper.add_input(Submit('submit', 'Kaydet'))
        self.helper.layout = Layout(
            Field('name'),
            Field('email'),
            Field('image'),
            HTML(
                """{% if form.image.value %}<img class="img-profile" src="{{ MEDIA_URL }}{{ form.image.value }}">{% endif %}"""),
        )

    class Meta:
        model = Supplier
        fields = ('name', 'email', 'image')


class ServiceUseForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ServiceUseForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Kaydet'))

    class Meta:
        model = Benefit
        fields = ('service',)

    def save(self, **kwargs):
        benefit = super(ServiceUseForm, self).save(commit=False)
        benefit.employe_id = kwargs.get('employe_id')
        benefit.save()
