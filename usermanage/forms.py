from usermanage.models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from supplier.models import Supplier
from company.models import Employe,Company
from django import forms

class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('user_type', 'username',)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True , **kwargs):

        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            pass
        if user.user_type == 'Supplier':
            user.save()
            supplier = Supplier(user=user)
            supplier.save()
        elif user.user_type == 'Employe':
            user.save()
            company = Company.objects.get(user_id=kwargs.get('company_user_id'))
            employe = Employe(user=user,company=company)
            employe.save()
        elif user.user_type == 'Company':
            user.save()
            company = Company(user=user)
            company.save()

        return user

class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('user_type','username', 'password', 'date_of_birth', 'is_active', 'is_admin')

    def clean_password(self):
        return self.initial["password"]

