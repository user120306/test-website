from django import forms
import re
from django.core.exceptions import ObjectDoesNotExist
from django.forms import ModelForm
from data.models import *

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email','fname',)

    class Meta:
        model = User
        fields = ('email','fname',)