from django import forms

from .models import User


class UserRegistrationForm(forms.ModelForm):
    """
    Форма регистрации пользователя.

    Эта форма используется для регистрации нового пользователя и включает в себя
    валидацию пароля. Содержит поля для имени пользователя, электронной почты и пароля.
    """

    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        """
        Проверяет, совпадают ли пароли.
        """
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Пароли не совпадают!")
