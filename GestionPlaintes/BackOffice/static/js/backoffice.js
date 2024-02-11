// CODE JS POUR BACKOFFICE
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
let currentPage = 1;
const rowsPerPage = 5;

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

function prevPage() {
    if (currentPage > 1) {
        currentPage--;
        displayTickets(currentPage);
    }
}

function nextPage() {
    const tickets = document.querySelectorAll('#ticket-table tbody tr').length;
    const totalPages = Math.ceil(tickets / rowsPerPage);
    if (currentPage < totalPages) {
        currentPage++;
        displayTickets(currentPage);
    }
}

displayTickets(currentPage);
