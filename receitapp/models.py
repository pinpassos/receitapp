from django.db import models
from receitapp.validators.model_validator import RegexValidatorTempoPreparo, verifica_se_imagem_valida


class Receita(models.Model):
    '''
    '''

    NIVEL_DIFICULDADE = [
        ('F', 'Facil'),
        ('M', 'Medio'),
        ('D', 'Dificil'),
    ]

    ingrediente = models.TextField('Ingredientes')
    modo_preparo = models.TextField('Mode de preparo')
    nome = models.CharField('Nome da receita', max_length=160)
    preparada = models.BooleanField('Receita preparada', default=False)
    imagem = models.ImageField(
        'Imagem', upload_to='img', null=True, blank=True, validators=[verifica_se_imagem_valida])
    tempo_preparo = models.CharField(
        'Tempo de preparo', max_length=5, help_text='HH:MM', validators=[RegexValidatorTempoPreparo])
    dificuldade = models.CharField(
        'Dificuldade', max_length=10, choices=NIVEL_DIFICULDADE)
    categoria = models.ForeignKey(
        'Categoria', related_name='categoria_receita', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nome


class Categoria(models.Model):
    '''
    '''

    nome = models.CharField('Categoria', max_length=100, unique=True)

    def save(self, *args, **kwargs):
        self.nome = self.nome.capitalize()
        super(Categoria, self).save(*args, **kwargs)

    def __str__(self):
        return self.nome
