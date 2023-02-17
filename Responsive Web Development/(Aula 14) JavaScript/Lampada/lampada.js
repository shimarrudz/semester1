//Mais uma forma de pegar o elemento HTML 
let ligar = document.getElementById("ligar");
let lampada = document.getElementById("lampada");

//Evento click com botão
ligar.addEventListener("click", ligarLampada);
desligar.addEventListener("click", desligarLampada);

//Evento double click
lampada.addEventListener("dblclick", quebrarLampada);

//função para ligar a lampada(alterar a imagem)
function ligarLampada () {
    lampada.src = "img/ligada.jpg";
}

// Função para desligar a lampada 
function desligarLampada () {
    lampada.src = "img/desligada.jpg"
}

//função lampada quebrada
function quebrarLampada () {
    lampada.src = "img/quebrada.jpg"
}

//Evento do mouse por cima da função
lampada.addEventListener("mouseover", ligarLampada);
lampada.addEventListener("mouseleave", desligarLampada)
