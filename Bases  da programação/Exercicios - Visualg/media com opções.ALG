Algoritmo "M�diaComOp��es"

Var
   // Se��o de Declara��es das vari�veis
   media, nota1, nota2, nota3, nota4: REAL
   //Real por tratar-se de numeros decimais

Inicio
   // Se��o de Comandos, procedimento, fun��es, operadores, etc...
   ESCREVA("Digite a primeira nota:")
   LEIA(nota1)
   ESCREVA("Digite a segunda nota:")
   LEIA(nota2)
   ESCREVA("Digite a terceira nota:")
   LEIA(nota3)
   ESCREVA("Digite a quarta nota:")
   LEIA(nota4)
   media <- (nota1 + nota2 + nota3 + nota4)/4
         SE media >= 6 ENTAO
         ESCREVA ("Voc� foi Aprovado!")
         SEN�O
         ESCREVA ("Voc� foi reprovado!")
         FIMSE
Fimalgoritmo