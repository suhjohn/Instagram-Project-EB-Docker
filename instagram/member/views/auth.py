from django.conf import settings
from django.contrib.auth import get_user_model, logout as django_logout, login as django_login, authenticate
from django.shortcuts import render, redirect

from ..forms import SignUpForm, LoginForm

# Create your views here.

__all__ = [
    'login',
    'logout',
    'signup',
]

User = get_user_model()


def login(request):
    """
    로그인 기능
    :param request:
    :return:
    """
    next_path = request.GET.get('next')
    login_form = LoginForm(request.POST, )

    if login_form.is_valid():
        login_form.login(request)
        if next_path:
            return redirect(next_path)
        return redirect('post:post_list')

    context = {
        'login_form': login_form,
        'facebook_app_scope': ','.join(settings.FACEBOOK_APP_SCOPE),
        'facebook_app_id': settings.FACEBOOK_APP_ID,
    }
    return render(request, 'member/login.html', context)


def logout(request):
    """
    로그아웃 기능
    :param request:
    :return:
    """
    django_logout(request)
    return redirect('member:login')


def signup(request):
    """
    회원가입 기능
    :param request:
    :return:
    """
    signup_form = SignUpForm(request.POST, request.FILES, )
    if signup_form.is_valid():
        signup_form.save()
        new_user = authenticate(request, username=signup_form.cleaned_data['username'],
                                password=signup_form.cleaned_data['password2'])
        django_login(request, new_user)
        return redirect('post:post_list')
    context = {
        'signup_form': signup_form
    }

    return render(request, 'member/sign_up.html', context)

