from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, HTML
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from notice.models import Notice as NoticeModel


class NoticeForm(forms.ModelForm):
    class Meta:
        model = NoticeModel
        fields = ['name', 'email', 'message', 'pub_date', 'image']

    def __init__(self, *args, **kwargs):
        super(NoticeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.disable_csrf = True
        self.helper.layout = Layout(
            'title',
            'description',
            'imagefile',
            HTML(
                """{% if form.imagefile.value %}<img class="img-responsive" src="{{ MEDIA_URL }}{{ form.imagefile.value }}">{% endif %}""", ),
            'flag_featured',
        )

class NoticeImageForm(forms.Form):
    image = forms.ImageField(required=True)


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
