//Calculadora de Partidas rankeadas

// Variáveis, operadores, Loops. 
// estruturas de deciçoes e Funções

// Criar função que recebe como parâmetros a quantidade de vitórias
// e de derrotas de um jogador, depois disso retorne o resultado p/
//uma variável, e o saldo de Rankeadas deve ser feito atavés do 
// calculo (vitorias - derrotas)

// vitorias <= 10 = Ferro
// XP = 11 ~20 = Bronze
// XP = 21 ~50 = Prata
// XP = 51 ~80 = ouro
// XP = 81 ~90 = diamante
// XP = 91 ~100 = Lendário
// XP =  > 100 = Imortal


// Saída 
// "O herói tem um saldo de  {sadoVitorias} e está no níovel {nivel}"


function calculaRanking(vitorias, derrotas) {
    
    ranking = "";
    win = parseInt(vitorias);
    loss = parseInt(derrotas);

    let saldorankeadas = (win, loss) => win - loss;

    saldorankeadas = saldorankeadas(win, loss);

    if (saldorankeadas <= 10){
        ranking = 'Ferro';
    } else if (saldorankeadas <= 20){
        ranking = 'Bronze';
    } else if (saldorankeadas <= 50){
        ranking = 'Prata';
    } else if (saldorankeadas <= 80){
        ranking = 'Ouro';
    } else if (saldorankeadas <= 90){
        ranking = 'Diamante';
    } else if (saldorankeadas <= 100){
        ranking = 'Lendário';
    } else if (saldorankeadas > 100){
        ranking = 'Imortal';
    } else {
        console.log('O saldo entre vitórias e derrotas contém algum erro, pois o valor é de ',  saldorankeadas  + '. Poderia verificar novamente?')
    }
    console.log('"O herói tem um saldo de', saldorankeadas, 'e está no nível', ranking,'."');

}

calculaRanking(300, 20);