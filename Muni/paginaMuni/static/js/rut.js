document.addEventListener("DOMContentLoaded", function () {
    const runInput = document.getElementById("rut");
    const icon = document.getElementById("rut-icon"); // Obtener el ícono de validación

    // Evento para procesar el RUT mientras se escribe
    runInput.addEventListener("input", function () {
        let value = this.value.replace(/[^0-9kK]/g, ""); // Eliminar caracteres no permitidos
        if (value.includes("-")) {
            value = value.split("-")[0]; // Solo tomar la parte numérica antes del guion
        }
        if (value.length >= 7) {
            value = value.slice(0, 8); // Limitar a 8 dígitos numéricos
        }
        this.value = value; // Actualizar el campo con el valor limpio

        // Validación del RUT
        if (value.length < 7) {
            icon.classList.add('invalid'); // Mostrar icono de error
            icon.classList.remove('valid');
            icon.style.display = 'inline-block'; // Mostrar icono de error
        } else {
            icon.classList.remove('invalid');
            icon.classList.add('valid'); // Mostrar icono de éxito
            icon.style.display = 'inline-block'; // Mostrar icono de éxito
        }
    });

    // Evento para calcular el DV al perder el foco
    runInput.addEventListener("blur", function () {
        let value = this.value.replace(/[^0-9]/g, ""); // Eliminar caracteres no numéricos
        if (value.length >= 7) {
            const dv = calcularDV(value); // Calcular dígito verificador
            this.value = `${value}-${dv}`; // Asignar el RUT con DV al campo
        } else {
            this.value = value; // Si no hay 7 dígitos, no agregar DV
        }
    });

    // Función para calcular el dígito verificador
    function calcularDV(rut) {
        let suma = 0;
        let multiplicador = 2;
        for (let i = rut.length - 1; i >= 0; i--) {
            suma += parseInt(rut[i], 10) * multiplicador;
            multiplicador = multiplicador === 7 ? 2 : multiplicador + 1;
        }
        const resto = 11 - (suma % 11);
        if (resto === 11) {
            return '0';
        } else if (resto === 10) {
            return 'K';
        } else {
            return resto.toString();
        }
    }
});