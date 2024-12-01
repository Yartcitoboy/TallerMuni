document.getElementById("taller").addEventListener("change", function () {
  const selectedOption = this.options[this.selectedIndex];
  const tallerInfo = JSON.parse(selectedOption.getAttribute("data-info"));

  if (tallerInfo) {
    document.getElementById("taller-nombre").textContent = tallerInfo.nombre;
    document.getElementById("taller-descripcion").textContent = tallerInfo.descripcion;
    document.getElementById("taller-duracion").textContent = tallerInfo.duracion;
    document.getElementById("taller-instructor").textContent = tallerInfo.instructor;

    document.getElementById("taller-info").style.display = "block";
  }
});
