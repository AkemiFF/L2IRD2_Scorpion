const rechercheBar = document.querySelector(".users .recherche input"),
    rechercheBtn = document.querySelector(".users .recherche button"),
    usersList = document.querySelector(".users .users-list");


rechercheBtn.onclick = () => {
    rechercheBar.classList.toggle("active");
    rechercheBar.focus();
    rechercheBtn.classList.toggle("active");
    rechercheBar.value = "";
}


document.addEventListener('DOMContentLoaded', function () {
    $.ajax({
        type: 'GET',
        url: '../php/view_user.php',
        dataType: 'json',
        success: function (userDetails) {
            if (userDetails.error) {
                window.location.href = 'index.php';
            } else {
                document.querySelector('.nav-logo p').innerText = userDetails.name; 
            }
        },
        error: function (error) {
            console.error(error);
        }
    });
});
