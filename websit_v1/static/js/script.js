function toggleComment(link) {
    var commentsDiv = link.nextElementSibling;
    commentsDiv.style.display = commentsDiv.style.display === 'none' ? 'block' : 'none';
}

document.addEventListener("DOMContentLoaded", function() {
    var toggleLinks = document.getElementsByClassName("toggle-comment");
    for (var i = 0; i < toggleLinks.length; i++) {
        var commentsDiv = toggleLinks[i].nextElementSibling;
        commentsDiv.style.display = 'none';
    }
});





    function redirectToProfile() {
        window.location.href = "/profile";
    }

    function redirectToCreateAccount() {
        window.location.href = "/singup";
    }

    function redirectToLogout() {
        window.location.href = "/login";
    }


