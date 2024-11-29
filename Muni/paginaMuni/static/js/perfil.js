let isEditing = false;

function cambiarImagen(event) {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function (e) {
            const imagen = document.getElementById('user-image');
            imagen.src = e.target.result;
        };
        reader.readAsDataURL(file);
    }
}

function editarPerfil() {
    const camposEditables = ['nombre', 'email', 'celular', 'direccion',];
    const boton = document.querySelector('.editar-perfil');
    let valid = true; // Bandera para la validación

    camposEditables.forEach((campoId) => {
        const elemento = document.getElementById(campoId);

        if (isEditing) { 
            const input = elemento.querySelector('input');
            if (input) {
                if (input.value.trim() === '') {
                    alert(`El campo ${campoId} no puede estar vacío.`);
                    valid = false;
                } else {
                    elemento.textContent = input.value; 
                }
            }
        } else {

            const valorActual = elemento.textContent;
            elemento.innerHTML = `<input type="text" value="${valorActual}" style="width: 100%;">`;
        }
    });


    if (isEditing && !valid) {
        return;
    }

    // Cambiar texto del botón
    boton.textContent = isEditing ? 'Editar Perfil' : 'Guardar Cambios';
    isEditing = !isEditing;
}
