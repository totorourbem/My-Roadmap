// Adicione um título simples ao site com o id 'titulo', e um elemento 
// que represente um produto à venda. O produto precisa incluir pelo  
// o nome, a descrição e o preço.
// Procure usar o método simples e o método complexo.

//Criando Elementos no DOM - createElement

let tagproduto = document.createElement('div');
let fotoProduto = document.createElement('div');

// Atribuição de ids ou classes - .id e .className

tagproduto.id = 'descricaoGelo'
fotoProduto.id = 'fotoGelo'

// Populando os elementos - innerText e innerHTML

tagproduto.innerHTML = 
`
<h2 class='titulo'>"GELO! Gelado e molhado!"</h2>
<p class=produto-texto> Seu melhor amigo nos dias quentes! Esse objeto super cool é perfeito para refrescar sua bebida, aliviar a dor de uma pancada ou até mesmo fazer experiências científicas malucas! 😜 <br>
Composto por moléculas de água congelada, o gelo é a solução para todos os seus problemas calorosos. 💦💨 E não se preocupe, ele não faz bagunça e não precisa de cuidados especiais. <br>
Basta colocá-lo no freezer e pronto! E se você comprar agora, ganha um brinde especial: um cubinho de gelo com formato de unicórnio! 🦄🌈 Não perca essa oportunidade de ter o gelo mais estiloso do pedaço! 😎❄️ <br>
Apenas R$ 9,99! R$ 9,99!!!</p>
`
fotoProduto.innerHTML = 
`
<img src='https://s2.glbimg.com/Yc9YoNBKKDqA1hlhsTqc1xKdpgk=/1200x/smart/filters:cover():strip_icc()/s.glbimg.com/po/rc/media/2014/09/13/13_51_49_265_cubos_de_gelo.jpg' width='300' height='300' >
`

// Adicionado os elementos ao site - getElementbyID e appendChild:

let listaProduto = document.getElementById('lista-produto');
listaProduto.appendChild(tagproduto);
listaProduto.appendChild(fotoProduto);

