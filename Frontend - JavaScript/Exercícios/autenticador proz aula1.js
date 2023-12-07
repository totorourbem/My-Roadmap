// Crte duas variáveis, uma que guarde a senha do usuário, 
// outra que verifica se ele tem permissões de administrador

// Crie duas estruturas ccondicionais
//A primeira deve imprimir "Insira sua nova senha"
//CASO O USERNAME E A SENHA ESTEJAM CORRETOS
// e imprimir "Usuário/senha incorretos" caso 
// qualuqwer um dos dois esteja errado

// A segunda estrutra condicional deve imprimir  
// "Você não pode acessar essa área do sistema"
// caso o user não tenha permissoes e 
// "Bem-vindo á area de adminikstração" se sim

let password = "Creitin";
const administrador = false;

if (password == "Creitin") {
  console.log("Insira sua nova senha")
} else {
  console.log("Usuário/senha incorretos")
}

if (administrador) {
  console.log('"Bem-vindo á area de administração"')
} else {
  console.log("Você não pode acessar essa área do sistema")
}