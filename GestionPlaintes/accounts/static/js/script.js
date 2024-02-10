
// Click button Se connecter et S'inscrire
var a = document.getElementById("loginBtn");
var b = document.getElementById("registerBtn");
var x = document.getElementById("login");
var y = document.getElementById("register");

function login() {
    x.style.left = "4px";
    y.style.right = "-520px";

    a.className += " white-btn";
    b.className = "btn";

    x.style.opacity = 1;
    y.style.opacity = 0;
}

function register() {
    x.style.left = "-510px";
    y.style.right = "5px";

    a.className = "btn";
    b.className += " white-btn";

    x.style.opacity = 0;
    y.style.opacity = 1;
}

function myMenuFunction() {
    var i = document.getElementById("navMenu");

    if (i.className === "nav-menu") {
        i.className += " responsive";
    }
    else {
        i.className = "nav-menu";
    }
}

// Condition lorsque l'utilisateur s'inscrit
document.addEventListener('DOMContentLoaded', function () {
    var inscriptionBtn = document.getElementById('inscription');
    var nameField = document.getElementById('name');
    var surnameField = document.getElementById('surname');
    var emailField = document.getElementById('email-inscrip');
    var passwordField = document.getElementById('password-inscrip');
    var image = document.getElementById('image');

    inscriptionBtn.addEventListener('click', function () {
    // vers index.php
    });

    nameField.addEventListener('input', function () {
        nameField.classList.remove('error');
    });

    surnameField.addEventListener('input', function () {
        surnameField.classList.remove('error');
    });

    emailField.addEventListener('input', function () {
        emailField.classList.remove('error');
    });

    passwordField.addEventListener('input', function () {
        passwordField.classList.remove('error');
    });
    image.addEventListener('input', function () {
        nameField.classList.remove('error');
    });
});

// Condition lorsque l'utilisateur se connecter
document.addEventListener('DOMContentLoaded', function () {
    var connexionBtn = document.getElementById('connexion');
    var email = document.getElementById('email');
    var password = document.getElementById('password');

    connexionBtn.addEventListener('click', function () {
        if (email.value.trim() === '') {
            email.classList.add('error');
            toastr.error('L\'adresse émail ne doit pas être vide !', '', {
                positionClass: 'toast-top-center'
            });
            return;
        } else {
            email.classList.remove('error');
        }

        if (password.value.trim() === '') {
            password.classList.add('error');
            toastr.error('Le mot de passe ne doit pas être vide !', '', {
                positionClass: 'toast-top-center'
            });
            return;
        } else {
            password.classList.remove('error');
        }

    });

    email.addEventListener('input', function () {
        email.classList.remove('error');
    });

    password.addEventListener('input', function () {
        password.classList.remove('error');
    });
});

// Condition sur la vérification de la saisie du nom
document.addEventListener('DOMContentLoaded', function () {
    var inscriptionBtn = document.getElementById('inscription');
    var nameField = document.getElementById('name');
    var surnameField = document.getElementById('surname');
    var emailField = document.getElementById('email-inscrip');
    var passwordField = document.getElementById('password-inscrip');

    inscriptionBtn.addEventListener('click', function () {
    //    Vers index.php

    });

    nameField.addEventListener('input', function () {
        nameField.classList.remove('is-invalid');
    });

    surnameField.addEventListener('input', function () {
        surnameField.classList.remove('is-invalid');
    });

    emailField.addEventListener('input', function () {
        emailField.classList.remove('is-invalid');
    });

    passwordField.addEventListener('input', function () {
        passwordField.classList.remove('is-invalid');
    });
});