//DOM = Document Object Model

/*  SELECIONA UMA TAG (seleciona um h1, modificando apenas o primeiro) */
let titulo = document.querySelector("#titulo");

let subtitulo = document.querySelector("#subtitulo");

/* Mudei o texto do h1 */
titulo.textContent = "DOM";

/* Mudei o texto do h2 */
titulo.textContent = "Este é o subtítulo"

console.log(titulo,subtitulo);


let tela = document.querySelector("main");

let buttonDark = document.querySelector("#buttonDark");

let buttonLigth = document.querySelector("#buttonLigth")




buttonDark.addEventListener("click", modoDark);
buttonLigth.addEventListener("click", modoLigth);


function modoDark(){
    tela.classList.add("dark")
    tela.classList.remove("ligth")
}

function modoLigth(){
    tela.classList.add("ligth")
    tela.classList.remove("dark")
}