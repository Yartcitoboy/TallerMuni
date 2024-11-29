const data = [
    {
        title: "Jumping - Fitness 2024",
        date: "Ma / Ju (11:00-12:00)",
        location: "Juanita Oriente 915, Puente Alto, Chile",
        available: false,
        type: "Gratuita",
        image: "../img/CUECA.jpg",
        URL:"../views/yoga.html"
    },
    {
        title: "Baile Adulto Mayor 2024 - Renacer de Llaverías",
        date: "Ju (16:00-17:00)",
        location: "On Panta 367, Puente Alto, Chile",
        available: true,
        type: "Gratuita",
        image: "https://via.placeholder.com/300",
        
        
    },
    {
        title: "Capoeira 2024 - Centro de Extensión Don Ramón",
        date: "Ma / Ju (19:30-21:00)",
        location: "Luis Matte Larraín 2472, Puente Alto, Chile",
        available: false,
        type: "Gratuita",
        image: "https://via.placeholder.com/300"
    },
    {
        title: "Yoga 2024 - Sede Papelera",
        date: "Ma (18:30-19:30)",
        location: "Calle Central 217, Puente Alto, Chile",
        available: true,
        type: "Gratuita",
        image: "https://via.placeholder.com/300"
    },
    {
        title: "Yoga 2024 - Sede Papelera",
        date: "Ma (18:30-19:30)",
        location: "Calle Central 217, Puente Alto, Chile",
        available: true,
        type: "Gratuita",
        image: "https://via.placeholder.com/300"
    },
    {
        title: "Yoga 2024 - Sede Papelera",
        date: "Ma (18:30-19:30)",
        location: "Calle Central 217, Puente Alto, Chile",
        available: true,
        type: "Gratuita",
        image: "https://via.placeholder.com/300"
    },
    {
        title: "Yoga 2024 - Sede Papelera",
        date: "Ma (18:30-19:30)",
        location: "Calle Central 217, Puente Alto, Chile",
        available: true,
        type: "Gratuita",
        image: "https://via.placeholder.com/300"
    },
    {
        title: "Yoga 2024 - Sede Papelera",
        date: "Ma (18:30-19:30)",
        location: "Calle Central 217, Puente Alto, Chile",
        available: true,
        type: "Gratuita",
        image: "https://via.placeholder.com/300"
    },
    {
        title: "Yoga 2024 - Sede Papelera",
        date: "Ma (18:30-19:30)",
        location: "Calle Central 217, Puente Alto, Chile",
        available: true,
        type: "Gratuita",
        image: "https://via.placeholder.com/300"
    },
    {
        title: "Yoga 2024 - Sede Papelera",
        date: "Ma (18:30-19:30)",
        location: "Calle Central 217, Puente Alto, Chile",
        available: true,
        type: "Gratuita",
        image: "https://via.placeholder.com/300"
    }
];

document.addEventListener("DOMContentLoaded", renderCards);


function renderCards() {
    const container = document.getElementById("cards-container");
    container.innerHTML = "";

    data.forEach((item) => {
        const card = document.createElement("div");
        card.classList.add("card");

        card.innerHTML = `
            <img src="${item.image}" alt="${item.title}">
            <div class="card-content">
                <h3 class="card-title">${item.title}</h3>
                <p class="card-info">${item.date}</p>
                <p class="card-info">${item.location}</p>
                <div class="cta">
                    <span>${item.type}</span>
                    <span>${item.available ? "Disponible" : "Sin cupos"}</span>
                </div>
            </div>
        `;

        container.appendChild(card);
    });
}
document.addEventListener("DOMContentLoaded", renderCards);
