// Manipulando estilos da DIV de texto
//IMPORTATE, para demosntração, é necessário ir comentando os blocos dos exercicios nanteriores no HTML e no JS

// let div = document.querySelector("div");
// div.style.color = "blue";
// div.style.fontSize = "16px";

// //Manipulandfo estilos com .style

// let div = document.querySelector("div");

// //verifica se incluiu a classe na div (aqui retorna true no console)
// let incluiClasse = div.classList.contains("borda-azul")
// console.log(incluiClasse);

// //verifica se incluiu a classe na div (aqui retorna false no console)
// incluiClasse = div.classList.contains("texto-novo")
// console.log(incluiClasse);

// //Adiciona uma class pré-configurada no CSS a um elemento HTML que não a contenha
// div.classList.add("texto-novo");

// //Removew uma class pré-configurada no CSS a um elemento HTML que não a contenha
// div.classList.remove("borda-azul");

// //Toggle: verifica a existencia da classe em um único comando(liga/desliga)
// div.classList.toggle("borda-azul");
// div.classList.toggle("borda-azul");

// Função .addEventListener

// //Captiurar elementos
// let numero = document.querySelector("h1");
// let botao = document.querySelector("button");

// //Declaração de variáveis/contadores
// let contagem = 0;

// // função a ser atribuida ao botão
// function adicionarUm(){
//     contagem = contagem + 1;
//     numero.innerText = contagem;
// }

// // Mostra o funcionamentoi manual da função
// // adicionarUm();
// // adicionarUm();

// //codgio que monitora um elemento, e vincula algio a uma ação feita nele
// //no caso "click" é ao clicar do botão, que chama a nossa função (args)
// botao.addEventListener("click", adicionarUm);

// Variáveis de escritas dessa parte do código - função anônima

// let numero = document.querySelector("h1");
// let botao = document.querySelector("button");
// let contagem = 0;

// botao.addEventListener("click", function(){
//   contagem = contagem + 1;
//   numero.innerText = contagem;
// });

// Variáveis de escritas dessa parte do código - arrow function

// let numero = document.querySelector("h1");
// let botao = document.querySelector("button");
// let contagem = 0;

// botao.addEventListener("click", () => {
//   contagem = contagem + 1;
//   numero.innerText = contagem;
// });

//Eventos de Mouse
// Selecionar elementos da página
let button = document.querySelector("button");
let span = document.querySelector("span");
let section = document.querySelector("section");

//Evento mouseover. funlção e chamada com addEventListener
function mostrarSpan(){
    span.style.opacity = "100"
}
button.addEventListener("mouseover", mostrarSpan);

//Evento mouseout. funlção e chamada com addEventListener, pra desligar a primeira função
function ocultarSpan(){
    span.style.opacity = "0"
}
button.addEventListener("mouseout", ocultarSpan);

//Evento de click no botão
function fazerUmClick(){
    section.innerText = "Fez um click simples!"
}
button.addEventListener("click", fazerUmClick);

//Evento de click duplo
function fazerDoisClicks(){
    section.innerText = "Fez um duplo click!"
}
button.addEventListener("dblclick", fazerDoisClicks);