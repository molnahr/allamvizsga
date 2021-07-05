from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
from practices import views  
from classroom import views as classroom_views

urlpatterns = [

    path('student_profile/<str:pk>/',classroom_views.student_profile, name = 'student_profile'),
    path('all_students/<str:pk>/',classroom_views.all_students, name = 'all_students'),
    path('create_classroom/',classroom_views.create_classroom, name = 'create_classroom'),
    path('processing/',classroom_views.processing, name = 'processing'),
    path('join/',classroom_views.join, name = 'join'),
    path('my_classroom/',classroom_views.my_classroom, name = 'my_classroom'),

    path('teacher_or_student_registration/', user_views.teacher_or_student_registration, name='teacher_or_student_registration'),
    path('teacher_register/', user_views.teacher_register, name='teacher_register'),

    path('my_answers_comment/<str:pk>/', views.MyAnswersComment, name = 'my_answers_comment'),
    path('my_answers/', views.MyAnswers, name = 'my_answers'),
    path('add_score_to_answer_teacher/<str:pk>/<str:profile>/', views.AddScoreToAnswerTeacher, name = 'add_score_to_answer_teacher'),
    path('view_exercise_all/', views.ViewExerciseAll, name = 'view_exercise_all'),
    path('view_exercise/<str:pk>/', views.ViewExercise, name = 'view_exercise'),
    path('exercise_answer/<str:pk>/', views.ExerciseAnswer, name = 'exercise_answer'),
    path('all_answer_exercise/<str:pk>/', views.AllAnswerExercise, name = 'all_answer_exercise'),
    path('add_answer_exercise/<str:pk>/', views.AddAnswerExercise, name = 'add_answer_exercise'),
    path('delete_exercise/<str:pk>/', views.DeleteExercise, name = 'delete_exercise'),
    path('update_exercise/<str:pk>/', views.UpdateExercise, name = 'update_exercise'),
    path('create_exercise/', views.CreateExercise, name = 'create_exercise'),
    path('scoreboard/',views.Scoreboard,name = 'scoreboard'),
    path('solve_exercise/<str:pk>',views.SolveExercise, name = 'solve_exercise'),
    path('practices_student/',views.PracticesStudent, name = 'practices_student'),
    path('practices/',views.Practices, name = 'practices'),
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='users/password_reset.html'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='users/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='users/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='users/password_reset_complete.html'
         ),
         name='password_reset_complete'),
    
    path('', include('blog.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
