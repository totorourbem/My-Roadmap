Algoritmo "NumeroPrimo"
Var
contador : INTEIRO //base pra f�rmula
numero : INTEIRO //userimput
eprimo : LOGICO  //o que a gente procura
Inicio
ESCREVA("Informe um n�mero para verificar se ele � primo: ")
LEIA(numero)
eprimo := VERDADEIRO
PARA contador DE 2 AT� numero-1 FA�A  //contador come�a em 2 porque divsior por 1 da resto zero e quebra o loop, e at� � numero-1 pelo mesmo motivo.
SE (numero MOD contador) = 0 ENTAO  //se resto de numero divido por contador � igual a zero,
eprimo := FALSO
FIMSE
FIMPARA
SE eprimo = VERDADEIRO ENTAO
ESCREVA("O n�mero ", numero, " � primo!")
SENAO
ESCREVA("O n�mero ", numero, " N�O � primo!")
FIMSE
Fimalgoritmo