from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.utils.timezone import now

from .models import UserProfile


@login_required
def my_account(request):
    user_profile = UserProfile.objects.get(user=request.user)

    return render(request, 'pages/my_account.html', {
        'now': now(),
        'user': request.user,
        'user_profile': user_profile
    })


@login_required
def update_account(request):
    user_profile = UserProfile.objects.get(user=request.user)

    if request.method == 'POST':
        # Обработка формы
        request.user.username = request.POST.get('username')
        request.user.email = request.POST.get('email')
        user_profile.address = request.POST.get('address')
        user_profile.address2 = request.POST.get('address2')
        user_profile.birthday = request.POST.get('birthday')
        user_profile.gender = request.POST.get('gender')

        # Сохранение изменений
        request.user.save()
        user_profile.save()

        messages.success(request, 'Profile updated successfully.')
        return redirect('account:my_account')

    return render(request, 'pages/my_account.html', {
        'user': request.user,
        'user_profile': user_profile
    })


@login_required
def logout_user(request):
    logout(request)
    return redirect('main:index')  # Или любой другой URL
