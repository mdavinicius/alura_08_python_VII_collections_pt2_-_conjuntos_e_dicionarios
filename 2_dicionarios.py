# criando um dicionário
aparicoes = {
    "Guilherme": 1,
    "cachorro": 2,
    "nome": 2,
    "vinho": 1
}
print(aparicoes)  # imprimindo o dicionário
print(aparicoes["Guilherme"])  # imprimindo o valor da chave 'Guilherme'
print(aparicoes["cachorro"])  # imprimindo o valor da chave 'cachorro'
print(aparicoes.get("xpto", 0))  # com o get() no dicionário, vamos procurar se existe "xpto", senão retornará 0
print("-----------------------------------")

aparicoes["Carlos"] = 1  # adicionando elementos ao dicionario, [key] = valor
print(aparicoes)
print("-----------------------------------")

aparicoes["Carlos"] = 3  # alterando valor de um valor
print(aparicoes)
print("-----------------------------------")

del aparicoes["Carlos"]  # removendo um elemento
print(aparicoes)
print("-----------------------------------")

print("cachorro" in aparicoes)  # buscando uma chave dentro de um dicionario
print("-----------------------------------")

for elemento in aparicoes:  # ao iterar sobre um dicionario, irá retornar sempre as chaves - pt.1
    print(elemento)
print("-----------------------------------")

for elemento in aparicoes.keys():  # iterando as chaves de forma declarada com keys() - pt.2
    print(elemento)
print("-----------------------------------")

for elemento in aparicoes.values():  # iterando sobre os valores com values()
    print(elemento)
print("-----------------------------------")

for elemento in aparicoes:  # iterando sobre keys and values 'grosseiramente'
    valor = aparicoes[elemento]
    print(elemento, ":", valor)
print("-----------------------------------")

for elemento in aparicoes.items():  # iterando sobre keys and values de forma pythonica com items() pt.1
    print(elemento)
print("-----------------------------------")

for chave, valor in aparicoes.items():  # iterando sobre keys and values de forma pythonica pt.2, desmembrando o dicionário
    print(chave, "=", valor)
print("-----------------------------------")

print(["palavra {}".format(chave) for chave in aparicoes.keys()])  # concatenando uma 'palavra' com cada chave
print("-----------------------------------")

# v1 - pegar uma string, por em minúsculo, separar por palavras e contar quants x cada palavra aparece
meu_texto = "Bem vindo meu nome é Vinicius e eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"
meu_texto = meu_texto.lower().split()  # colocar em minúsculo e separ por palavras (vai virar lista)
print("Printando 'meu_texto': ", meu_texto)

aparicoes = {}
for palavras in meu_texto:  # contar quantos vezes cada palavra aparece pt.1
    valor = aparicoes.get(palavras, 0)  # lembrando que o parâmetro do .get() em dicionários, se não encontrar a palavra, ira por value = 0
    aparicoes[palavras] = valor + 1
print("Printando 'aparicoes': ", aparicoes)
print("-----------------------------------")

# v2 - agora o mesmo exercício, porém com uma função que remove a necessidade de usar o .get, pois se não tiver o valor, adicionará 0 graças ao int()
from collections import defaultdict

meu_texto = "Bem vindo meu nome é Vinicius e eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"
meu_texto = meu_texto.lower().split()

aparicoes_v2 = defaultdict(int)
for elemento in meu_texto:
    aparicoes_v2[elemento] += 1
print("Printando 'aparicoes_v2': ", aparicoes_v2)
print("-----------------------------------")

print("A palavra 'meu' apareceu: {} vezes.".format(aparicoes_v2['meu']))  # print formatado mostrando quantas x uma determinada palavra aparece, puxando pela key
print("-----------------------------------")

# v3 - agora com Counter, ele já acessa o iterável. Resumindo tudo em 1 linha
from collections import Counter

meu_texto = "Bem vindo meu nome é Vinicius e eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"

aparicoes_v3 = Counter(meu_texto.lower().split())
print("Printando 'aparicoes_v3': ", aparicoes_v3)
print("-----------------------------------")
