from django.shortcuts import render, redirect
from .models import *
from .filters import MedicoFilter
from .forms import MedicoForm, ConsultaForm


def listar_medicos(request):
    medico = Medico.objects.all()
    return render(request, 'clinica/listar_medicos.html', {'medico':medico})

def criar_consulta(request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            form.save()
            print(form)
            return redirect()
    else:
        form = ConsultaForm()
    return render(request, 'clinica/form_consulta.html', {'form':form})



