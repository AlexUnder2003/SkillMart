from django.views.generic import TemplateView, UpdateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.utils.timezone import now

from .forms import UserProfileForm
from .models import UserProfile


class MyAccountView(LoginRequiredMixin, TemplateView):
    template_name = 'pages/my_account.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_profile = UserProfile.objects.get(user=self.request.user)
        context.update({
            'now': now(),
            'user': self.request.user,
            'user_profile': user_profile,
            'form': UserProfileForm(instance=user_profile),
        })
        return context


class UpdateAccountView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'pages/my_account.html'

    def get_object(self, queryset=None):
        return UserProfile.objects.get(user=self.request.user)

    def form_valid(self, form):
        user = self.request.user
        user.username = form.cleaned_data['username']
        user.email = form.cleaned_data['email']
        user.save()

        messages.success(self.request, 'Profile updated successfully.')
        return redirect('account:my_account')

    def form_invalid(self, form):
        messages.error(self.request, 'Please correct the errors below.')
        return super().form_invalid(form)


class LogoutUserView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('main:index')
