# Generated by Django 4.0.5 on 2022-06-22 20:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, unique=True, verbose_name='Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Receita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingrediente', models.TextField(verbose_name='Ingredientes')),
                ('modo_preparo', models.TextField(verbose_name='Mode de preparo')),
                ('nome', models.CharField(max_length=160, verbose_name='Nome da receita')),
                ('preparada', models.BooleanField(default=False, verbose_name='Receita preparada')),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='img', verbose_name='Imagem')),
                ('tempo_preparo', models.CharField(help_text='HH:MM', max_length=5, verbose_name='Tempo de preparo')),
                ('dificuldade', models.CharField(choices=[('F', 'Facil'), ('M', 'Medio'), ('D', 'Dificil')], max_length=10, verbose_name='Dificuldade')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='categoria_receita', to='receitapp.categoria')),
            ],
        ),
    ]
