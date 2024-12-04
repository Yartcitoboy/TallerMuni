// Input field effects
document.querySelectorAll('.form input, .form textarea').forEach((input) => {
    input.addEventListener('keyup', (e) => {
      const label = input.previousElementSibling;
      if (e.target.value === '') {
        label.classList.remove('active', 'highlight');
      } else {
        label.classList.add('active', 'highlight');
      }
    });
  
    input.addEventListener('blur', (e) => {
      const label = input.previousElementSibling;
      if (e.target.value === '') {
        label.classList.remove('active', 'highlight');
      } else {
        label.classList.remove('highlight');
      }
    });
  
    input.addEventListener('focus', (e) => {
      const label = input.previousElementSibling;
      if (e.target.value === '') {
        label.classList.remove('highlight');
      } else {
        label.classList.add('highlight');
      }
    });
  });
  
  // Tab switching
  document.querySelectorAll('.tab a').forEach((tabLink) => {
    tabLink.addEventListener('click', (e) => {
      e.preventDefault();
  
      const parentTab = tabLink.parentElement;
      parentTab.classList.add('active');
      Array.from(parentTab.parentElement.children)
        .filter((li) => li !== parentTab)
        .forEach((sibling) => sibling.classList.remove('active'));
  
      const targetId = tabLink.getAttribute('href').substring(1);
      document.querySelectorAll('.tab-content > div').forEach((content) => {
        if (content.id === targetId) {
          content.style.display = 'block';
        } else {
          content.style.display = 'none';
        }
      });
    });
  });


// Validaciones y animaciones
document.querySelectorAll('.form input').forEach((input) => {
  const icon = input.nextElementSibling; // Cambiar para obtener el icono después del input

  input.addEventListener('input', (e) => {
    const label = input.previousElementSibling;
    const value = e.target.value;

    // Validaciones específicas por campo
    
      if (input.id === 'nombre' || input.id === 'apellido1' || input.id === 'apellido2' && value.length < 3) {
        input.classList.add('invalid');
        input.classList.remove('valid');
        icon.classList.add('invalid');
        icon.classList.remove('valid');
        icon.style.display = 'inline-block';
      } else {
        input.classList.remove('invalid');
        input.classList.add('valid');
        icon.classList.remove('invalid');
        icon.classList.add('valid');
        icon.style.display = 'inline-block';
      }
      
      if (input.id === 'telefono' && value.length < 8) {
        input.classList.add('invalid');
        input.classList.remove('valid');
        icon.classList.add('invalid');
        icon.classList.remove('valid');
        icon.style.display = 'inline-block';
      } else {
        input.classList.remove('invalid');
        input.classList.add('valid');
        icon.classList.remove('invalid');
        icon.classList.add('valid');
        icon.style.display = 'inline-block';
      }
    

    if (input.id === 'email') {
      const emailPattern = /^[^\s@]+@[^\s@]+\.(com|cl)$/; // Validación de correo
      if (!emailPattern.test(value)) {
        input.classList.add('invalid');
        input.classList.remove('valid');
        icon.classList.add('invalid');
        icon.classList.remove('valid');
        icon.style.display = 'inline-block';
      } else {
        input.classList.remove('invalid');
        input.classList.add('valid');
        icon.classList.remove('invalid');
        icon.classList.add('valid');
        icon.style.display = 'inline-block';
      }
    }

    // Animación de la etiqueta
    if (value === '') {
      label.classList.remove('active', 'highlight');
      icon.style.display = 'none'; 
    } else {
      label.classList.add('active', 'highlight');
    }
  });
});

document.getElementById('nombre').addEventListener('input', function (e) {
  this.value = this.value.replace(/[^a-zA-ZáéíóúÁÉÍÓÚñÑ\s]/g, ''); 
});
document.getElementById('apellido1').addEventListener('input', function (e) {
  this.value = this.value.replace(/[^a-zA-ZáéíóúÁÉÍÓÚñÑ\s]/g, ''); 
});
document.getElementById('apellido2').addEventListener('input', function (e) {
  this.value = this.value.replace(/[^a-zA-ZáéíóúÁÉÍÓÚñÑ\s]/g, ''); 
});

document.getElementById('telefono').addEventListener('input', function (e) {
  this.value = this.value.replace(/\D/g, ''); 
});
