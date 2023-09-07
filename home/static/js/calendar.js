
document.addEventListener('DOMContentLoaded', function() {
    var calendarEl = document.getElementById('calendar');
    var calendar = new FullCalendar.Calendar(calendarEl, {
        // Configuración del calendario
        initialView: 'dayGridMonth', // Cambia la vista inicial si lo deseas
        events: [
            // Aquí puedes cargar tus eventos desde Django o una API externa
            {
                title: 'Evento 1',
                start: '2023-07-10',
                end: '2023-07-11'
            },
            // Agrega más eventos aquí
        ]
    });
    calendar.render();
});


function updateClock() {
    var now = new Date();
    var hours = now.getHours();
    var minutes = now.getMinutes();
    var seconds = now.getSeconds();
    
    // Formatea los valores para que tengan 2 dígitos
    hours = hours < 10 ? '0' + hours : hours;
    minutes = minutes < 10 ? '0' + minutes : minutes;
    seconds = seconds < 10 ? '0' + seconds : seconds;
    
    var timeString = hours + ':' + minutes + ':' + seconds;
    document.getElementById('clock').textContent = timeString;
}
// Actualiza el reloj cada segundo
setInterval(updateClock, 1000);
