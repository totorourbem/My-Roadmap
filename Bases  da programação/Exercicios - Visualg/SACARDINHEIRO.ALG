Algoritmo "SacarDinheiro"

Var
// Seção de Declarações das variáveis 
   SaldoDisponivel, ValorDoSaque : REAL

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
     SaldoDisponivel := 1000 //Assumimos que haja 100 lulas de saldo
     ESCREVA ("Informe o valor do saque:")
     LEIA (ValorDoSaque)
     SE ValorDoSaque <= SaldoDisponivel ENTÃO
        SaldoDisponivel := SaldoDisponivel - ValorDoSaque
        ESCREVAL ("Sacando R$ ", ValorDoSaque, ".")
     SENAO
        ESCREVAL ("O valor solicitado é maior que o valor disponível para saque!")
     FIMSE

     ESCREVAL ("Saldo Disponível: R$",SaldoDisponivel)
Fimalgoritmo