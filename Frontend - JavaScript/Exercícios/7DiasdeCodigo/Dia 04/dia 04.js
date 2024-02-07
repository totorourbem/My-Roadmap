// Você já brincou de tentar adivinhar o número que seu amigo ou amiga estava pensando? Hoje você vai voltar na infância e fazer exatamente isso. Mas agora, o jogo vai ser contra o próprio computador!
// Você deve criar um programinha que comece com um valor específico pré-definido entre 0 a 10 para o número que você vai adivinhar (7, por exemplo).
// Em seguida, o programa vai perguntar para você qual o valor que você deseja chutar e, caso você acerte, ele irá te parabenizar. Caso erre, ele vai te dar mais 2 tentativas.
// No fim, caso você não acerte nenhuma vez, ele vai imprimir qual era o número inicial.
// Depois que o programinha estiver funcionando, tente usar um número randômico em vez de um número pré-definido.

numeroSecreto = Math.floor(Math.random() * (10 - 0 + 1) + 0)

tentativa = parseInt(prompt("Digite um número inteiro de zero a 10?"))
tentativaNo = 0

while (tentativaNo < 3) {
    tentativaNo++;

    if (numeroSecreto === tentativa) {
        alert("Parabens, você acertou o numero secreto, que era " + numeroSecreto)
        break;
    } else if (numeroSecreto != tentativa) {
        alert("Que pena, você errou o numero secreto, e gastou uma tentativa. Restam " + (3 - tentativaNo) + " tentativas.")
        tentativaNo ++;
    } else if (tentativaNo === 3) {}   
        alert("Que pena, você errou o numero secreto, que era " + numeroSecreto);
        break;  
    }
