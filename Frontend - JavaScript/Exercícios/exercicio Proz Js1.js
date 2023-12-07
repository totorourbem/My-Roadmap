//escreva o código necessário para avaliar cada elemento do array e imprimir uma frase
// seguindo algum dos seguintes três modelos:

//- X é par e menor que 50
//- X é menor que 50
//- X é maior que 50

let numerosDaSorte = [37, 14, 26, 5, 94, 87]  

for (let i = 0; i < numerosDaSorte.length; i++) {
  if (numerosDaSorte[i] % 2 === 0 && numerosDaSorte[i] < 50) {
    console.log('O ' + (i+1) + '° numero, ' + numerosDaSorte[i] + ' é par e menor que 50!')
  }
  else if (numerosDaSorte[i] < 50) {
    console.log('O ' + (i+1)  + '° numero, ' + numerosDaSorte[i] + ' é menor que 50!')
  }
  else {
    console.log('O ' + (i+1) + '° numero, ' + numerosDaSorte[i] + ' é maior que 50!')
  }
} 