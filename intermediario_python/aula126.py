# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}
# s1 = set('Maycon')
# s1 = set()  # vazio
# s1 = {'Maycon', 1, 2, 3}  # com dados

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)
lista1 = [1, 2, 3, 2, 3, 3, 3, 3]
# s1 = {1, 2, 3, 2, 3, 3, 3, 3}  # com dados
s1 = set(lista1)
lista2 = list(s1)

print(lista2)

# Métodos úteis:
# add, update, clear, discard

# s1.clear()
s1.discard('Olá mundo')
s1.discard('Luiz')
print(s1)
# print(s1)


# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em amboss1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2
s3 = s1 & s2
s3 = s2 - s1
s3 = s1 ^ s2
print(s3)