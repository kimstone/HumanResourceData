from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserAccountAuthenticationForm, UserAccountRegistrationForm, UserAccountUpdateForm
from django.contrib.auth import login, logout, authenticate

from .models import UserAccount


def edit_profile_view(request, *args, **kwargs):
    context = {}

    if not request.user.is_authenticated:
        return redirect("login")

    user_id = kwargs.get("user_id")

    try:
        account = UserAccount.objects.get(pk=user_id)
    except UserAccount.DoesNotExist:
        return HttpResponse("Something went wrong.")

    if account.pk != request.user.pk:
        return HttpResponse("You cannot edit someone elses profile.")

    if request.POST:
        form = UserAccountUpdateForm(request.POST, instance=request.user)
        print(form)
        if form.is_valid():
            form.save()
            return redirect("apps.access_control:show", user_id=account.pk)
        else:
            form = UserAccountUpdateForm(
                request.POST,
                instance=request.user,
                initial={
                    "id": account.pk,
                    "email": account.email,
                    "username": account.username,
                    "firstname": account.firstname,
                    "lastname": account.lastname,
                    "birthdate": account.birthdate,
                    "hiredate": account.hire_date,
                    "startdate": account.start_date,
                    "enddate": account.end_date,
                    "hide_email": account.hide_email,
                }
            )

            context['form'] = form

    else:
        form = UserAccountUpdateForm(
            initial={
                "id": account.pk,
                "email": account.email,
                "username": account.username,
                "firstname": account.firstname,
                "lastname": account.lastname,
                "birthdate": account.birthdate,
                "hiredate": account.hire_date,
                "startdate": account.start_date,
                "enddate": account.end_date,
                "hide_email": account.hide_email,
            }
        )
        context['form'] = form

    return render(request, "access_control/edit_profile.html", context)


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


def get_redirect_if_exists(request):
    redirect = None
    if request.GET:
        if request.GET.get("next"):
            redirect = str(request.GET.get("next"))
    return redirect


def login_view(request, *args, **kwargs):
    context = {}

    user = request.user
    """
    if user.is_authenticated:
        return redirect("/")
    """

    destination = get_redirect_if_exists(request)
    print("destination: " + str(destination))


    if request.POST:
        form = UserAccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                if destination:
                    return redirect(destination)
                return redirect("/")

    else:
        form = UserAccountAuthenticationForm()

    context['login_form'] = form

    return render(request, "access_control/login.html", context)


def logout_view(request):
    logout(request)
    return redirect("/")


def view_account_view(request, *args, **kwargs):
    context = {}
    user_id = kwargs.get("user_id")

    try:
        account = UserAccount.objects.get(pk=user_id)
    except:
        return HttpResponse("Something went wrong.")

    if account:
        context['id'] = account.id
        context['username'] = account.username
        context['email'] = account.email
        context['firstname'] = account.firstname
        context['lastname'] = account.lastname
        context['hide_email'] = account.hide_email
        context['birthdate'] = account.birthdate
        context['hire_date'] = account.hire_date
        context['start_date'] = account.start_date
        context['end_date'] = account.end_date
        context['department'] = account.department
        context['job'] = account.job

    return render(request, "access_control/view_profile.html", context)