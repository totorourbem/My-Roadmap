// Adicione um título simples ao site com o id 'titulo', e um elemento 
// que represente um produto à venda. O produto precisa incluir pelo  
// o nome, a descrição e o preço.
// Procure usar o método simples e o método complexo.

//Criando Elementos no DOM - createElement

let tituloSimples = document.createElement('h1');
let descricaoGelo = document.createElement('p');

// Atribuição de ids ou classes - .id e .className

tituloSimples.id = 'titulo';

// Populando os elementos - innerText e innerHTML

tituloSimples.innerText = "GELO! Gelado e molhado!";
descricaoGelo.innerText = `
Seu melhor amigo nos dias quentes! Esse objeto super cool é perfeito para refrescar sua bebida, aliviar a dor de uma pancada ou até mesmo fazer experiências científicas malucas! 😜 
Composto por moléculas de água congelada, o gelo é a solução para todos os seus problemas calorosos. 💦💨 E não se preocupe, ele não faz bagunça e não precisa de cuidados especiais. 
Basta colocá-lo no freezer e pronto! E se você comprar agora, ganha um brinde especial: um cubinho de gelo com formato de unicórnio! 🦄🌈 Não perca essa oportunidade de ter o gelo mais estiloso do pedaço! 😎❄️ 
Apenas R$ 9,99! R$ 9,99!!!
`

// Adicionado os elementos ao site - querySelector e appendChild:
// Primeiro identifica o elemento pai e captura-o com queruySelector
// Depois, adiciona os elemeentos a ele com appendChild

let paginaDinamica = document.querySelector('body');

paginaDinamica.appendChild(tituloSimples);
paginaDinamica.appendChild(descricaoGelo);


console.log(tituloSimples)
console.log(descricaoGelo)
console.log(paginaDinamica)
