from unittest.mock import Mock

import pytest

from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario



@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Lee', email='tonny_lee92@yahoo.com.br'),
            Usuario(nome='Ig', email='iguinho@ig.com.br')
        ],
        [
            Usuario(nome='Lee', email='tonny_lee92@yahoo.com.br')
        ]
    ]
)
def test_qtd_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'tonny_lee92@yahoo.com.br',
        'Curso Python Pro',
        'Confira os módulos'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Lee', email='tonny_lee92@yahoo.com.br')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'iguinho@ig.com.br',
        'Curso Python Pro',
        'Confira os módulos'
    )
    enviador.enviar.assert_called_once_with(
        'iguinho@ig.com.br',
        'tonny_lee92@yahoo.com.br',
        'Curso Python Pro',
        'Confira os módulos'
    )
