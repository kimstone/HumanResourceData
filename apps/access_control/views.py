from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserAccountRegistrationForm
from django.contrib.auth import login, logout, authenticate

def index_page_view(request, *args, **kwargs):
    context = {}
    return render(request, "access_control/index.html", context)


def register_view(request, *args, **kwargs):
    context = {}

    staff_member = request.user

    if staff_member.is_authenticated:
        return HttpResponse("You are already authenticated as " + str(staff_member.email))

    if request.POST:
        form = UserAccountRegistrationForm(request.POST)
        #profile_form = StaffProfileForm(request.POST)

        if form.is_valid():
            form.save()

            #profile = profile_form.save(commit=False)
            #profile.user = staff_member
            #profile.save()

            email = form.cleaned_data.get('email').lower()
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            destination = kwargs.get("next")
            if destination:
                return redirect(destination)
            return redirect('/')
        else:
            context['registration_form'] = form

    else:
        form = UserAccountRegistrationForm()
        #profile_form = StaffProfileForm()

        context['registration_form'] = form
        #context['profile_form'] = profile_form

    return render(request, 'access_control/register.html', context)