let titulo = document.getElementById('titulo');
let lista = document.getElementById('lista-ordenada');
let link = document.getElementsById('link');
let listaCaos = document.getElementsById('listaCaos');

titulo.innerText = "título implementado via JS";
link.innerText = "PROS!JS!";

lista.innerHTML = `
    <li><a href="https://google.com></a></li>
    <li><a href="https://bing.com></a></li>
    <li><a href="https://you.com></a></li>
    
`

listaCaos.innerHTML = ` 
    <li>HTML 5;</li>
    <li>CSS 3;</li>
    <li>JS;</li>

`
