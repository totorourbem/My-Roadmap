document.addEventListener("DOMContentLoaded", function() {

    // FUNÇOES GERAIS
    //popup de campo obrigatório - as vezes é necessário desativar o autiocoplete dos campos para funcionar
    function togglePopup (input, label) {
        //ocultar popup de campo obrigatório
        input.addEventListener("focus", () => {
            label.classList.add("required-popup");
        });
        //ocultar popup de campo obrigatório
        input.addEventListener("blur", () => {
            label.classList.remove("required-popup");
        });    
    };

    function estilizarInputCorreto(input, helper) {
        helper.classList.remove("visible");
        input.classList.remove("error");
        input.classList.add("correct");
    }

    function estilizarInputIncorreto(input, helper) {
        helper.classList.add("visible");
        input.classList.add("error");
        input.classList.remove("correct");
    }
    //VALIDAÇÃO USERNAME
    // Variáveis
    let usernameInput = document.getElementById("username");
    let usernameLabel = document.querySelector('label[for="username"]');
    let usernameHelper = document.getElementById("username-helper");

    togglePopup(usernameInput, usernameLabel);

    //validar valor dos input
    usernameInput.addEventListener("change", function(e){
        let valor = e.target.value
        if (valor.length < 5) {
            usernameHelper.innerText = "O username precisa ter 5 ou mais caracteres"
            estilizarInputIncorreto(usernameInput, usernameHelper)
            inputsCorretos.username = false
        } else{
            estilizarInputCorreto(usernameInput, usernameHelper)
            inputsCorretos.username = true
        }
    });

    //VALIDAÇÃO EMAIL
    // Variáveis
    let emailInput = document.getElementById("email");
    let emailLabel = document.querySelector('label[for="email"]');
    let emailHelper = document.getElementById("email-helper");
    
    togglePopup(emailInput, emailLabel);    
    
    //validar valores dos input
    emailInput.addEventListener("change", function(e){
        let valor = e.target.value
        if(valor.includes("@") && valor.includes(".com")) {
            estilizarInputCorreto(emailInput, emailHelper)
            inputsCorretos.email = true
        }else {
            emailHelper.innerText = "Por favor, insira um e-mail válido."
            estilizarInputIncorreto(emailInput, emailHelper)
            inputsCorretos.email = false
        }

    });
    
    //VALIDAÇÃO SENHA
    // Variáveis
    let senhaInput = document.getElementById("senha");
    let senhaLabel = document.querySelector('label[for="senha"]');
    let senhaHelper = document.getElementById("senha-helper"); 
    
    togglePopup(senhaInput, senhaLabel);

    //validar valores dos input
    senhaInput.addEventListener("blur", function(e){
        let valor = e.target.value
        if (valor==="") {
            senhaHelper.innerText = "O campo senha não pode estar vazio."
            estilizarInputIncorreto(senhaInput, senhaHelper)
            inputsCorretos.senha = false
        } else{
            estilizarInputCorreto(senhaInput, senhaHelper)
            inputsCorretos.senha = true
        }
    });

    //VALIDAÇÃO CONFIRMA-SENHA
    // Variáveis
    let confirmaSenhaInput = document.getElementById("confirma-senha");
    let confirmaSenhaLabel = document.querySelector('label[for="confirma-senha"]');
    let confirmaSenhaHelper = document.getElementById("confirma-senha-helper"); 
    
    togglePopup(confirmaSenhaInput, confirmaSenhaLabel);

    //validar valores dos input
    confirmaSenhaInput.addEventListener("change", function(e){
        let confirmaSenhaValor = e.target.value
        if (confirmaSenhaValor === senhaInput.value) {
            estilizarInputCorreto(confirmaSenhaInput, confirmaSenhaHelper);
            inputsCorretos.confirmaSenha = true
        } else{
            confirmaSenhaHelper.innerText = "O campo confirmar senha deve ser identico ao campo senha."
            estilizarInputIncorreto(confirmaSenhaInput, confirmaSenhaHelper);
            inputsCorretos.confirmaSenha = false
        }
    });

    //CONTROLE DE ENVIO DE FORMULÁRIO

    let btnSubmit = document.querySelector("button[type='submit']");
    let inputsCorretos = {
        username: false,
        email: false,
        senha: false,
        confirmaSenha: false
    }

    btnSubmit.addEventListener("click", (e)=>{
        if(inputsCorretos.username == false || inputsCorretos.email == false || inputsCorretos.senha == false || inputsCorretos.confirmaSenha == false){
            e.preventDefault()
            alert("Os campos obrigatórios precisam ser preenchidos corretamente!")
        }else{
            alert("Formulário enviado com sucesso!")
        }
    })

})