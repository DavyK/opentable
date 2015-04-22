from django import forms
from django.contrib.auth.admin import User, UserCreationForm
from django.contrib.auth.hashers import check_password
from django.db.models import Q


class LoginForm(forms.Form):

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'username'
    }), label='')

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'password',
    }), label='')

    class Meta:
        fields = ['username', 'password']

    def is_valid(self):
        """Taken from http://chriskief.com/2012/12/16/override-django-form-is_valid/
            with thanks!!!
        """

        # run the parent validation first
        valid = super(LoginForm, self).is_valid()

        # we're done now if not valid
        if not valid:
            return valid

        # so far so good, get this user based on the username or email
        try:
            user = User.objects.get(
                Q(username=self.cleaned_data['username'])
            )

        # no user with this username or email address
        except User.DoesNotExist:

            self.add_error('username', 'User does not exist')
            return False

        # verify the passwords match
        if not check_password(self.cleaned_data['password'], user.password):
            self.add_error('password', 'incorrect password')
            return False

        # all good
        return True


class CustomUserCreationForm(UserCreationForm):

    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


