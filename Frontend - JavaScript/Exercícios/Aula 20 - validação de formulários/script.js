document.addEventListener("DOMContentLoaded", function() {

    // FUNÇOES GENÉRICAS
    //popup de campo obrigatório - as vezes é necessário desativar o autiocoplete dos campos para funcionar
    function popupCampo (input, label) {
        //ocultar popup de campo obrigatório
        input.addEventListener("focus", () => {
            label.classList.add("required-popup");
        });
        //ocultar popup de campo obrigatório
        input.addEventListener("blur", () => {
            label.classList.remove("required-popup");
        });    
    };

    //VALIDAÇÃO USERNAME
    // Variáveis
    let usernameInput = document.getElementById("username");
    let usernameLabel = document.querySelector('label[for="username"]');
    let usernameHelper = document.getElementById("username-helper");

    popupCampo(usernameInput, usernameLabel);

    //validar valor dos input
    usernameInput.addEventListener("change", function(e){
        let valor = e.target.value
        if (valor.length < 5) {
            usernameInput.classList.remove("correct")
            usernameInput.classList.add("error")
            usernameHelper.innerText = "O username precisa ter 5 ou mais caracteres"
            usernameHelper.classList.add("visible")
        } else{
            usernameInput.classList.remove("error")
            usernameInput.classList.add("correct")
            usernameHelper.classList.remove("visible")
        }
    });

    //VALIDAÇÃO EMAIL
    // Variáveis
    let emailInput = document.getElementById("email");
    let emailLabel = document.querySelector('label[for="email"]');
    let emailHelper = document.getElementById("email-helper");
    
    popupCampo(emailInput, emailLabel);    
    
    //validar valores dos input
    emailInput.addEventListener("change", function(e){
        let valor = e.target.value
        if(valor.includes("@") && valor.includes(".com")) {
            emailInput.classList.remove("error")
            emailInput.classList.add("correct")
            emailHelper.classList.remove("visible")
        }else {
            emailInput.classList.remove("correct")
            emailInput.classList.add("error")
            emailHelper.innerText = "Por fgavor, insira um e-mail válido."
            emailHelper.classList.add("visible")
        }

    }
    )})

