function loginModal(){
    let modal = new bootstrap.Modal(document.getElementById('modal_login'))
    modal.show()
}


function validateRegister(){
    let myUsername = document.getElementsByName('username');
    // const user = document.getElementById("user_name").value
    // let email = document.getElementByName("user_email")
    // let passwd = document.getElementByName("user_passwd")
    // let rpt_passwd = document.getElementByName("user_rpt_passwd")
    console.log(myUsername[0]);
}

// $('#register_form').on('load', function() {
//     const inputValue = $('#user_name').val();
//     console.log(inputValue)
// });