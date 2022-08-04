resp = {}
def notas(*a, sit=False):
    """
    => função para analizar media de notas
    :param a: recebe notas dos alunos
    :param sit:(opcional) insere a situação do aluno
    :return: retorna o dicionario com  informações do aluno
    """
    resp['quantidade'] = len(a)
    resp['maior'] = max(a)
    resp['menor'] = min(a)
    resp['media'] = sum(a) / len(a)
    if sit:
        if resp['media'] < 6:
            resp['situação'] ='RUIM'
        elif 6 >= resp['media'] < 7:
            resp['situação'] = 'RAZOAVEL'
        else:
            resp['situação'] = 'OTIMA'
    return resp



dici = notas(3.5, 3.5, 7)
print(dici)
help(notas)
