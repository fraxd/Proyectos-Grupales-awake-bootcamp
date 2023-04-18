a = JSON.parse(localStorage.getItem('molestia'))
window.addEventListener('load', function () {
    if(a==false)
    window.location.href='anexos/login.html';
})