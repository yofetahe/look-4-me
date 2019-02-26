
function view_signup_form(){
    document.getElementById('signup_form').style.display = 'block'
    document.getElementById('login_form').style.display = 'none'
    document.getElementById('signup').className = 'active'
    document.getElementById('login').className = ''
}

function view_login_form(){
    document.getElementById('signup_form').style.display = 'none'
    document.getElementById('login_form').style.display = 'block'
    document.getElementById('signup').className = ''
    document.getElementById('login').className = 'active'
}

