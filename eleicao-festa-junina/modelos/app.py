from modelos.jurado import Jurado
from modelos.aluno import Aluno

mayki = Aluno('Mayki','Mister')
jurado = Jurado('Carléia', 'Educacional')

jurado.atribuir_nota(mayki, 0, 0, 0, 0)
jurado.atribuir_nota(mayki, 9, 9, 9, 9)

print(mayki)
