$('#registro').validate({ 
    "rules": {
        "rut": {
            required: true,
        },
        "username": {
            required: true,
        },
        "email": {
            required: true,
            email: true,
        },
        "password": {
            required: true,
            minlength : 10,
        },
        "password2": {
            required: true,
            minlength : 10,
            equalTo : "#password",
        },
    },
    messages: {
        "rut": {
            required: 'Debe ingresar un RUT',
        },
        "username": {
            required: 'Debe ingresar un nombre de usuario',
        },
        "email": {
            required: 'Debe ingresar su correo electrónico',
            email: 'Formato de correo incorrecto'
        },
        "password": {
            required: 'Debe ingresar una password',
            minlength: 'La mínima cantidad de caracteres de la contraseña es 10',
        },
        "password2": {
            required: 'Debe repetir la misma password',
            minlength: 'La mínima cantidad de caracteres de la contraseña es 10',
            equalTo: 'La repetición de contraseña debe coincidir con la contraseña original',
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

function validarRut(rut) {
    if (rut.length < 8) return false;
  
    var caracteres = /^(\d{1,3}(\.?\d{3})*)\-?([\dkK])$/i;
    if (!caracteres.test(rut)) return false;
  
    rut = rut.replace(/\./g, '');
    var dv = rut.slice(-1).toUpperCase();
    var cuerpo = rut.slice(0, -1);
  
    var suma = 0;
    var multiplo = 2;
    for (var i = cuerpo.length - 1; i >= 0; i--) {
      suma += parseInt(cuerpo.charAt(i)) * multiplo;
      if (multiplo < 7) multiplo += 1;
      else multiplo = 2;
    }
  
    var resultado = 11 - (suma % 11);
    if (resultado == 11) dv = '0';
    else if (resultado == 10) dv = 'K';
    else dv = resultado.toString();
  
    return dv === dv;
  }
  
  $(document).ready(function() {
    $('#id_rut').on('input', function() {
      var rut = $(this).val();
      var resultado = $('#resultado');
      if (validarRut(rut)) {
        resultado.text('El RUT es válido.');
      } else {
        resultado.text('El RUT es inválido.');
      }
    });
  });
  

$("#id_rut").rules("add", { rut: true });
$("#id_email").rules("add", { validateemail: true });


