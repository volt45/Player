from django.contrib.auth.hashers import check_password, make_password
from django.http import HttpResponseRedirect
from django.shortcuts import render

from MusicPlayer.models import User, Music


def is_current_user(request):
    try:
        user = User.objects.get(Login=request.COOKIES.get('login'))
        return check_password(request.COOKIES.get("password"), user.Password)
    except:
        return False


def index(request):
    all_music = Music.objects.all()[:15]
    login = request.COOKIES.get("login")
    if not is_current_user(request):
        return HttpResponseRedirect(redirect_to="/")
    return render(request, 'player/templates/index.html',
                  context={"all_music": all_music, 'first': all_music[0], 'login': login})


def login(request):
    if request.POST.get("Login") is None:
        return render(request, "player/templates/login.html")
    user_login = request.POST.get("Login")
    user_password = request.POST.get("Password")
    if len(User.objects.filter(Login=user_login)) == 0:
        return render(
            request=request,
            template_name="player/templates/login.html"
        )
    user = User.objects.get(Login=user_login)
    if not check_password(user_password, user.Password):
        return render(
            request,
            "player/templates/login.html",
            context={"error": "Такого пользователя нет или неверный пароль"}
        )
    response = HttpResponseRedirect("/index")
    response.set_cookie("login", user_login, max_age=180)
    response.set_cookie("password", user_password, max_age=180)
    return response


def logout(request):
    response = HttpResponseRedirect("/")
    response.set_cookie("login", max_age=0)
    response.set_cookie("password", max_age=0)
    return response


def registration(request):
    if request.POST.get("Login") is None:
        return render(
            request=request,
            template_name="player/templates/registration.html"
        )
    user_firstname = request.POST.get("FirstName")
    user_lastname = request.POST.get("LastName")
    user_login = request.POST.get("Login")
    user_password = request.POST.get("Password")
    user_phone = request.POST.get("Phone")
    user_email = request.POST.get("Email")
    user_datebirth = request.POST.get("DateBirth")
    if len(User.objects.filter(Login=user_login)) != 0:
        return render(
            request,
            "player/templates/registration.html",
            context={"error": "Такой пользователь уже есть"}
        )
    else:
        User.objects.create(
            FirstName=user_firstname,
            LastName=user_lastname,
            Login=user_login,
            Password=make_password(user_password),
            Phone=user_phone,
            Email=user_email,
            DateBirth=user_datebirth,
        ).save()
        response = HttpResponseRedirect("/")
        response.set_cookie("login", user_login, max_age=86400)
        response.set_cookie("password", user_password, max_age=86400)
        return response
