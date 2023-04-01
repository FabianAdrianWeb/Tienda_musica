$('#contacto_validate').validate({ 
    "rules": {
        "nombre": {
            required: true,
        },
        "email": {
            required: true,
            email: true,
        },
        "mensaje": {
            required: true,
            minlength : 10,
        },
    },
    messages: {
        "nombre": {
            required: 'Debe ingresar su nombre',
        },
        "email": {
            required: 'Debe ingresar su correo electrónico',
            email: 'Formato de correo incorrecto'
        },
        "mensaje": {
            required: 'Debe ingresar un mensaje',
            minlength: 'La mínima cantidad de caracteres del mensaje es 10',
        },
    }
});

function validateEmail(email) {
    var re = /\S+@\S+\.\S+/;
    return re.test(email);
}

$.validator.addMethod(
    "validateemail",
    function(value, element, validate) {
        debugger
        if (validate) {
            return validateEmail(value);
        }
    },
    "Formato de correo incorrecto"
);


$("#email").rules("add", { validateemail: true });

