from django import forms
from .models.screenshot import Screenshot

class ScreenshotForm(forms.ModelForm):
    class Meta:
        model = Screenshot
        fields = "__all__"
