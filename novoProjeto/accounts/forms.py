from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

from novoProjeto.accounts.models import PasswordReset
from novoProjeto.core.mail import send_mail_template
from novoProjeto.core.utils import generate_hash_key

User = get_user_model()


class PasswordResetForm(forms.Form):
    email= forms.EmailField(label='E-mail')

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            return email
        raise forms.ValidationError('Nenhum usuário encontrado com este e-mail')

    def save(self):
        user = User.objects.get(email=self.cleaned_data['email'])
        key = generate_hash_key(user.username)
        reset = PasswordReset(key=key, user=user)
        reset.save()
        template_name = 'accounts/password_reset_mail.html'
        subject = 'Criar nova senha no PUC Online'
        context = {
            'reset': reset,
        }
        send_mail_template(subject, template_name, context, [user.email])


class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmação de senha', widget=forms.PasswordInput)

    def clean_passwords2(self):
        passwords1 = self.cleaned_data.get("password1")
        passwords2 = self.cleaned_data.get("password2")
        if passwords1 and passwords2 and passwords1 != passwords2:
            raise forms.ValidationError('A confirmação de senha não está correta')
        return passwords2

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ['username', 'email']


class EditAccountForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'name']