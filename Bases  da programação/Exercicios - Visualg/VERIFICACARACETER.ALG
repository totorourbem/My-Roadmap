Algoritmo "VerificaCaraceter"

Var
   // Se��o de Declara��es das vari�veis
   letra: caractere //o que o user digita
   contador: inteiro  //o que o cod faz a equival�ncia

Inicio
   // Se��o de Comandos, procedimento, fun��es, operadores, etc...

   ESCREVA("Insira a Letra aqui:")
   LEIA(letra)
   ESCOLHA letra
   CASO "A"
      contador := 1
   CASO "B"
      contador := 2
   CASO "C"
      contador := 3
   CASO "D"
      contador := 4
   CASO "E"
      contador := 5
   CASO "F"
      contador := 6
   CASO "G"
      contador := 7
   CASO "H"
      contador := 8
   CASO "I"
      contador := 9
   CASO "J"
      contador := 10
   CASO "K"
      contador := 11
   CASO "L"
      contador := 12
   CASO "M"
      contador := 13
   CASO "N"
      contador := 14
   CASO "O"
      contador := 15
   CASO "P"
      contador := 16
   CASO "Q"
      contador := 17
   CASO "R"
      contador := 18
   CASO "S"
      contador := 19
   CASO "T"
      contador := 20
   CASO "U"
      contador := 21
   CASO "V"
      contador := 22
   CASO "W"
      contador := 23
   CASO "X"
      contador := 24
   CASO "Y"
      contador := 25
   CASO "Z"
      contador := 26
   OUTROCASO
      ESCREVA ("Esse n�o � um caracetere v�lido")
   FIMESCOLHA
   ESCREVA("A letra ", letra, " est� na posi��o", contador, " do alfabeto.")

FIMALGORITMO
