from django import forms
from django.contrib.auth.models import User

# cadastrar usuario 
class CadastroUsuarioForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])  # Criptografa a senha
        user.is_superuser = False
        user.is_staff = False
        if commit:
            user.save()
        return user
