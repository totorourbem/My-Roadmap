Algoritmo "SacarDinheiro"

Var
// Se��o de Declara��es das vari�veis 
   SaldoDisponivel, ValorDoSaque : REAL

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
     SaldoDisponivel := 1000 //Assumimos que haja 100 lulas de saldo
     ESCREVA ("Informe o valor do saque:")
     LEIA (ValorDoSaque)
     SE ValorDoSaque <= SaldoDisponivel ENT�O
        SaldoDisponivel := SaldoDisponivel - ValorDoSaque
        ESCREVAL ("Sacando R$ ", ValorDoSaque, ".")
     SENAO
        ESCREVAL ("O valor solicitado � maior que o valor dispon�vel para saque!")
     FIMSE

     ESCREVAL ("Saldo Dispon�vel: R$",SaldoDisponivel)
Fimalgoritmo