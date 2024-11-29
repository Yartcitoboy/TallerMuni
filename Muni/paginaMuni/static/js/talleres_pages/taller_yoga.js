function mostrarInscripcion() {
    const card = document.getElementById('cardInscripcion');
    card.classList.remove('ocultar');
    card.classList.add('mostrar');
}

function cerrarInscripcion() {
    const card = document.getElementById('cardInscripcion');
    card.classList.remove('mostrar');
    card.classList.add('ocultar');
}