var suggestionButtons = document.querySelectorAll('.suggestion-button');
suggestionButtons.forEach(function(button) {
    button.addEventListener('click', function() {
        var suggestionText = button.dataset.suggestionText;
        var textarea = document.querySelector('#description');
        textarea.value = suggestionText;
    });
});