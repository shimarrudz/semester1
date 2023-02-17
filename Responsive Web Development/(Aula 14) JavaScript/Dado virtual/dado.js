//Selecionar elementos


let numSorteado = 0;
let imgDado = document.getElementbyId("imgDado");
let buttonSortear = document.querySelector("#buttonSortear");s
let sorteado = document.querySelector("#sorteado");

buttonSortear.addEventListener("click", sortear)

function sortear(){

    imgDado.classList.add("animar");
    sorteado.classList.add("aparecer");


    numSorteado = getRandomInt(1,6);
    console.log(numSorteado)
    imgDado.setAtribute("src","img/" + numSorteado + ".png" )
    imgDado.classList.remove("animar");


   
}
 //Função que gera número randomico inteiro
 //Incluindo o mínimo e o máximo
 function getRandomInt(min, max) {

    min = Math.ceil(min)  // arredonda para cima  ceil  = teto

    max = Math.floor(max) // arredonda para baixo floor = piso

    return Math.floor(Math.random() * (max - min + 1)) + min

}
 
