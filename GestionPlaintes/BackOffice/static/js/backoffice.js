function openModal(modalId) {
    var modal = document.getElementById(modalId);
    modal.style.display = "block";
}

function closeModal(modalId) {
    var modal = document.getElementById(modalId);
    modal.style.display = "none";
}

function confirmCloseTicket() {
    closeModal('close-ticket-confirmation-modal');
}

// Button next et prev
// Définir une variable pour garder une trace de la page actuelle
let currentPage = 1;
// Définir le nombre de lignes par page
const rowsPerPage = 5;

// Cette fonction affiche les tickets pour la page spécifiée
function displayTickets(page) {
    const startIndex = (page - 1) * rowsPerPage;
    const endIndex = startIndex + rowsPerPage;
    const tickets = document.querySelectorAll('#ticket-table tbody tr');

    tickets.forEach((ticket, index) => {
        if (index >= startIndex && index < endIndex) {
            ticket.style.display = 'table-row';
        } else {
            ticket.style.display = 'none';
        }
    });
}

// Cette fonction affiche la page précédente
function prevPage() {
    if (currentPage > 1) {
        currentPage--;
        displayTickets(currentPage);
    }
}

// Cette fonction affiche la page suivante
function nextPage() {
    const tickets = document.querySelectorAll('#ticket-table tbody tr').length;
    const totalPages = Math.ceil(tickets / rowsPerPage);
    if (currentPage < totalPages) {
        currentPage++;
        displayTickets(currentPage);
    }
}

// Appeler la fonction pour afficher les tickets de la première page au chargement de la page
displayTickets(currentPage);
