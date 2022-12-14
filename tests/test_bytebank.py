import pytest
from pytest import mark

from codigo.bytebank import Funcionario


class TestClass:
    def test_quando_idade_recebe_13_02_2000_deve_retornar_22(self):
        entrada = '13/03/2000'
        esperado = 22

        funcionario_teste = Funcionario('teste', entrada, 1111)

        resultado = funcionario_teste.idade()

        assert resultado == esperado

    def test_quando_sobrenome_recebe_lucas_carvalho_deve_retornar_apenas_carvalho(self):
        entrada = 'Lucas Carvalho'
        esperado = 'Carvalho'

        lucas = Funcionario(entrada, '11/11/2000', 1111)
        resultado = lucas.sobrenome()

        assert resultado == esperado

    def test_quando_decrecimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada_salario = 100000
        entrada_nome = 'Paulo Bragança'
        esperado = 90000

        funcionario_teste = Funcionario(entrada_nome, '11/11/1990', entrada_salario)
        funcionario_teste.decrescimo_salario()
        resultado = funcionario_teste.salario

        assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada = 1000
        esperado = 100

        funcionario = Funcionario('Teste', '11/11/2000', entrada)
        resultado = funcionario.calcular_bonus()

        assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            entrada = 1000000

            funcionario = Funcionario('Teste', '11/11/2000', entrada)
            resultado = funcionario.calcular_bonus()

            assert resultado
