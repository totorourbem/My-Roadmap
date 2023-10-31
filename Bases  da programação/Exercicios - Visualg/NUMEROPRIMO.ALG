Algoritmo "NumeroPrimo"
Var
contador : INTEIRO //base pra fórmula
numero : INTEIRO //userimput
eprimo : LOGICO  //o que a gente procura
Inicio
ESCREVA("Informe um número para verificar se ele é primo: ")
LEIA(numero)
eprimo := VERDADEIRO
PARA contador DE 2 ATÉ numero-1 FAÇA  //contador começa em 2 porque divsior por 1 da resto zero e quebra o loop, e até é numero-1 pelo mesmo motivo.
SE (numero MOD contador) = 0 ENTAO  //se resto de numero divido por contador é igual a zero,
eprimo := FALSO
FIMSE
FIMPARA
SE eprimo = VERDADEIRO ENTAO
ESCREVA("O número ", numero, " é primo!")
SENAO
ESCREVA("O número ", numero, " NÃO é primo!")
FIMSE
Fimalgoritmo