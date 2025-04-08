from django.db import models

especialidades = (
    ('pd', 'pediatra'),
    ('cg', 'clinico geral'),
    ('of', 'oftamologista'),
)

status_field = (
    ("agendado","agendado"),
    ("realizado", "realizado"),
    ("cancelado", "cancelado")
)
class Medico(models.Model):
    nome = models.CharField(max_length=255)
    especialidade = models.CharField(max_length=255, choices=especialidades)
    crm = models.CharField(max_length=255, primary_key=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.nome
    
class Consulta(models.Model):
    paciente = models.CharField(max_length=255)
    data = models.DateTimeField()
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    status = models.CharField(max_length=255, choices=status_field)

    def __str__(self):
        return self.paciente
# Create your models here.
