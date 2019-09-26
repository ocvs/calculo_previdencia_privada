from django.forms import Form, fields


class SimulatorForm(Form):
    idade_atual = fields.IntegerField(min_value=0)
    idade_saida = fields.IntegerField(min_value=50)
    rentabilidade_anual = fields.DecimalField(min_value=0, decimal_places=2)
    contribuicao_mensal = fields.DecimalField(min_value=0, decimal_places=2)
    # rentabilidade_anual = fields.IntegerField(min_value=0)
    # contribuicao_mensal = fields.IntegerField(min_value=0)
    sexo = fields.ChoiceField(choices=(('M', 'M'), ('F', 'F')))
