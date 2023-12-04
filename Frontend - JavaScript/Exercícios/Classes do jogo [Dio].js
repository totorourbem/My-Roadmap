// # 3️⃣ Escrevendo as classes de um Jogo

// **O Que deve ser utilizado**

// - Variáveis
// - Operadores
// - Laços de repetição
// - Estruturas de decisões
// - Funções
// - Classes e Objetos

// ## Objetivo:

// Crie uma classe generica que represente um herói de uma aventura e que possua as seguintes propriedades:

// - nome
// - idade
// - tipo (ex: guerreiro, mago, monge, ninja )

// além disso, deve ter um método chamado atacar que deve atender os seguientes requisitos:

// - exibir a mensagem: "o {tipo} atacou usando {ataque}")
// - aonde o {tipo} deve ser concatenando o tipo que está na propriedade da classe
// - e no {ataque} deve seguir uma descrição diferente conforme o tipo, seguindo a tabela abaixo:

// se mago -> no ataque exibir (usou magia)
// se guerreiro -> no ataque exibir (usou espada)
// se monge -> no ataque exibir (usou artes marciais)
// se ninja -> no ataque exibir (usou shuriken)

// ## Saída

// Ao final deve se exibir uma mensagem:

// - "o {tipo} atacou usando {ataque}"
//   ex: mago atacou usando magia
//   guerreiro atacou usando espada

class hero {
    constructor(nome, idade, tipo) {

    if (tipo === 'mago'||tipo === 'guerreiro'||tipo === 'monge'||tipo === 'ninja') {
        this.nome = nome;
        this.idade = parseInt(idade);
        this.tipo = tipo;
    } else {
        console.log('Revise os valores digitados, por gentileza!')
    }
        
    }
    atacar() {
        if (this.tipo === 'mago') {
        console.log(`o ${this.tipo} ${this.name} atacou usando magia.`)
        } else if (this.tipo === 'guerreiro') {
        console.log(`o ${this.tipo} ${this.name} atacou usando espada.`)
    }    else if (this.tipo === 'monge') {
        console.log(`o ${this.tipo} ${this.name} atacou usando artes marciais.`)
        } else {
        console.log(`o ${this.tipo} ${this.name} atacou usando shurikens.`)
        }
    }
}


let guerreiro= new hero('Krogar', 32, 'guerreiro')
let mago= new hero('Kyros', 41, 'mago')
let monge= new hero('Yue', 22, 'monge')
let ninja= new hero('chin', 18, 'ninja')

guerreiro.atacar();
mago.atacar();
monge.atacar();
ninja.atacar();


let geraErro= new hero('Erradin', 99, 'erro')