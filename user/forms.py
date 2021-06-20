from django import forms
from django.contrib.auth.signals import user_logged_in
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class UsereditForm(forms.ModelForm):
    class Meta:
        model = User
        fields=(
            'picture',
            'full_name',
            'email',
            'bio',
            'website',
            'phone_number',
            'gender',
        )
