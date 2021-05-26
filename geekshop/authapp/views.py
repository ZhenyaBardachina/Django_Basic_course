from django.contrib import auth
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from authapp.forms import ShopUserLoginForm, ShopUserRegisterForm, ShopUserEditForm


def login(request):
    redirect_to = request.GET.get('next', '')

    login_form = ShopUserLoginForm(data=request.POST)
    if request.method == 'POST' and login_form.is_valid():
        username = request.POST.get('username')
        password = request.POST.get('password')
        redirect_to = request.POST.get('next')
        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(redirect_to or reverse('index'))
    else:
        form = ShopUserLoginForm()

    context = {
        'page_title': 'вход',
        'login_form': login_form,
        'redirect_to': redirect_to,
    }
    return render(request, 'authapp/login.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    if request.method == 'POST':
        register_form = ShopUserRegisterForm(request.POST, request.FILES)

        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        register_form = ShopUserRegisterForm()

    context = {
        'page_title': 'регистрация',
        'register_form': register_form,
    }

    return render(request, 'authapp/register.html', context)


def edit(request):
    if request.method == 'POST':
        edit_form = ShopUserEditForm(request.POST, request.FILES, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('auth:edit'))
    else:
        edit_form = ShopUserEditForm(instance=request.user)

    context = {
        'page_title': 'редактирование',
        'edit_form': edit_form,
    }

    return render(request, 'authapp/edit.html', context)

