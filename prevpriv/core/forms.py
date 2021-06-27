from django.forms import Form, fields




class SimulatorForm(Form):
    idade_atual = fields.IntegerField(min_value=0)
    idade_saida = fields.IntegerField(min_value=50)
    rentabilidade_anual = fields.FloatField(min_value=0)
    contribuicao_mensal = fields.FloatField(min_value=0)
    # rentabilidade_anual = fields.IntegerField(min_value=0)
    # contribuicao_mensal = fields.IntegerField(min_value=0)
    sexo = fields.ChoiceField(choices=(('M', 'M'), ('F', 'F')))
