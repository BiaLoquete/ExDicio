Alunos = {'ALAN': 'Aluno 1', 'ANA ALICE': 'Aluno 2', 'ANA LUIZA': 'Aluno 3', 'BRENO': 'Aluno 4', 'BRUNO CARVALHO': 'Aluno 5', 'BRUNO OTÁVIO': 'Aluno 6', 'DAVI BIAZOTO': 'Aluno 7', 'DAVI TREVISAN': 'Aluno 8', 'EMILLY ': 'Aluno 9', 'FILIPE': 'Aluno 10', 'GEOVANA ': 'Aluno 11', 'GUILHERME NUNES': 'Aluno 12', 'HEITOR': 'Aluno 13', 'JOÃO PEDRO BERTELLI': 'Aluno 14', 'JOÃO PEDRO MORELLI': 'Aluno 15', 'JOÃO PEDRO MILANI': 'Aluno 16', 'JULIA DESIATO': 'Aluno 17', 'JULIA GARCIA': 'Aluno 18', 'KAIQUE': 'Aluno 19', 'KAROLINE': 'Aluno 20', 'KAUÊ': 'Aluno 21', 'KRISTHYAN': 'Aluno 22', 'LAURA': 'Aluno 23', 'LEONARDO': 'Aluno 24', 'LORENA': 'Aluno 25', 'MARIA CLARA': 'Aluno 26', 'MARIANA': 'Aluno 27', 'MATHEUS': 'Aluno 28', 'PEDRO': 'Aluno 29', 'TAYNÁ': 'Aluno 30', 'VITOR': 'Aluno 31', 'YAN': 'Aluno 32', 'YASMIM RAÍSSA': 'Aluno 33', 'YASMIN SARAH': 'Aluno 34'}

de = str (input('Digite o nome que deseja deletar de letra maiúscula: '))
if de in Alunos.keys():
    del Alunos[de]
print(Alunos)