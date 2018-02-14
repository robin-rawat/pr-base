from django import forms
from .models import BucxMember


class MemberForm(forms.ModelForm):
    class Meta:
            model = BucxMember
            fields = [
            "u_name",
            "bio",
            "location",
            "birth_date",
]
