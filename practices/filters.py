from django.forms.widgets import Select
import django_filters
from django_filters.filters import Filter
from .models import *
from django_filters import DateFilter, CharFilter, ChoiceFilter

class ExerciseFilter(django_filters.FilterSet):
    #start_date = DateFilter(field_name="date_created", lookup_expr="gte")
    #end_date = DateFilter(field_name="date_created", lookup_expr="lte")
    # icontains = ignore Case Sensivity
    title = CharFilter(field_name="title", lookup_expr="icontains", label="Cím")
    level = ChoiceFilter(field_name="level", lookup_expr="icontains", label="Szint",choices=Exercise.LEVEL)
    exercise_type = ChoiceFilter(field_name="exercise_type", lookup_expr="icontains", label="Típus",choices=Exercise.EXERCISE_TYPE)

    class Meta:
        model = Exercise
        fields = ('title','level','exercise_type')

