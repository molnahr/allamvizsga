from practices import views    

urlpatterns = [
path('scoreboard',views.Scoreboard, name = 'scoreboard'),
path('solve_exercise/<str:pk>',views.SolveExercise, name = 'solve_exercise'),
path('practices',views.Practices, name = 'practices'),
path('practices_student',views.PracticesStudent, name = 'practices_student'),
path('create_exercise', views.CreateExercise, name = 'create_exercise'),
path('update_exercise/<str:pk>', views.UpdateExercise, name = 'update_exercise'),
path('delete_exercise/<str:pk>', views.DeleteExercise, name = 'delete_exercise'),
]
