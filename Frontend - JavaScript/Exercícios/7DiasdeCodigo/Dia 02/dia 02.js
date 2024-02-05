nome = prompt("digite o seu primeiro nome?")
idade = parseInt(prompt("Qual sua idade?"))
linguagem = prompt("Qyal linguagem você está estudando?")
cidade = prompt("Em qual cidade você mora?")

alert (`Ola, ${nome}! Que bom saber que você tem ${idade} anos e está estudando ${linguagem}.`)

let questao;

do {questao = parseInt(prompt(`Você gosta de estudsar a linguagem ${linguagem}? Digite 1 - para SIM ou 2 - para NÃO:`))

    if (questao == 1) {
        alert(`Que bom que você gosta de estudar a linguagem ${linguagem, nome}!`)
    }else if (questao == 2) {
        alert(`Que pena, {nome}.. Seraá que o que falta é um curso presencial em sua cidade, ${cidade}?`)
    }else{
        console.log(`{nome}, não reconheci sua resposta`)
    }
} while (questao < 1 || questao >2)