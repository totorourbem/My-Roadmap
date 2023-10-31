algoritmo "JogoDaVelha"
var
   tabuleiro: vetor[1..3,1..3] de caractere
   nomeJogador1, nomeJogador2, jogadorAtual, vencedor : caractere
   linhaJogada, colunaJogada, i, j : inteiro
inicio
   escreval("###Jogo da velha###")
   //Inicialização do tabuleiro com "_" nas linhas 1 e 2 e " " na terceira linha
   //i é a linha e j é a coluna.
   para j de 1 ate 3 faca
      para i de 1 ate 2 faca
         tabuleiro[i,j] := "_"
      fimpara
      tabuleiro[3,j] := " "
   fimpara
   escreva("Informe o nome do(a) primeiro(a) jogador(a): ")
   leia(nomeJogador1)
   escreva("Informe o nome do(a) segundo(a) jogador(a): ")
   leia(nomeJogador2)
   escreval("Vamos começar o jogo.")
   jogadorAtual := nomeJogador1
   vencedor := ""
   repita
      //Apresenta a situação atual do tabuleiro
      escreval("Neste momento o tabuleiro está assim:")
      escreval(" 1 2 3")
      escreval("1 _", tabuleiro[1,1], "_|_", tabuleiro[1,2], "_|_", tabuleiro[1,3], "_")
      escreval("2 _", tabuleiro[2,1], "_|_", tabuleiro[2,2], "_|_", tabuleiro[2,3], "_")
      escreval("3 ", tabuleiro[3,1], " | ", tabuleiro[3,2], " | ", tabuleiro[3,3], " ")
      escreval("É a vez do(a) jogador(a): ", jogadorAtual)
      repita
         repita
            escreva("Informe o número da linha da sua jogada: ")
            leia(linhaJogada)
            //Valida se o usuário digitou um valor válido
            se (linhaJogada < 1) ou (linhaJogada > 3) entao
               escreval("A linha deve ser entre 1 e 3")
            fimse
         ate (linhaJogada >= 1) e (linhaJogada <= 3)
         repita
            escreva("Informe o número da coluna da sua jogada: ")
            leia(colunaJogada)
            //Valida se o usuário digitou um valor válido
            se ((colunaJogada < 1) ou (colunaJogada > 3)) entao
               escreval("A coluna deve ser entre 1 e 3")
            fimse
         ate ((colunaJogada >= 1) e (colunaJogada <= 3))
         //Valida se a posição jogada á está preenchida
         se (tabuleiro[linhaJogada,colunaJogada] <> "_") e
            (tabuleiro[linhaJogada,colunaJogada] <> " ") entao
            escreval("A posição ", linhaJogada,", ", colunaJogada, " já está
            preenchida.")
         fimse
      ate (tabuleiro[linhaJogada,colunaJogada] = "_") ou
      (tabuleiro[linhaJogada,colunaJogada] = " ")
      se jogadorAtual = nomeJogador1 entao
         tabuleiro[linhaJogada,colunaJogada] := "X"
         jogadorAtual := nomeJogador2
      senao
         tabuleiro[linhaJogada,colunaJogada] := "O"
         jogadorAtual := nomeJogador1
      fimse
      //Valida se alguem ganhou o jogo
      para j de 1 ate 3 faca
         //Verifica as colunas
         //_X_|_O_|_X_
         //_X_|_O_|_X_
         // X | O | X
         se ((tabuleiro[1,j] = "X") ou (tabuleiro[1,j] = "O")) e (tabuleiro[1,j] =
            tabuleiro[2,j]) e (tabuleiro[2,j] = tabuleiro[3,j]) entao
            vencedor := tabuleiro[1,j]
         fimse
      fimpara
      para i de 1 ate 3 faca
         //Verifica as linhas
         //_X_|_X_|_X_
         //_O_|_O_|_O_
         // X | X | X
         se ((tabuleiro[i,1] = "X") ou (tabuleiro[i,1] = "O")) e (tabuleiro[i,1] =
            tabuleiro[i,2]) e (tabuleiro[i,2] = tabuleiro[i,3]) entao
            vencedor := tabuleiro[i,1]
         fimse
      fimpara
      //Verifica as diagonais
      //_X_|___|_X_
      //___|_X_|___
      // X | | X
      se (((tabuleiro[2,2] = "X") ou (tabuleiro[2,2] = "O")) e ((tabuleiro[1,1] =
         tabuleiro[2,2]) e (tabuleiro[2,2] = tabuleiro[3,3])) ou ((tabuleiro[3,1] =
         tabuleiro[2,2]) e (tabuleiro[2,2] = tabuleiro[1,3]))) entao
         vencedor := tabuleiro[2,2]
      fimse
      //Verifica se deu velha
      se ((vencedor <> "") e (tabuleiro[1,1] <> "_") e (tabuleiro[1,2] <> "_") e
         (tabuleiro[1,3] <> "_") e (tabuleiro[2,1] <> "_") e (tabuleiro[2,2] <> "_") e
         (tabuleiro[2,3] <> "_") e (tabuleiro[3,1] <> " ") e (tabuleiro[3,2] <> " ") e
         (tabuleiro[3,3] <> " ")) entao
         vencedor := "V"
      fimse
   ate vencedor <> ""
   //Apresenta a situação atual do tabuleiro
   escreval("Neste momento o tabuleiro está assim:")
   escreval(" 1 2 3")
   escreval("1 _", tabuleiro[1,1], "_|_", tabuleiro[1,2], "_|_", tabuleiro[1,3], "_")
   escreval("2 _", tabuleiro[2,1], "_|_", tabuleiro[2,2], "_|_", tabuleiro[2,3], "_")
   escreval("3 ", tabuleiro[3,1], " | ", tabuleiro[3,2], " | ", tabuleiro[3,3], " ")
   se vencedor = "X" entao
      escreva("O vencedor do jogo foi: ", nomeJogador1)
   fimse
   se vencedor = "O" entao
      escreva("O vencedor do jogo foi: ", nomeJogador2)
   fimse
   se vencedor = "V" entao
      escreva("O jogo deu Velha!")
   fimse
fimalgoritmo