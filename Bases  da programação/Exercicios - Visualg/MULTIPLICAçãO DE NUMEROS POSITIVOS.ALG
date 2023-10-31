algoritmo "multiplicaçãoValores"
var
fator1, fator2, resultado, contador : REAL
inicio
ESCREVA ("Digite um valor para a para o primeiro fator: ")
Leia (fator1)
ESCREVA ("Digite um valor para a para o segundo fator: ")
Leia (fator2)
resultado <- 0
contador <- 0
ENQUANTO contador < fator2 FAÇA
resultado <- resultado + fator1
contador <- contador +1 //unico problema é que isso obriga o fator2 a ser um numero inteiro e positivo
FIMENQUANTO
ESCREVA (resultado)
fimalgoritmo
