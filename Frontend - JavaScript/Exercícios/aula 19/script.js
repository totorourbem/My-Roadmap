document.addEventListener("DOMContentLoaded", function() {
    // variáveis
    const linkPerfil = document.getElementById("link-perfil");
    const navPerfil = document.getElementById("nav-perfil");
    const linkPerfilDados = document.getElementById("link-perfil-dados"); 
    const logout = document.getElementById("logout");

    //exibir barra de navegação secundária
    linkPerfil.addEventListener("mouseover", () => {
        navPerfil.style.display = "block"
    })

    //navegação via teclado numérico

    document.addEventListener("keyup", (e)=> {

        if (navPerfil.style.display === "block") {
            if (e.key == "1") {
                linkPerfilDados.click()
            }
            else if (e.key == "2") {
                logout.click()
            }
        } else if (e.key == "1") {
            navPerfil.style.display = "block"
        }
        else if (e.key == "escape") {
            navPerfil.style.display = "none"
        }
    })
});