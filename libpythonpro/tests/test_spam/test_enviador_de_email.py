import pytest

from libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None

@pytest.mark.parametrize(
    'remetente',
    ['tonny_lee92@yahoo.com.br','iguinho@ig.com']
)
def test_remetente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
            remetente,
            'lee.tonny92@gmail.com',
            'Cursos Python Pro',
            'Ipsum Lorem'
        )
    assert remetente in resultado


@pytest.mark.parametrize(
    'remetente',
    ['','iguinho']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'lee.tonny92@gmail.com',
            'Cursos Python Pro',
            'Ipsum Lorem'
        )
