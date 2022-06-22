from django.test import TestCase
from django.db import IntegrityError
from receitapp.models import Receita, Categoria


class ReceitaModelTestCase(TestCase):
    ''' Classe de testes para o modelo de receita '''
    
    def setUp(self):
        # Dificuldade choices
        self.nivel_dificuldade = [
            ('F', 'Facil'),
            ('M', 'Medio'),
            ('D', 'Dificil'),
        ]

        # Instancia de Receita
        self.receita = Receita.objects.create(
            ingrediente='TextField',
            modo_preparo='TextField',
            imagem='ImageField.jpg',
            nome='CharField',
            preparada=False,
            tempo_preparo='00:00',
            dificuldade=self.nivel_dificuldade,
            categoria=Categoria.objects.create(nome='Categoria')
        )
    
    def test_receita_tipo_campos(self):
        ''' teste para validar se campos de receita recebem os tipos corretos '''
        
        receita = self.receita
        self.assertIsInstance(receita.nome, str)
        self.assertIsInstance(receita.preparada, bool)
        self.assertIsInstance(receita.ingrediente, str)
        self.assertIsInstance(receita.dificuldade, list)
        self.assertIsInstance(receita.modo_preparo, str)
        self.assertIsInstance(receita.tempo_preparo, str)
        self.assertIsInstance(receita.categoria, Categoria)

    def test_se_receita_e_valida(self):
        ''' teste para validar se campos estao armazenando os valores corretos '''
        
        receita = self.receita
        self.assertIsInstance(receita, Receita)
        self.assertEqual(receita.preparada, False)
        self.assertEqual(receita.nome, 'CharField')
        self.assertEqual(receita.tempo_preparo, '00:00')
        self.assertEqual(receita.ingrediente, 'TextField')
        self.assertEqual(receita.modo_preparo, 'TextField')
        self.assertEqual(receita.dificuldade, self.nivel_dificuldade)
        self.assertEqual(receita.categoria, Categoria.objects.get(nome='Categoria'))

    def test_receita_tempo_preparo_e_valido(self):
        pass


class CategoriaModelTestCase(TestCase):
    ''' Classe de testes para o modelo de categoria '''
    
    def setUp(self):
        self.categoria = Categoria(
            nome='Salgado'
        )

    def test_se_categoria_e_unica(self):
        ''' teste para verificar se categoria sobe excessao ao tentar salvar uma que ja existe '''

        Categoria.objects.create(nome='Salgado')
        with self.assertRaises(IntegrityError):
            Categoria.objects.create(nome='Salgado')

    def test_categoria_tipo_campos(self):
        ''' teste para validar se campos de categoria recebem os tipos corretos '''

        self.assertIsInstance(self.categoria.nome, str)
        
    def test_if_categoria_e_valida(self):
        ''' teste para validar se campos estao armazenando os valores corretos '''
        self.assertEqual(self.categoria.nome, 'Salgado')
