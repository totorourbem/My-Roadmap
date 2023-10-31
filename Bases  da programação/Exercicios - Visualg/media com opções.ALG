Algoritmo "MédiaComOpções"

Var
   // Seção de Declarações das variáveis
   media, nota1, nota2, nota3, nota4: REAL
   //Real por tratar-se de numeros decimais

Inicio
   // Seção de Comandos, procedimento, funções, operadores, etc...
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
         ESCREVA ("Você foi Aprovado!")
         SENÃO
         ESCREVA ("Você foi reprovado!")
         FIMSE
Fimalgoritmo