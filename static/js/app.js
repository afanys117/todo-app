document.addEventListener('DOMContentLoaded', function () {
    const deleteButtons = document.querySelectorAll('.delete-btn');
    
    deleteButtons.forEach(button => {
        button.addEventListener('click', function (event) {
            const confirmed = confirm('Are you sure you want to delete this task?');
            if (!confirmed) {
                event.preventDefault();
            }
        });
    });
});
