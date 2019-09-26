from django.shortcuts import render
from calculos.rodar_simulacao import calcula
from prevpriv.core.forms import SimulatorForm


def simulator(request):
    form = SimulatorForm(request.GET)

    if form.is_valid():
        saldo, renda_mensal_vitalicia = calcula(**form.cleaned_data)

        context = {
            'renda_mensal_vitalicia': renda_mensal_vitalicia,
            'saldo': saldo,
            'form': form,
        }
    else:
        context = {}
    
    return render(request, 'index.html', context)
