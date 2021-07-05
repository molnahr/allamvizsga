from django.shortcuts import render
from users.models import Profile
from .models import classroom
from django.contrib.auth.models import User
import string
import secrets
from .forms import Join
from django.contrib import messages
from practices.models import Solving
from django.contrib.auth.decorators import login_required
from users.decorators import allowed_users

@login_required
@allowed_users(allowed_roles=['admin','teacher'])
def create_classroom(request):
    return render(request,"classroom/upload.html")


@login_required
@allowed_users(allowed_roles=['admin','teacher'])
def processing(request):
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(6))
    if request.method == "POST":
        name = classroom()
        name.classname = request.POST.get('class_name')
        name.creator = request.user
        name.code = password
        name.save()
    return render(request, "classroom/create.html", {'password': password, 'creator': name.creator, 'name': name.classname})


@login_required
def join(request):
    context = None
    if request.method == 'POST':
        form = Join(request.POST)
        if form.is_valid():
            passcode = form.cleaned_data['join']
            classrooms = classroom.objects.all()
            try:
                classroom_obj = classroom.objects.get(code=passcode)
            except classroom.DoesNotExist:
                messages.warning(
                    request, 'Sajnálom, helytelen belépő kód!'
                )
                return render(request, "classroom/no.html")

            classroom_obj.user_profile.add(request.user.profile)
            messages.success(
                request, 'Üdvözlöm! Ön sikeresen belépett az osztályba!'
            )
            return render(
                request, "classroom/okay.html",
                {'classrooms': classrooms, 'pswd': passcode}
            )

    else:
        form = Join()
        context = {"form": form}

    messages.info(request, 'Írja be az egyedi osztály azanosító kódot.')
    return render(request, "classroom/join.html", context if context else None)

@login_required
def my_classroom(request):
    profile = Profile.objects.get(user=request.user.id)
    my_class = classroom.objects.filter(user_profile = profile.id)
    context = {'my_class': my_class}
    return render(request, "classroom/my_classroom.html", context)

@login_required
def all_students(request, pk):
    actual_class = classroom.objects.get(id = pk)
    students = actual_class.user_profile.all()
    context = {'students': students}
    return render(request,"classroom/inner_classroom.html", context)

@login_required
@allowed_users(allowed_roles=['admin','teacher'])
def student_profile(request, pk):
    profile = Profile.objects.get(id=pk)
    answer = Solving.objects.filter(user_profile=profile)
    context = {'profile': profile, 'answer': answer}
    return render(request,"classroom/student_profile.html", context)
