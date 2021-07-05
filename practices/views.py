from django.shortcuts import render, redirect
from django_filters import filters
from .models import Exercise, Solving
from .forms import ExerciseForm, SolveExerciseForm, AddAnswerExerciseForm, AddScoreToAnswerTeacherForm
from .filters import ExerciseFilter
from django.contrib.auth.decorators import login_required
from users.decorators import allowed_users
from users.models import Profile, User
from classroom.models import classroom



@login_required
def MyAnswersComment(request, pk):
    profile = Profile.objects.get(user=request.user.id)
    answer = Solving.objects.get(id=pk)
    context = {'profile': profile, 'answer': answer}
    return render(request,"practices/my_answers_comment.html", context)

@login_required
def MyAnswers(request):
    profile = Profile.objects.get(user=request.user.id)
    answer = Solving.objects.filter(user_profile=profile)
    context = {'profile': profile, 'answer': answer}
    return render(request,"classroom/student_profile.html", context)


@login_required
def Scoreboard(request):
    all_score = Profile.objects.all().order_by('-score')
    return render(request,"practices/scoreboard.html",{'Score': all_score})


@login_required
@allowed_users(allowed_roles=['admin','teacher'])
def AddScoreToAnswerTeacher(request, pk, profile):
    answer = Solving.objects.get(id=pk)
    form = AddScoreToAnswerTeacherForm(instance=answer) # ez felelős, hogy mikor vissza megyünk az oldalra be vannak már állítva a dolgok, ahogy az adatbázisban voltak.
    profile_user = Profile.objects.get(id=profile)
    if request.method == 'POST':
        form = AddScoreToAnswerTeacherForm(request.POST, instance=answer)
        if form.is_valid():
            form.save()
            profile_user = Profile.objects.get(id=profile)
            profile_user.score += answer.score
            print(answer.score)
            print(profile_user.score)
            profile_user.save()
            return redirect('practices')
    
    context = {'form':form, 'answer': answer, 'profile':profile_user}
    return render(request,"practices/add_score_to_answer_teacher.html", context)


def ViewExerciseAll(request):
    all_exercise = Exercise.objects.all()
    myFilter = ExerciseFilter(request.GET,queryset=all_exercise)
    all_exercise = myFilter.qs
    context = {'Exercises':all_exercise, 'myFilter':myFilter}
    return render(request,"practices/view_exercise_all.html", context)

def ViewExercise(request,pk):
    exercise = Exercise.objects.get(id=pk)
    context = {'Exercise':exercise}
    return render(request,"practices/view_exercise.html", context)

@login_required
def ExerciseAnswer(request,pk):
    exercise = Exercise.objects.get(id=pk)
    user_profile = Profile.objects.get(user=request.user.id)
    answer = Solving.objects.filter(user_profile=user_profile, exercise=exercise)

    context = {'Exercise':exercise, 'Answer': answer, 'Profile': user_profile}
    return render(request,"practices/exercise_answer.html", context)

@login_required
def SolveExercise(request,pk):
    exercise = Exercise.objects.get(id=pk)
    solve_form = SolveExerciseForm()
    if request.method == 'POST':
        solve_form = SolveExerciseForm(request.POST)
        if solve_form.is_valid():
            solve = solve_form.save()
            solve.user_profile.add(request.user.profile)
            solve.exercise.add(exercise)
            return redirect('practices_student')

    context = {'Exercise':exercise,'Solve': solve_form}
    return render(request,"practices/solving.html", context)



def PracticesStudent(request):
    all_exercise = Exercise.objects.all()

    myFilter = ExerciseFilter(request.GET,queryset=all_exercise)
    all_exercise = myFilter.qs

    context = {'Exercises':all_exercise, 'myFilter':myFilter}
    return render(request,"practices/exercise_student.html", context)


@allowed_users(allowed_roles=['admin','teacher'])
def Practices(request):
    all_exercise = Exercise.objects.all()

    myFilter = ExerciseFilter(request.GET,queryset=all_exercise)
    all_exercise = myFilter.qs

    context = {'Exercises':all_exercise, 'myFilter':myFilter}
    return render(request,"practices/exercise.html", context)

@login_required
@allowed_users(allowed_roles=['admin','teacher'])
def CreateExercise(request):
    form = ExerciseForm()
    if request.method == 'POST':
        form = ExerciseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('practices')

    context = {'form':form}
    return render(request,"practices/exercise_form.html", context)

@login_required
@allowed_users(allowed_roles=['admin','teacher'])
def UpdateExercise(request, pk):
    exercise = Exercise.objects.get(id=pk)
    form = ExerciseForm(instance=exercise) # ez felelős, hogy mikor vissza megyünk az oldalra be vannak már állítva a dolgok, ahogy az adatbázisban voltak.
    
    if request.method == 'POST':
        form = ExerciseForm(request.POST, instance=exercise)
        if form.is_valid():
            form.save()
            return redirect('practices')
    
    context = {'form':form}
    return render(request,"practices/exercise_form.html", context)


@login_required
@allowed_users(allowed_roles=['admin','teacher'])
def DeleteExercise(request, pk):
    exercise = Exercise.objects.get(id=pk)
    if request.method == 'POST':
        exercise.delete()
        return redirect('practices')
    context = {'exercise':exercise}
    return render(request,"practices/delete.html", context)


@login_required
@allowed_users(allowed_roles=['admin','teacher'])
def AddAnswerExercise(request, pk):
    exercise = Exercise.objects.get(id=pk)
    form = AddAnswerExerciseForm(instance=exercise) # ez felelős, hogy mikor vissza megyünk az oldalra be vannak már állítva a dolgok, ahogy az adatbázisban voltak.
    
    if request.method == 'POST':
        form = AddAnswerExerciseForm(request.POST, instance=exercise)
        if form.is_valid():
            form.save()
            return redirect('practices')
    
    context = {'form':form}
    return render(request,"practices/teacher_add_answer.html", context)




@login_required
@allowed_users(allowed_roles=['admin','teacher'])
def AllAnswerExercise(request, pk):
    exercise = Exercise.objects.get(id=pk)
    answer = Solving.objects.filter(exercise=exercise)
    teacher_profile = Profile.objects.get(user=request.user.id)
    teacher_class = classroom.objects.filter(user_profile = teacher_profile)
    listA = []
    listB = []

    # az osszes  olyan profil amelyikkel a tanar egy csoportban van
    for i in teacher_class:
        for j in i.user_profile.all():
            listA.append(j.id)
        
    final_listA = list(dict.fromkeys(listA))
    # the users who send answer
    for x in answer:
        for y in x.user_profile.all():
            listB.append(y.id)
    
    final_listB = list(dict.fromkeys(listB))


    final_listA_as_set = set(final_listA)
    intersection = final_listA_as_set.intersection(final_listB)
    intersection_as_list = list(intersection)
    
    answer = Solving.objects.filter(exercise=exercise,user_profile__in=intersection_as_list)
    context = {'answer':answer, 'exercise': exercise, 'intersection_as_list': intersection_as_list}
    return render(request,"practices/student_answers.html", context)

