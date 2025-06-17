#1. Crie uma função chamada boas_vindas() que imprima a mensagem "Bem-vindo(a)  disciplina ALLP"(Dica: não precisa de parâmetro!)
def boas_vindas():
  """
  Imprime a mensagem "Bem-vindo(a) à disciplina ALLP".
  """
  print("Bem-vindo(a) à disciplina ALLP")
# Chamando a função para ver a mensagem:
boas_vindas()

#2. Crie uma função chamada quadrado(numero) que receba um número como parâmetro e retorne o quadrado dele.
def quadrado(numero):
  """
  Calcula o quadrado de um número.
  Args:
    numero: O número a ser elevado ao quadrado.
  Returns:
    O quadrado do número.
  """
  return numero ** 2
# Exemplos de uso:
print(f"O quadrado de 5 é: {quadrado(5)}")
print(f"O quadrado de 10 é: {quadrado(10)}")
print(f"O quadrado de -3 é: {quadrado(-3)}")

#3. Crie uma função chamada somar(a, b) que receba dois números, some-os e retorne o resultado.
def somar(a, b):
  """
  Recebe dois números e retorna a soma deles.

  Args:
    a: O primeiro número.
    b: O segundo número.

  Returns:
    A soma de 'a' e 'b'.
  """
  return a + b

# Exemplos de uso:
print(f"A soma de 5 e 3 é: {somar(5, 3)}")
print(f"A soma de 10 e -2 é: {somar(10, -2)}")
print(f"A soma de 0 e 7 é: {somar(0, 7)}")

#4. Crie uma função chamada contagem(inicio=1, fim=5) que imprima uma contagem de inicio até fim (use range).(Teste a função passando e não passando parâmetros.)

def contagem(inicio=1, fim=5):
  """
  Imprime uma contagem de um número de início até um número de fim.

  Args:
    inicio: O número inicial da contagem (padrão é 1).
    fim: O número final da contagem (padrão é 5).
  """
  print(f"Contagem de {inicio} até {fim}:")
  for i in range(inicio, fim + 1): 
    print(i)
print("--- Teste passando parâmetros ---")
contagem(inicio=3, fim=7)
print("\n")
contagem(10, 15)
print("--- Teste não passando parâmetros ---")
contagem()

#5. Crie uma função chamada calcula_imc(peso=70, altura=1.75) que retorne o valor do IMC.(Fórmula: peso / altura²)
def calcula_imc(peso=70, altura=1.75):
  imc = peso / (altura ** 2)
  return imc
imc_padrao = calcula_imc()
print(f"O IMC padrão (peso=70kg, altura=1.75m) é: {imc_padrao:.2f}")
imc_exemplo1 = calcula_imc(peso=85, altura=1.80)
print(f"O IMC para peso=85kg e altura=1.80m é: {imc_exemplo1:.2f}")
imc_exemplo2 = calcula_imc(peso=60, altura=1.65)
print(f"O IMC para peso=60kg e altura=1.65m é: {imc_exemplo2:.2f}")

#6. Crie uma função chamada par_ou_impar(numero) que informe se o número é par ou ímpar.

def par_ou_impar(numero):
  """
  Verifica se um número é par ou ímpar e imprime o resultado.

  Args:
    numero: O número a ser verificado.
  """
  if numero % 2 == 0:
    print(f"O número {numero} é PAR.")
  else:
    print(f"O número {numero} é ÍMPAR.")


par_ou_impar(4)
par_ou_impar(7)
par_ou_impar(0)
par_ou_impar(13)

#7. Crie uma função chamada saudacao(nome="Visitante") que exiba uma mensagem de saudação com o nome passado.

def saudacao(nome="Visitante"):
  """
  Exibe uma mensagem de saudação personalizada.

  Args:
    nome: O nome da pessoa a ser saudada (padrão é "Visitante").
  """
  print(f"Olá, {nome}! Seja bem-vindo(a).")

# Exemplos de uso:
saudacao() # Usando o valor padrão
saudacao("Alice") # Passando um nome
saudacao(nome="Bruno") # Passando um nome explicitamente