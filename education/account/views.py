from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.utils.timezone import now

from .forms import UserProfileForm
from .models import UserProfile


@login_required
def my_account(request):
    user_profile = UserProfile.objects.get(user=request.user)
    form = UserProfileForm(instance=user_profile)

    return render(request, 'pages/my_account.html', {
        'now': now(),
        'user': request.user,
        'user_profile': user_profile,
        'form': form,
    })


@login_required
def update_account(request):
    user_profile = UserProfile.objects.get(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            user = request.user
            user.username = form.cleaned_data['username']
            user.email = form.cleaned_data['email']
            user.save()

            form.save()

            messages.success(request, 'Profile updated successfully.')
            return redirect('account:my_account')
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'pages/my_account.html', {
        'form': form,
        'user': request.user,
        'user_profile': user_profile,
        'now': now(),
    })


@login_required
def logout_user(request):
    logout(request)
    return redirect('main:index')
