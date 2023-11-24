// Desafio Classificador de Nível de Herói
//Objetivo
// Crie uma variável para armazenar o nome e a quantidfade de experiência (XP)
// de herói;, depois, utilize uma estrutura de decisão para apresentar alguma
//  das mensafgens abaixo:

// XP < 1000 = Ferro
// XP = 1001 ~2000 = Bronze
// XP = 2001 ~5000 = Prata
// XP = 5001 ~7000 = ouro
// XP = 7001 ~8000 = Platina
// XP = 8001 ~9000 = Ascendente
// XP = 9001 ~10000 = Imortal
// XP = > 10000 = Radiante

// Saida

// "O herói de nome *[no do heroi]* está no nivel de *[nivel do heroi]*."


let nomeDoHeroi = "Link";
let XPLevel = 99999;
let categoria = ""

if (XPLevel <= 1000){
    categoria = 'Ferro';
    console.log("O herói de nome", nomeDoHeroi + " está no nível de " + categoria+"!")
} else if (XPLevel <= 2000){
    categoria = 'Bronze';
    console.log("O herói de nome", nomeDoHeroi + " está no nível de " + categoria+"!")
} else if (XPLevel <= 5000){
    categoria = 'Prata';
    console.log("O herói de nome", nomeDoHeroi + " está no nível de " + categoria+"!")
} else if (XPLevel <= 7000){
    categoria = 'Ouro';
    console.log("O herói de nome", nomeDoHeroi + " está no nível de " + categoria+"!")
} else if (XPLevel <= 8000){
    categoria = 'Platina';
    console.log("O herói de nome", nomeDoHeroi + " está no nível de " + categoria+"!")
} else if (XPLevel <= 9000){
    categoria = 'Ascendente';
    console.log("O herói de nome", nomeDoHeroi + " está no nível de " + categoria+"!")
} else if (XPLevel <= 10000){
    categoria = 'Imortal';
    console.log("O herói de nome", nomeDoHeroi + " está no nível de " + categoria+"!")
} else if (XPLevel > 10000){
    categoria = 'Radiante';
    console.log("O herói de nome", nomeDoHeroi + " está no nível de " + categoria+"!")
} else {
    console.log('Não pude reconhecer esse nivel, ',  XPLevel  + '. Poderia verificar novamente?')
}
