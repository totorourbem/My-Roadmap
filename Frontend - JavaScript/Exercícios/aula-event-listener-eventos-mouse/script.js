//Variáveis e dados

let subtotalInfo = {
  quantidade: 1,
  valor: 11.66,
};

let qtdadeSubtotal = document.getElementById("quantidade-subtotal");
let valorSubtotal = document.getElementById("valor-subtotal");
let botaoAdicionar = document.getElementById('btn-adicionar-produto-01');
let botaoSubtrair = document.getElementById('btn-subtrair-produto-01');
let qtdproduto01 = document.querySewlector('quantidade-produto-01');

qtdadeSubtotal.innerText = subtotalInfo.quantidade + " itens";
valorSubtotal.innerText = subtotalInfo.valor;

//Funções de incrementar e decemtar item do carrinho

botaoAdicionar.addEventListener('click', function () {
  qtdproduto01.value = Number(qtdproduto01.value) + 1;
  qtdadeSubtotal.innerText = qtdproduto01.value + " itens";
  valorSubtotal.innerText = (subtotalInfo.valor * qtdproduto01.value).toFixed(2);
})

botaoSubtrair.addEventListener('click', function () {
  qtdproduto01.value = Number(qtdproduto01.value) - 1;
  qtdadeSubtotal.innerText = qtdproduto01.value + " itens";
  valorSubtotal.innerText = (subtotalInfo.valor * qtdproduto01.value).toFixed(2);
})
