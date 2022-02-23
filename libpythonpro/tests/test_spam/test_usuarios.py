from libpythonpro.spam.modelos import Usuario


def test_salvar_usuario(conexao, sessao):
    usuario = Usuario(nome='Lee', email='tonny_lee92@yahoo.com.br')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(conexao, sessao):
    usuarios = [
        Usuario(nome='Lee', email='tonny_lee92@yahoo.com.br'),
        Usuario(nome='Ig', email='iguinho@ig.com.br')
    ]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
