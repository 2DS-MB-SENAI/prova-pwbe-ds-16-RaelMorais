import django_filters
from .models import Medico

class MedicoFilter(django_filters.FilterSet):
    especialidade = django_filters.ChoiceFilter(choices=Medico._meta.get_field('especialidade').choices, required=False)
