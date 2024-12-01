// static/js/taller.js

document.getElementById('taller').addEventListener('change', function() {
  var selectedOption = this.options[this.selectedIndex];
  var tallerInfo = JSON.parse(selectedOption.getAttribute('data-info'));
  
  document.getElementById('taller-nombre').textContent = tallerInfo.nombre;
  document.getElementById('taller-instructor').textContent = tallerInfo.instructor;
  document.getElementById('taller-descripcion').textContent = tallerInfo.descripcion;
  document.getElementById('taller-duracion').textContent = tallerInfo.duracion;
});
