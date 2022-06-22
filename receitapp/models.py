from django.db import models


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
        'Imagem', upload_to='img', null=True, blank=True)
    tempo_preparo = models.CharField(
        'Tempo de preparo', max_length=5, help_text='HH:MM')
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

    def __str__(self):
        return self.nome
