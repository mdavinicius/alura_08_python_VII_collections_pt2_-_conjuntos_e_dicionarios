# criando duas listas
usuarios_data_science = [15, 23, 34, 56]
usuarios_machine_learning = [13, 23, 56, 42]

# criando uma terceira lista sendo cópia da 1ª e anexando a 2ª na sequência
assistiram = usuarios_data_science.copy()
assistiram.extend(usuarios_machine_learning)  # ao usar o extend(), colocamos elementos repetidos
print(assistiram, len(assistiram))
print("-----------------------------------")

# a melhor forma para evitar repetição, é usando um set {}, que é um cojunto que não aceita itens repetidos, porém não é possível ordernar
assistiram = set(assistiram)  # set() para criar um conjunto, ou direto {}
print(assistiram, len(assistiram))
print("-----------------------------------")

# print(assistiram[3])  # dará erro, pois um set é um conjunto e conjunto não tem posição
print("Não é possível acessar a posição de um set, pois sets não tem posição")
print("-----------------------------------")

for usuarios in assistiram:  # mas é iterável
    print(usuarios)
print("-----------------------------------")

# pegando as listas anteriores e transformando em sets
usuarios_data_science = set(usuarios_data_science)
usuarios_machine_learning = set(usuarios_machine_learning)

print(usuarios_data_science | usuarios_machine_learning)  # '|' é 'ou' - apenas os elementos que estão em um conjunto ou no outro, sem repetir
print(usuarios_data_science & usuarios_machine_learning)  # '&' é 'e' - apenas os elementos que estão nos dois conjuntos
print(usuarios_data_science - usuarios_machine_learning)  # '-' é 'menos' - usuários do primeiro grupo menos do segundo grupo
print(usuarios_data_science ^ usuarios_machine_learning)  # '^' é 'ou exclusivo' - elementos de um conjunto ou outro, mas não presente nos dois ao mesmo tempo
print("-----------------------------------")

# será que o '15' fez data_science mas não fez machine_learning?
fez_ds_mas_nao_fez_ml = usuarios_data_science - usuarios_machine_learning
print(15 in fez_ds_mas_nao_fez_ml)
print("-----------------------------------")

# adicionando elementos no cojunto
usuarios_data_science.add(11)  # usa add() para adicionar
print(usuarios_data_science)
print("-----------------------------------")

# frozenset transforma o conjunto em imutavel
usuarios_frozen = frozenset(usuarios_data_science)
print(usuarios_frozen)
# usuarios_frozen.add(700)  # dará erro, pois o conjunto está congelado (imutavel)
print("-----------------------------------")

meu_texto = "Bem vindo meu nome é Vinicius e eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"
print(meu_texto.split())  # split quebra o texto em todos os espaços em branco (mas pode definir outro padrão)
meu_texto = set(meu_texto.split())  # agora fizemos um conjunto de palavras únicas
print(meu_texto)
print("-----------------------------------")

