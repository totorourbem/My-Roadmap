algoritmo "divisãoValores"

var
   dividendo, divisor, quociente, resto : REAL
inicio
   ESCREVA ("Digite um valor para a para o dividendo: ")
   Leia (dividendo)
   ESCREVA ("Digite um valor para a para o divisor: ")
   Leia (divisor)
   quociente <- dividendo div divisor
   resto <- dividendo % divisor
   ESCREVA(dividendo, divisor, resto, quociente)
   ESCREVAL (dividendo, " | ", divisor)
   ESCREVAL ("    ", " ", "_____")
   ESCREVAL (resto, " ", quociente)
fimalgoritmo
