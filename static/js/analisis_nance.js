
    var pos = 0;
    var numtabla=1;

    $(document).ready(function(){  
//cambia los atributos con el checkbox, si esta clickeado se habilitan los campos de lo contrario los deshabilita
//y borra los datos


//-------------------------Tabla 1------------------------------------------     
        $("#id_1tablas-0-seleccion").click(function() {  
            if($(".checkbox").is(':checked')) {  
                $('#id_1tablas-0-mdm').attr('readonly', false);
                $('#id_1tablas-0-mprx').attr('readonly', false);
                $('#id_1tablas-0-mdrx').attr('readonly', false);
                $('#id_1tablas-0-mdm').attr('required', true);
                $('#id_1tablas-0-mprx').attr('required', true);
                $('#id_1tablas-0-mdrx').attr('required', true);

            } else {  
                //alert("No está activado"); 
    			$('#id_1tablas-0-mdm').attr('readonly', true);
                $('#id_1tablas-0-mprx').attr('readonly', true);
                $('#id_1tablas-0-mdrx').attr('readonly', true);	
                $('#id_1tablas-0-mdm').attr('required', false);
                $('#id_1tablas-0-mprx').attr('required', false);
                $('#id_1tablas-0-mdrx').attr('required', false);


                $('#id_1tablas-0-mdm').val("");
                $('#id_1tablas-0-mprx').val("");
                $('#id_1tablas-0-multiplicacion').val("");
                $('#id_1tablas-0-mdrx').val("");
                
            }  
        });
        $("#id_1tablas-1-seleccion").click(function() {  
            if($(".checkbox").is(':checked')) {  
                $('#id_1tablas-1-mdm').attr('readonly', false);
                $('#id_1tablas-1-mprx').attr('readonly', false);
                $('#id_1tablas-1-mdrx').attr('readonly', false);	
                $('#id_1tablas-1-mdm').attr('required', true);
                $('#id_1tablas-1-mprx').attr('required', true);
                $('#id_1tablas-1-mdrx').attr('required', true);    
            } else {  
                $('#id_1tablas-1-mdm').attr('readonly', true);
                $('#id_1tablas-1-mprx').attr('readonly', true);
                $('#id_1tablas-1-mdrx').attr('readonly', true);	
                $('#id_1tablas-1-mdm').attr('required', false);
                $('#id_1tablas-1-mprx').attr('required', false);
                $('#id_1tablas-1-mdrx').attr('required', false);

                $('#id_1tablas-1-mdm').val("");
                $('#id_1tablas-1-mprx').val("");
                $('#id_1tablas-1-multiplicacion').val("");
                $('#id_1tablas-1-mdrx').val("");    
            }  
        });
        $("#id_1tablas-2-seleccion").click(function() {  
            if($(".checkbox").is(':checked')) {  
                $('#id_1tablas-2-mdm').attr('readonly', false);
                $('#id_1tablas-2-mprx').attr('readonly', false);
                $('#id_1tablas-2-mdrx').attr('readonly', false);	
                $('#id_1tablas-2-mdm').attr('required', true);
                $('#id_1tablas-2-mprx').attr('required', true);
                $('#id_1tablas-2-mdrx').attr('required', true);    
            } else {  
                $('#id_1tablas-2-mdm').attr('readonly', true);
                $('#id_1tablas-2-mprx').attr('readonly', true);
                $('#id_1tablas-2-mdrx').attr('readonly', true);	
                $('#id_1tablas-2-mdm').attr('required', false);
                $('#id_1tablas-2-mprx').attr('required', false);
                $('#id_1tablas-2-mdrx').attr('required', false); 

                $('#id_1tablas-2-mdm').val("");
                $('#id_1tablas-2-mprx').val("");
                $('#id_1tablas-2-multiplicacion').val("");
                $('#id_1tablas-2-mdrx').val("");
            }  
        });
        $("#id_1tablas-3-seleccion").click(function() {  
            if($(".checkbox").is(':checked')) {  
                $('#id_1tablas-3-mdm').attr('readonly', false);
                $('#id_1tablas-3-mprx').attr('readonly', false);
                $('#id_1tablas-3-mdrx').attr('readonly', false);	
                $('#id_1tablas-3-mdm').attr('required', true);
                $('#id_1tablas-3-mprx').attr('required', true);
                $('#id_1tablas-3-mdrx').attr('required', true);    
            } else {  
                $('#id_1tablas-3-mdm').attr('readonly', true);
                $('#id_1tablas-3-mprx').attr('readonly', true);
                $('#id_1tablas-3-mdrx').attr('readonly', true);	
                $('#id_1tablas-3-mdm').attr('required', false);
                $('#id_1tablas-3-mprx').attr('required', false);
                $('#id_1tablas-3-mdrx').attr('required', false);  

                $('#id_1tablas-3-mdm').val("");
                $('#id_1tablas-3-mprx').val("");
                $('#id_1tablas-3-multiplicacion').val("");
                $('#id_1tablas-3-mdrx').val("");  
            }  
        });
        $("#id_1tablas-4-seleccion").click(function() {  
            if($(".checkbox").is(':checked')) {  
                $('#id_1tablas-4-mdm').attr('readonly', false);
                $('#id_1tablas-4-mprx').attr('readonly', false);
                $('#id_1tablas-4-mdrx').attr('readonly', false);	
                $('#id_1tablas-4-mdm').attr('required', true);
                $('#id_1tablas-4-mprx').attr('required', true);
                $('#id_1tablas-4-mdrx').attr('required', true); 
            } else {  
                $('#id_1tablas-4-mdm').attr('readonly', true);
                $('#id_1tablas-4-mprx').attr('readonly', true);
                $('#id_1tablas-4-mdrx').attr('readonly', true);	
                $('#id_1tablas-4-mdm').attr('required', false);
                $('#id_1tablas-4-mprx').attr('required', false);
                $('#id_1tablas-4-mdrx').attr('required', false); 

                $('#id_1tablas-4-mdm').val("");
                $('#id_1tablas-4-mprx').val("");
                $('#id_1tablas-4-multiplicacion').val("");
                $('#id_1tablas-4-mdrx').val("");
            }  
        });
        $("#id_1tablas-5-seleccion").click(function() {  
            if($(".checkbox").is(':checked')) {  
                $('#id_1tablas-5-mdm').attr('readonly', false);
                $('#id_1tablas-5-mprx').attr('readonly', false);
                $('#id_1tablas-5-mdrx').attr('readonly', false);    
                $('#id_1tablas-5-mdm').attr('required', true);
                $('#id_1tablas-5-mprx').attr('required', true);
                $('#id_1tablas-5-mdrx').attr('required', true); 
            } else {  
                $('#id_1tablas-5-mdm').attr('readonly', true);
                $('#id_1tablas-5-mprx').attr('readonly', true);
                $('#id_1tablas-5-mdrx').attr('readonly', true); 
                $('#id_1tablas-5-mdm').attr('required', false);
                $('#id_1tablas-5-mprx').attr('required', false);
                $('#id_1tablas-5-mdrx').attr('required', false); 

                $('#id_1tablas-5-mdm').val("");
                $('#id_1tablas-5-mprx').val("");
                $('#id_1tablas-5-multiplicacion').val("");
                $('#id_1tablas-5-mdrx').val("");
            }  
        });
        $("#id_1tablas-6-seleccion").click(function() {  
            if($(".checkbox").is(':checked')) {  
                $('#id_1tablas-6-mdm').attr('readonly', false);
                $('#id_1tablas-6-mprx').attr('readonly', false);
                $('#id_1tablas-6-mdrx').attr('readonly', false);    
                $('#id_1tablas-6-mdm').attr('required', true);
                $('#id_1tablas-6-mprx').attr('required', true);
                $('#id_1tablas-6-mdrx').attr('required', true); 
            } else {  
                $('#id_1tablas-6-mdm').attr('readonly', true);
                $('#id_1tablas-6-mprx').attr('readonly', true);
                $('#id_1tablas-6-mdrx').attr('readonly', true); 
                $('#id_1tablas-6-mdm').attr('required', false);
                $('#id_1tablas-6-mprx').attr('required', false);
                $('#id_1tablas-6-mdrx').attr('required', false); 

                $('#id_1tablas-6-mdm').val("");
                $('#id_1tablas-6-mprx').val("");
                $('#id_1tablas-6-multiplicacion').val("");
                $('#id_1tablas-6-mdrx').val("");
            }  
        });
        $("#id_1tablas-7-seleccion").click(function() {  
            if($(".checkbox").is(':checked')) {  
                $('#id_1tablas-7-mdm').attr('readonly', false);
                $('#id_1tablas-7-mprx').attr('readonly', false);
                $('#id_1tablas-7-mdrx').attr('readonly', false);    
                $('#id_1tablas-7-mdm').attr('required', true);
                $('#id_1tablas-7-mprx').attr('required', true);
                $('#id_1tablas-7-mdrx').attr('required', true); 
            } else {  
                $('#id_1tablas-7-mdm').attr('readonly', true);
                $('#id_1tablas-7-mprx').attr('readonly', true);
                $('#id_1tablas-7-mdrx').attr('readonly', true); 
                $('#id_1tablas-7-mdm').attr('required', false);
                $('#id_1tablas-7-mprx').attr('required', false);
                $('#id_1tablas-7-mdrx').attr('required', false); 

                $('#id_1tablas-7-mdm').val("");
                $('#id_1tablas-7-mprx').val("");
                $('#id_1tablas-7-multiplicacion').val("");
                $('#id_1tablas-7-mdrx').val("");
            }  
        });
        $("#id_1tablas-8-seleccion").click(function() {  
            if($(".checkbox").is(':checked')) {  
                $('#id_1tablas-8-mdm').attr('readonly', false);
                $('#id_1tablas-8-mprx').attr('readonly', false);
                $('#id_1tablas-8-mdrx').attr('readonly', false);    
                $('#id_1tablas-8-mdm').attr('required', true);
                $('#id_1tablas-8-mprx').attr('required', true);
                $('#id_1tablas-8-mdrx').attr('required', true); 
            } else {  
                $('#id_1tablas-8-mdm').attr('readonly', true);
                $('#id_1tablas-8-mprx').attr('readonly', true);
                $('#id_1tablas-8-mdrx').attr('readonly', true); 
                $('#id_1tablas-8-mdm').attr('required', false);
                $('#id_1tablas-8-mprx').attr('required', false);
                $('#id_1tablas-8-mdrx').attr('required', false); 

                $('#id_1tablas-8-mdm').val("");
                $('#id_1tablas-8-mprx').val("");
                $('#id_1tablas-8-multiplicacion').val("");
                $('#id_1tablas-8-mdrx').val("");
            }  
        });
        $("#id_1tablas-9-seleccion").click(function() {  
            if($(".checkbox").is(':checked')) {  
                $('#id_1tablas-9-mdm').attr('readonly', false);
                $('#id_1tablas-9-mprx').attr('readonly', false);
                $('#id_1tablas-9-mdrx').attr('readonly', false);    
                $('#id_1tablas-9-mdm').attr('required', true);
                $('#id_1tablas-9-mprx').attr('required', true);
                $('#id_1tablas-9-mdrx').attr('required', true); 
            } else {  
                $('#id_1tablas-9-mdm').attr('readonly', true);
                $('#id_1tablas-9-mprx').attr('readonly', true);
                $('#id_1tablas-9-mdrx').attr('readonly', true); 
                $('#id_1tablas-9-mdm').attr('required', false);
                $('#id_1tablas-9-mprx').attr('required', false);
                $('#id_1tablas-9-mdrx').attr('required', false); 

                $('#id_1tablas-9-mdm').val("");
                $('#id_1tablas-9-mprx').val("");
                $('#id_1tablas-9-multiplicacion').val("");
                $('#id_1tablas-9-mdrx').val("");
            }  
        });
//-------------------------Tabla 2------------------------------------------
        $("#id_2tablas-0-seleccion").click(function() {  
            if($(".checkbox").is(':checked')) {  
                $('#id_2tablas-0-mdm').attr('readonly', false);
                $('#id_2tablas-0-mprx').attr('readonly', false);
                $('#id_2tablas-0-mdrx').attr('readonly', false);    
                $('#id_2tablas-0-mdm').attr('required', true);
                $('#id_2tablas-0-mprx').attr('required', true);
                $('#id_2tablas-0-mdrx').attr('required', true); 
            } else {  
                //alert("No está activado"); 
                $('#id_2tablas-0-mdm').attr('readonly', true);
                $('#id_2tablas-0-mprx').attr('readonly', true);
                $('#id_2tablas-0-mdrx').attr('readonly', true); 
                $('#id_2tablas-0-mdm').attr('required', false);
                $('#id_2tablas-0-mprx').attr('required', false);
                $('#id_2tablas-0-mdrx').attr('required', false);

                $('#id_2tablas-0-mdm').val("");
                $('#id_2tablas-0-mprx').val("");
                $('#id_2tablas-0-multiplicacion').val("");
                $('#id_2tablas-0-mdrx').val("");
            }  
        });
        $("#id_2tablas-1-seleccion").click(function() {  
            if($(".checkbox").is(':checked')) {  
                $('#id_2tablas-1-mdm').attr('readonly', false);
                $('#id_2tablas-1-mprx').attr('readonly', false);
                $('#id_2tablas-1-mdrx').attr('readonly', false);    
                $('#id_2tablas-1-mdm').attr('required', true);
                $('#id_2tablas-1-mprx').attr('required', true);
                $('#id_2tablas-1-mdrx').attr('required', true);    
            } else {  
                $('#id_2tablas-1-mdm').attr('readonly', true);
                $('#id_2tablas-1-mprx').attr('readonly', true);
                $('#id_2tablas-1-mdrx').attr('readonly', true); 
                $('#id_2tablas-1-mdm').attr('required', false);
                $('#id_2tablas-1-mprx').attr('required', false);
                $('#id_2tablas-1-mdrx').attr('required', false);

                $('#id_2tablas-1-mdm').val("");
                $('#id_2tablas-1-mprx').val("");
                $('#id_2tablas-1-multiplicacion').val("");
                $('#id_2tablas-1-mdrx').val("");    
            }  
        });
        $("#id_2tablas-2-seleccion").click(function() {  
            if($(".checkbox").is(':checked')) {  
                $('#id_2tablas-2-mdm').attr('readonly', false);
                $('#id_2tablas-2-mprx').attr('readonly', false);
                $('#id_2tablas-2-mdrx').attr('readonly', false);    
                $('#id_2tablas-2-mdm').attr('required', true);
                $('#id_2tablas-2-mprx').attr('required', true);
                $('#id_2tablas-2-mdrx').attr('required', true);    
            } else {  
                $('#id_2tablas-2-mdm').attr('readonly', true);
                $('#id_2tablas-2-mprx').attr('readonly', true);
                $('#id_2tablas-2-mdrx').attr('readonly', true); 
                $('#id_2tablas-2-mdm').attr('required', false);
                $('#id_2tablas-2-mprx').attr('required', false);
                $('#id_2tablas-2-mdrx').attr('required', false);

                $('#id_2tablas-2-mdm').val("");
                $('#id_2tablas-2-mprx').val("");
                $('#id_2tablas-2-multiplicacion').val("");
                $('#id_2tablas-2-mdrx').val("");    
            }  
        });
        $("#id_2tablas-3-seleccion").click(function() {  
            if($(".checkbox").is(':checked')) {  
                $('#id_2tablas-3-mdm').attr('readonly', false);
                $('#id_2tablas-3-mprx').attr('readonly', false);
                $('#id_2tablas-3-mdrx').attr('readonly', false);    
                $('#id_2tablas-3-mdm').attr('required', true);
                $('#id_2tablas-3-mprx').attr('required', true);
                $('#id_2tablas-3-mdrx').attr('required', true);    
            } else {  
                $('#id_2tablas-3-mdm').attr('readonly', true);
                $('#id_2tablas-3-mprx').attr('readonly', true);
                $('#id_2tablas-3-mdrx').attr('readonly', true); 
                $('#id_2tablas-3-mdm').attr('required', false);
                $('#id_2tablas-3-mprx').attr('required', false);
                $('#id_2tablas-3-mdrx').attr('required', false);

                $('#id_2tablas-3-mdm').val("");
                $('#id_2tablas-3-mprx').val("");
                $('#id_2tablas-3-multiplicacion').val("");
                $('#id_2tablas-3-mdrx').val("");    
            }  
        });
        $("#id_2tablas-4-seleccion").click(function() {  
            if($(".checkbox").is(':checked')) {  
                $('#id_2tablas-4-mdm').attr('readonly', false);
                $('#id_2tablas-4-mprx').attr('readonly', false);
                $('#id_2tablas-4-mdrx').attr('readonly', false);    
                $('#id_2tablas-4-mdm').attr('required', true);
                $('#id_2tablas-4-mprx').attr('required', true);
                $('#id_2tablas-4-mdrx').attr('required', true);    
            } else {  
                $('#id_2tablas-4-mdm').attr('readonly', true);
                $('#id_2tablas-4-mprx').attr('readonly', true);
                $('#id_2tablas-4-mdrx').attr('readonly', true); 
                $('#id_2tablas-4-mdm').attr('required', false);
                $('#id_2tablas-4-mprx').attr('required', false);
                $('#id_2tablas-4-mdrx').attr('required', false);

                $('#id_2tablas-4-mdm').val("");
                $('#id_2tablas-4-mprx').val("");
                $('#id_2tablas-4-multiplicacion').val("");
                $('#id_2tablas-4-mdrx').val("");    
            }  
        });
        $("#id_2tablas-5-seleccion").click(function() {  
            if($(".checkbox").is(':checked')) {  
                $('#id_2tablas-5-mdm').attr('readonly', false);
                $('#id_2tablas-5-mprx').attr('readonly', false);
                $('#id_2tablas-5-mdrx').attr('readonly', false);    
                $('#id_2tablas-5-mdm').attr('required', true);
                $('#id_2tablas-5-mprx').attr('required', true);
                $('#id_2tablas-5-mdrx').attr('required', true);    
            } else {  
                $('#id_2tablas-5-mdm').attr('readonly', true);
                $('#id_2tablas-5-mprx').attr('readonly', true);
                $('#id_2tablas-5-mdrx').attr('readonly', true); 
                $('#id_2tablas-5-mdm').attr('required', false);
                $('#id_2tablas-5-mprx').attr('required', false);
                $('#id_2tablas-5-mdrx').attr('required', false);

                $('#id_2tablas-5-mdm').val("");
                $('#id_2tablas-5-mprx').val("");
                $('#id_2tablas-5-multiplicacion').val("");
                $('#id_2tablas-5-mdrx').val("");    
            }  
        });
        $("#id_2tablas-6-seleccion").click(function() {  
            if($(".checkbox").is(':checked')) {  
                $('#id_2tablas-6-mdm').attr('readonly', false);
                $('#id_2tablas-6-mprx').attr('readonly', false);
                $('#id_2tablas-6-mdrx').attr('readonly', false);    
                $('#id_2tablas-6-mdm').attr('required', true);
                $('#id_2tablas-6-mprx').attr('required', true);
                $('#id_2tablas-6-mdrx').attr('required', true);    
            } else {  
                $('#id_2tablas-6-mdm').attr('readonly', true);
                $('#id_2tablas-6-mprx').attr('readonly', true);
                $('#id_2tablas-6-mdrx').attr('readonly', true); 
                $('#id_2tablas-6-mdm').attr('required', false);
                $('#id_2tablas-6-mprx').attr('required', false);
                $('#id_2tablas-6-mdrx').attr('required', false); 

                $('#id_2tablas-6-mdm').val("");
                $('#id_2tablas-6-mprx').val("");
                $('#id_2tablas-6-multiplicacion').val("");
                $('#id_2tablas-6-mdrx').val("");   
            }  
        });
        $("#id_2tablas-7-seleccion").click(function() {  
            if($(".checkbox").is(':checked')) {  
                $('#id_2tablas-7-mdm').attr('readonly', false);
                $('#id_2tablas-7-mprx').attr('readonly', false);
                $('#id_2tablas-7-mdrx').attr('readonly', false);    
                $('#id_2tablas-7-mdm').attr('required', true);
                $('#id_2tablas-7-mprx').attr('required', true);
                $('#id_2tablas-7-mdrx').attr('required', true);    
            } else {  
                $('#id_2tablas-7-mdm').attr('readonly', true);
                $('#id_2tablas-7-mprx').attr('readonly', true);
                $('#id_2tablas-7-mdrx').attr('readonly', true); 
                $('#id_2tablas-7-mdm').attr('required', false);
                $('#id_2tablas-7-mprx').attr('required', false);
                $('#id_2tablas-7-mdrx').attr('required', false); 

                $('#id_2tablas-7-mdm').val("");
                $('#id_2tablas-7-mprx').val("");
                $('#id_2tablas-7-multiplicacion').val("");
                $('#id_2tablas-7-mdrx').val("");   
            }  
        });
        $("#id_2tablas-8-seleccion").click(function() {  
            if($(".checkbox").is(':checked')) {  
                $('#id_2tablas-8-mdm').attr('readonly', false);
                $('#id_2tablas-8-mprx').attr('readonly', false);
                $('#id_2tablas-8-mdrx').attr('readonly', false);    
                $('#id_2tablas-8-mdm').attr('required', true);
                $('#id_2tablas-8-mprx').attr('required', true);
                $('#id_2tablas-8-mdrx').attr('required', true);    
            } else {  
                $('#id_2tablas-8-mdm').attr('readonly', true);
                $('#id_2tablas-8-mprx').attr('readonly', true);
                $('#id_2tablas-8-mdrx').attr('readonly', true); 
                $('#id_2tablas-8-mdm').attr('required', false);
                $('#id_2tablas-8-mprx').attr('required', false);
                $('#id_2tablas-8-mdrx').attr('required', false);    

                $('#id_2tablas-8-mdm').val("");
                $('#id_2tablas-8-mprx').val("");
                $('#id_2tablas-8-multiplicacion').val("");
                $('#id_2tablas-8-mdrx').val("");
            }  
        });
        $("#id_2tablas-9-seleccion").click(function() {  
            if($(".checkbox").is(':checked')) {  
                $('#id_2tablas-9-mdm').attr('readonly', false);
                $('#id_2tablas-9-mprx').attr('readonly', false);
                $('#id_2tablas-9-mdrx').attr('readonly', false);    
                $('#id_2tablas-9-mdm').attr('required', true);
                $('#id_2tablas-9-mprx').attr('required', true);
                $('#id_2tablas-9-mdrx').attr('required', true);    
            } else {  
                $('#id_2tablas-9-mdm').attr('readonly', true);
                $('#id_2tablas-9-mprx').attr('readonly', true);
                $('#id_2tablas-9-mdrx').attr('readonly', true); 
                $('#id_2tablas-9-mdm').attr('required', false);
                $('#id_2tablas-9-mprx').attr('required', false);
                $('#id_2tablas-9-mdrx').attr('required', false);  

                $('#id_2tablas-9-mdm').val("");
                $('#id_2tablas-9-mprx').val("");
                $('#id_2tablas-9-multiplicacion').val("");
                $('#id_2tablas-9-mdrx').val("");  
            }  
        });
      
    });  

    

// divide (MdM)(MpRx) entre /MdRx y pone el valor en la columna Valor x

    var suma = 0;
    var valor1 = 0 ;
    var valor2 = 0 ;
    var valor3 = 0 ;
    var valor4 = 0 ;
    var valor5 = 0 ;
    var valor6 = 0 ;
    var valor7 = 0 ;
    var valor8 = 0 ;
    var valor9 = 0 ;
    var valor10 = 0 ;
var suma2 = 0;
    var valor11 = 0 ;
    var valor21 = 0 ;
    var valor31 = 0 ;
    var valor41 = 0 ;
    var valor51 = 0 ;
    var valor61 = 0 ;
    var valor71 = 0 ;
    var valor81= 0 ;
    var valor91 = 0 ;
    var valor101 = 0 ;

var sum = 0;


//-------------------------Tabla 1------------------------------------------



$('#id_1tablas-0-mdrx').change(function() {
    $('#id_1tablas-0-valor_x').val($('#id_1tablas-0-multiplicacion').val()/$('#id_1tablas-0-mdrx').val());
    valor1=parseFloat($('#id_1tablas-0-valor_x').val());
    $('#total1').val(valor1+valor2+valor3+valor4+valor5+valor6+valor7+valor8+valor9+valor10);

});

$('#id_1tablas-1-mdrx').change(function() {
    $('#id_1tablas-1-valor_x').val($('#id_1tablas-1-multiplicacion').val()/$('#id_1tablas-1-mdrx').val());
    
    valor2=parseFloat($('#id_1tablas-1-valor_x').val());

    $('#total1').val(valor1+valor2+valor3+valor4+valor5+valor6+valor7+valor8+valor9+valor10);

});
$('#id_1tablas-2-mdrx').change(function() {
    $('#id_1tablas-2-valor_x').val($('#id_1tablas-2-multiplicacion').val()/$('#id_1tablas-2-mdrx').val());
    
    valor3=parseFloat($('#id_1tablas-2-valor_x').val());

    $('#total1').val(valor1+valor2+valor3+valor4+valor5+valor6+valor7+valor8+valor9+valor10);

});
$('#id_1tablas-3-mdrx').change(function() {
    $('#id_1tablas-3-valor_x').val($('#id_1tablas-3-multiplicacion').val()/$('#id_1tablas-3-mdrx').val());
    
    valor4=parseFloat($('#id_1tablas-3-valor_x').val());

    $('#total1').val(valor1+valor2+valor3+valor4+valor5+valor6+valor7+valor8+valor9+valor10);

});
$('#id_1tablas-4-mdrx').change(function() {
    $('#id_1tablas-4-valor_x').val($('#id_1tablas-4-multiplicacion').val()/$('#id_1tablas-4-mdrx').val());
    
    valor5=parseFloat($('#id_1tablas-4-valor_x').val());

    $('#total1').val(valor1+valor2+valor3+valor4+valor5+valor6+valor7+valor8+valor9+valor10);

});
$('#id_1tablas-5-mdrx').change(function() {
    $('#id_1tablas-5-valor_x').val($('#id_1tablas-5-multiplicacion').val()/$('#id_1tablas-5-mdrx').val());
    
    valor6=parseFloat($('#id_1tablas-5-valor_x').val());

    $('#total1').val(valor1+valor2+valor3+valor4+valor5+valor6+valor7+valor8+valor9+valor10);

});
$('#id_1tablas-6-mdrx').change(function() {
    $('#id_1tablas-6-valor_x').val($('#id_1tablas-6-multiplicacion').val()/$('#id_1tablas-6-mdrx').val());
    
    valor7=parseFloat($('#id_1tablas-6-valor_x').val());

    $('#total1').val(valor1+valor2+valor3+valor4+valor5+valor6+valor7+valor8+valor9+valor10);

});
$('#id_1tablas-7-mdrx').change(function() {
    $('#id_1tablas-7-valor_x').val($('#id_1tablas-7-multiplicacion').val()/$('#id_1tablas-7-mdrx').val());
    
    valor8=parseFloat($('#id_1tablas-7-valor_x').val());

    $('#total1').val(valor1+valor2+valor3+valor4+valor5+valor6+valor7+valor8+valor9+valor10);

});
$('#id_1tablas-8-mdrx').change(function() {
    $('#id_1tablas-8-valor_x').val($('#id_1tablas-8-multiplicacion').val()/$('#id_1tablas-8-mdrx').val());
    
    valor9=parseFloat($('#id_1tablas-8-valor_x').val());

    $('#total1').val(valor1+valor2+valor3+valor4+valor5+valor6+valor7+valor8+valor9+valor10);

});
$('#id_1tablas-9-mdrx').change(function() {
    $('#id_1tablas-9-valor_x').val($('#id_1tablas-9-multiplicacion').val()/$('#id_1tablas-9-mdrx').val());
    
    valor10=parseFloat($('#id_1tablas-9-valor_x').val());

    $('#total1').val(valor1+valor2+valor3+valor4+valor5+valor6+valor7+valor8+valor9+valor10);

    $('#maxilareden').val(ed_mand1+"-"+$('#total1').val());
    $('#maxilartotal').val($('#id_ed_maxi').val()-$('#total1').val());


});

//-------------------------Tabla 2------------------------------------------

$('#id_2tablas-0-mdrx').change(function() {
    $('#id_2tablas-0-valor_x').val($('#id_2tablas-0-multiplicacion').val()/$('#id_2tablas-0-mdrx').val());
    valor11=parseFloat($('#id_2tablas-0-valor_x').val());
$('#total2').val(valor11+valor21+valor31+valor41+valor51+valor61+valor71+valor81+valor91+valor101);

});

$('#id_2tablas-1-mdrx').change(function() {
    $('#id_2tablas-1-valor_x').val($('#id_2tablas-1-multiplicacion').val()/$('#id_2tablas-1-mdrx').val());
    
    valor21=parseFloat($('#id_2tablas-1-valor_x').val());

$('#total2').val(valor11+valor21+valor31+valor41+valor51+valor61+valor71+valor81+valor91+valor101);

});
$('#id_2tablas-2-mdrx').change(function() {
    $('#id_2tablas-2-valor_x').val($('#id_2tablas-2-multiplicacion').val()/$('#id_2tablas-2-mdrx').val());
    
    valor31=parseFloat($('#id_2tablas-2-valor_x').val());

$('#total2').val(valor11+valor21+valor31+valor41+valor51+valor61+valor71+valor81+valor91+valor101);

});
$('#id_2tablas-3-mdrx').change(function() {
    $('#id_2tablas-3-valor_x').val($('#id_2tablas-3-multiplicacion').val()/$('#id_2tablas-3-mdrx').val());
    
    valor41=parseFloat($('#id_2tablas-3-valor_x').val());

$('#total2').val(valor11+valor21+valor31+valor41+valor51+valor61+valor71+valor81+valor91+valor101);
});
$('#id_2tablas-4-mdrx').change(function() {
    $('#id_2tablas-4-valor_x').val($('#id_2tablas-4-multiplicacion').val()/$('#id_2tablas-4-mdrx').val());
    
    valor51=parseFloat($('#id_2tablas-4-valor_x').val());

$('#total2').val(valor11+valor21+valor31+valor41+valor51+valor61+valor71+valor81+valor91+valor101);
});
$('#id_2tablas-5-mdrx').change(function() {
    $('#id_2tablas-5-valor_x').val($('#id_2tablas-5-multiplicacion').val()/$('#id_2tablas-5-mdrx').val());
    
    valor61=parseFloat($('#id_2tablas-5-valor_x').val());

$('#total2').val(valor11+valor21+valor31+valor41+valor51+valor61+valor71+valor81+valor91+valor101);
});
$('#id_2tablas-6-mdrx').change(function() {
    $('#id_2tablas-6-valor_x').val($('#id_2tablas-6-multiplicacion').val()/$('#id_2tablas-6-mdrx').val());
    
    valor71=parseFloat($('#id_2tablas-6-valor_x').val());

$('#total2').val(valor11+valor21+valor31+valor41+valor51+valor61+valor71+valor81+valor91+valor101);
});
$('#id_2tablas-7-mdrx').change(function() {
    $('#id_2tablas-7-valor_x').val($('#id_2tablas-7-multiplicacion').val()/$('#id_2tablas-7-mdrx').val());
    
    valor81=parseFloat($('#id_2tablas-7-valor_x').val());

$('#total2').val(valor11+valor21+valor31+valor41+valor51+valor61+valor71+valor81+valor91+valor101);
});
$('#id_2tablas-8-mdrx').change(function() {
    $('#id_2tablas-8-valor_x').val($('#id_2tablas-8-multiplicacion').val()/$('#id_2tablas-8-mdrx').val());
    
    valor91=parseFloat($('#id_2tablas-8-valor_x').val());

    $('#total2').val(valor11+valor21+valor31+valor41+valor51+valor61+valor71+valor81+valor91+valor101);

});
$('#id_2tablas-9-mdrx').change(function() {
    $('#id_2tablas-9-valor_x').val($('#id_2tablas-9-multiplicacion').val()/$('#id_2tablas-9-mdrx').val());
    
    valor101=parseFloat($('#id_2tablas-9-valor_x').val());

    $('#total2').val(valor11+valor21+valor31+valor41+valor51+valor61+valor71+valor81+valor91+valor101);

    $('#mandibulareden').val(ed_mand1+"-"+$('#total2').val());
    $('#mandibulartotal').val($('#id_ed_mand').val()-$('#total2').val());

});

//----------------------------------------------------------------------------------------------------------------

// agarra los valores de x y hace la suma, ademas agrega los datos en la tabla 3

//-------------------------Tabla 1------------------------------------------
    $('#id_1tablas-0-valor_x').change(function() {
      valor1 += Number($('#id_1tablas-0-valor_x').val());
      $('#total1').val(valor1+valor2+valor3+valor4+valor5+valor6+valor7+valor8+valor9+valor10);
      $('#maxilareden').val(ed_mand1+"-"+$('#total1').val());
      $('#maxilartotal').val(ed_mand1-$('#total1').val());
    });
    $('#id_1tablas-1-valor_x').change(function() {
      valor2 = Number($('#id_1tablas-1-valor_x').val());
      $('#total1').val(valor1+valor2+valor3+valor4+valor5+valor6+valor7+valor8+valor9+valor10);
      $('#maxilareden').val(ed_mand1+"-"+$('#total1').val());
      $('#maxilartotal').val(ed_mand1-$('#total1').val());
    });
    $('#id_1tablas-2-valor_x').change(function() {
      valor3 = Number($('#id_1tablas-2-valor_x').val());
      $('#total1').val(valor1+valor2+valor3+valor4+valor5+valor6+valor7+valor8+valor9+valor10);
      $('#maxilareden').val(ed_mand1+"-"+$('#total1').val());
      $('#maxilartotal').val(ed_mand1-$('#total1').val());
    });
    $('#id_1tablas-3-valor_x').change(function() {
      valor4 = Number($('#id_1tablas-3-valor_x').val());
      $('#total1').val(valor1+valor2+valor3+valor4+valor5+valor6+valor7+valor8+valor9+valor10);
      $('#maxilareden').val(ed_mand1+"-"+$('#total1').val());
      $('#maxilartotal').val(ed_mand1-$('#total1').val());
    });
    $('#id_1tablas-4-valor_x').change(function() {
      valor5 = Number($('#id_1tablas-4-valor_x').val());
      $('#total1').val(valor1+valor2+valor3+valor4+valor5+valor6+valor7+valor8+valor9+valor10);
      $('#maxilareden').val(ed_mand1+"-"+$('#total1').val());
      $('#maxilartotal').val(ed_mand1-$('#total1').val());
    });
    $('#id_1tablas-5-valor_x').change(function() {
      valor6 = Number($('#id_1tablas-5-valor_x').val());
      $('#total1').val(valor1+valor2+valor3+valor4+valor5+valor6+valor7+valor8+valor9+valor10);
      $('#maxilareden').val(ed_mand1+"-"+$('#total1').val());
      $('#maxilartotal').val(ed_mand1-$('#total1').val());
    });
    $('#id_1tablas-6-valor_x').change(function() {
      valor7 = Number($('#id_1tablas-6-valor_x').val());
      $('#total1').val(valor1+valor2+valor3+valor4+valor5+valor6+valor7+valor8+valor9+valor10);
      $('#maxilareden').val(ed_mand1+"-"+$('#total1').val());
      $('#maxilartotal').val(ed_mand1-$('#total1').val());
    });
    $('#id_1tablas-7-valor_x').change(function() {
      valor8 = Number($('#id_1tablas-7-valor_x').val());
      $('#total1').val(valor1+valor2+valor3+valor4+valor5+valor6+valor7+valor8+valor9+valor10);
      $('#maxilareden').val(ed_mand1+"-"+$('#total1').val());
      $('#maxilartotal').val(ed_mand1-$('#total1').val());
    });
    $('#id_1tablas-8-valor_x').change(function() {
      valor9 = Number($('#id_1tablas-8-valor_x').val());
      $('#total1').val(valor1+valor2+valor3+valor4+valor5+valor6+valor7+valor8+valor9+valor10);
      $('#maxilareden').val(ed_mand1+"-"+$('#total1').val());
      $('#maxilartotal').val(ed_mand1-$('#total1').val());
    });
    $('#id_1tablas-9-valor_x').change(function() {
      valor10 = Number($('#id_1tablas-9-valor_x').val());
      $('#total1').val(valor1+valor2+valor3+valor4+valor5+valor6+valor7+valor8+valor9+valor10);
      $('#maxilareden').val(ed_mand1+"-"+$('#total1').val());
      $('#maxilartotal').val(ed_mand1-$('#total1').val());
    });


    $('#total1').val(valor1+valor2+valor3+valor4+valor5+valor6+valor7+valor8+valor9+valor10);

//-------------------------Tabla 2------------------------------------------

    $('#id_2tablas-0-valor_x').change(function() {
      valor11 = Number($('#id_2tablas-0-valor_x').val());
      $('#total2').val(valor11+valor21+valor31+valor41+valor51+valor61+valor71+valor81+valor91+valor101);
      $('#mandibulareden').val(ed_mand12+"-"+$('#total2').val());
      $('#mandibulartotal').val(ed_mand12-$('#total2').val());
    });
    $('#id_2tablas-1-valor_x').change(function() {
      valor21 = Number($('#id_2tablas-1-valor_x').val());
      $('#total2').val(valor11+valor21+valor31+valor41+valor51+valor61+valor71+valor81+valor91+valor101);
      $('#mandibulareden').val(ed_mand12+"-"+$('#total2').val());
      $('#mandibulartotal').val(ed_mand12-$('#total2').val());
    });
    $('#id_2tablas-2-valor_x').change(function() {
      valor31 = Number($('#id_2tablas-2-valor_x').val());
      $('#total2').val(valor11+valor21+valor31+valor41+valor51+valor61+valor71+valor81+valor91+valor101);
      $('#mandibulareden').val(ed_mand12+"-"+$('#total2').val());
      $('#mandibulartotal').val(ed_mand12-$('#total2').val());
    });
    $('#id_2tablas-3-valor_x').change(function() {
      valor41 = Number($('#id_2tablas-3-valor_x').val());
      $('#total2').val(valor11+valor21+valor31+valor41+valor51+valor61+valor71+valor81+valor91+valor101);
      $('#mandibulareden').val(ed_mand12+"-"+$('#total2').val());
      $('#mandibulartotal').val(ed_mand12-$('#total2').val());
    });
    $('#id_2tablas-4-valor_x').change(function() {
      valor51 = Number($('#id_2tablas-4-valor_x').val());
      $('#total2').val(valor11+valor21+valor31+valor41+valor51+valor61+valor71+valor81+valor91+valor101);
      $('#mandibulareden').val(ed_mand12+"-"+$('#total2').val());
      $('#mandibulartotal').val(ed_mand12-$('#total2').val());
    });
    $('#id_2tablas-5-valor_x').change(function() {
      valor61 = Number($('#id_2tablas-5-valor_x').val());
      $('#total2').val(valor11+valor21+valor31+valor41+valor51+valor61+valor71+valor81+valor91+valor101);
      $('#mandibulareden').val(ed_mand12+"-"+$('#total2').val());
      $('#mandibulartotal').val(ed_mand12-$('#total2').val());
    });
    $('#id_2tablas-6-valor_x').change(function() {
      valor71 = Number($('#id_2tablas-6-valor_x').val());
      $('#total2').val(valor11+valor21+valor31+valor41+valor51+valor61+valor71+valor81+valor91+valor101);
      $('#mandibulareden').val(ed_mand12+"-"+$('#total2').val());
      $('#mandibulartotal').val(ed_mand12-$('#total2').val());
    });
    $('#id_2tablas-7-valor_x').change(function() {
      valor81 = Number($('#id_2tablas-7-valor_x').val());
      $('#total2').val(valor11+valor21+valor31+valor41+valor51+valor61+valor71+valor81+valor91+valor101);
      $('#mandibulareden').val(ed_mand12+"-"+$('#total2').val());
      $('#mandibulartotal').val(ed_mand12-$('#total2').val());
    });
    $('#id_2tablas-8-valor_x').change(function() {
      valor91 = Number($('#id_2tablas-8-valor_x').val());
      $('#total2').val(valor11+valor21+valor31+valor41+valor51+valor61+valor71+valor81+valor91+valor101);
      $('#mandibulareden').val(ed_mand12+"-"+$('#total2').val());
      $('#mandibulartotal').val(ed_mand12-$('#total2').val());
    });
    $('#id_2tablas-9-valor_x').change(function() {
      valor101 = Number($('#id_2tablas-9-valor_x').val());
      $('#total2').val(valor11+valor21+valor31+valor41+valor51+valor61+valor71+valor81+valor91+valor101);
      $('#mandibulareden').val(ed_mand12+"-"+$('#total2').val());
      $('#mandibulartotal').val(ed_mand12-$('#total2').val());
    });


    $('#total2').val(valor11+valor21+valor31+valor41+valor51+valor61+valor71+valor81+valor91+valor101);

var ed_mand1="", ed_mand12="";
    $('#id_ed_maxi').change(function() {
        ed_mand1 = $('#id_ed_maxi').val();
      $('#maxilareden').val(ed_mand1);
       $('#maxilareden').val(ed_mand1+"-"+$('#total1').val());
      $('#maxilartotal').val(ed_mand1-$('#total1').val());
    });
    $('#id_ed_mand').change(function() {
        ed_mand12 = $('#id_ed_mand').val();
      $('#mandibulareden').val(ed_mand12);
      $('#mandibulareden').val(ed_mand12+"-"+$('#total2').val());
      $('#mandibulartotal').val(ed_mand12-$('#total2').val());
    });
    
            
//multiplica mdm * mprx

//-------------------------Tabla 1------------------------------------------

$('#id_1tablas-0-mdm').change(function() {
        $('#id_1tablas-0-multiplicacion').val($('#id_1tablas-0-mdm').val()*$('#id_1tablas-0-mprx').val()); 
});
$('#id_1tablas-0-mprx').change(function() {
        $('#id_1tablas-0-multiplicacion').val($('#id_1tablas-0-mdm').val()*$('#id_1tablas-0-mprx').val()); 
});
$('#id_1tablas-1-mdm').change(function() {
        $('#id_1tablas-1-multiplicacion').val($('#id_1tablas-1-mdm').val()*$('#id_1tablas-1-mprx').val()); 
});
$('#id_1tablas-1-mprx').change(function() {
        $('#id_1tablas-1-multiplicacion').val($('#id_1tablas-1-mdm').val()*$('#id_1tablas-1-mprx').val()); 
});
$('#id_1tablas-2-mdm').change(function() {
        $('#id_1tablas-2-multiplicacion').val($('#id_1tablas-2-mdm').val()*$('#id_1tablas-2-mprx').val()); 
});
$('#id_1tablas-2-mprx').change(function() {
        $('#id_1tablas-2-multiplicacion').val($('#id_1tablas-2-mdm').val()*$('#id_1tablas-2-mprx').val()); 
});
$('#id_1tablas-3-mdm').change(function() {
        $('#id_1tablas-3-multiplicacion').val($('#id_1tablas-3-mdm').val()*$('#id_1tablas-3-mprx').val()); 
});
$('#id_1tablas-3-mprx').change(function() {
        $('#id_1tablas-3-multiplicacion').val($('#id_1tablas-3-mdm').val()*$('#id_1tablas-3-mprx').val()); 
});
$('#id_1tablas-4-mdm').change(function() {
        $('#id_1tablas-4-multiplicacion').val($('#id_1tablas-4-mdm').val()*$('#id_1tablas-4-mprx').val()); 
});
$('#id_1tablas-4-mprx').change(function() {
        $('#id_1tablas-4-multiplicacion').val($('#id_1tablas-4-mdm').val()*$('#id_1tablas-4-mprx').val()); 
});
$('#id_1tablas-5-mdm').change(function() {
        $('#id_1tablas-5-multiplicacion').val($('#id_1tablas-5-mdm').val()*$('#id_1tablas-5-mprx').val()); 
});
$('#id_1tablas-5-mprx').change(function() {
        $('#id_1tablas-5-multiplicacion').val($('#id_1tablas-5-mdm').val()*$('#id_1tablas-5-mprx').val()); 
});
$('#id_1tablas-6-mdm').change(function() {
        $('#id_1tablas-6-multiplicacion').val($('#id_1tablas-6-mdm').val()*$('#id_1tablas-6-mprx').val()); 
});
$('#id_1tablas-6-mprx').change(function() {
        $('#id_1tablas-6-multiplicacion').val($('#id_1tablas-6-mdm').val()*$('#id_1tablas-6-mprx').val()); 
});
$('#id_1tablas-7-mdm').change(function() {
        $('#id_1tablas-7-multiplicacion').val($('#id_1tablas-7-mdm').val()*$('#id_1tablas-7-mprx').val()); 
});
$('#id_1tablas-7-mprx').change(function() {
        $('#id_1tablas-7-multiplicacion').val($('#id_1tablas-7-mdm').val()*$('#id_1tablas-7-mprx').val()); 
});
$('#id_1tablas-8-mdm').change(function() {
        $('#id_1tablas-8-multiplicacion').val($('#id_1tablas-8-mdm').val()*$('#id_1tablas-8-mprx').val()); 
});
$('#id_1tablas-8-mprx').change(function() {
        $('#id_1tablas-8-multiplicacion').val($('#id_1tablas-8-mdm').val()*$('#id_1tablas-8-mprx').val()); 
});
$('#id_1tablas-9-mdm').change(function() {
        $('#id_1tablas-9-multiplicacion').val($('#id_1tablas-9-mdm').val()*$('#id_1tablas-9-mprx').val()); 
});
$('#id_1tablas-9-mprx').change(function() {
        $('#id_1tablas-9-multiplicacion').val($('#id_1tablas-9-mdm').val()*$('#id_1tablas-9-mprx').val()); 
});

//-------------------------Tabla 2  ------------------------------------------

$('#id_2tablas-0-mdm').change(function() {
        $('#id_2tablas-0-multiplicacion').val($('#id_2tablas-0-mdm').val()*$('#id_2tablas-0-mprx').val()); 
});
$('#id_2tablas-0-mprx').change(function() {
        $('#id_2tablas-0-multiplicacion').val($('#id_2tablas-0-mdm').val()*$('#id_2tablas-0-mprx').val()); 
});
$('#id_2tablas-1-mdm').change(function() {
        $('#id_2tablas-1-multiplicacion').val($('#id_2tablas-1-mdm').val()*$('#id_2tablas-1-mprx').val()); 
});
$('#id_2tablas-1-mprx').change(function() {
        $('#id_2tablas-1-multiplicacion').val($('#id_2tablas-1-mdm').val()*$('#id_2tablas-1-mprx').val()); 
});
$('#id_2tablas-2-mdm').change(function() {
        $('#id_2tablas-2-multiplicacion').val($('#id_2tablas-2-mdm').val()*$('#id_2tablas-2-mprx').val()); 
});
$('#id_2tablas-2-mprx').change(function() {
        $('#id_2tablas-2-multiplicacion').val($('#id_2tablas-2-mdm').val()*$('#id_2tablas-2-mprx').val()); 
});
$('#id_2tablas-3-mdm').change(function() {
        $('#id_2tablas-3-multiplicacion').val($('#id_2tablas-3-mdm').val()*$('#id_2tablas-3-mprx').val()); 
});
$('#id_2tablas-3-mprx').change(function() {
        $('#id_2tablas-3-multiplicacion').val($('#id_2tablas-3-mdm').val()*$('#id_2tablas-3-mprx').val()); 
});
$('#id_2tablas-4-mdm').change(function() {
        $('#id_2tablas-4-multiplicacion').val($('#id_2tablas-4-mdm').val()*$('#id_2tablas-4-mprx').val()); 
});
$('#id_2tablas-4-mprx').change(function() {
        $('#id_2tablas-4-multiplicacion').val($('#id_2tablas-4-mdm').val()*$('#id_2tablas-4-mprx').val()); 
});
$('#id_2tablas-5-mdm').change(function() {
        $('#id_2tablas-5-multiplicacion').val($('#id_2tablas-5-mdm').val()*$('#id_2tablas-5-mprx').val()); 
});
$('#id_2tablas-5-mprx').change(function() {
        $('#id_2tablas-5-multiplicacion').val($('#id_2tablas-5-mdm').val()*$('#id_2tablas-5-mprx').val()); 
});
$('#id_2tablas-6-mdm').change(function() {
        $('#id_2tablas-6-multiplicacion').val($('#id_2tablas-6-mdm').val()*$('#id_2tablas-6-mprx').val()); 
});
$('#id_2tablas-6-mprx').change(function() {
        $('#id_2tablas-6-multiplicacion').val($('#id_2tablas-6-mdm').val()*$('#id_2tablas-6-mprx').val()); 
});
$('#id_2tablas-7-mdm').change(function() {
        $('#id_2tablas-7-multiplicacion').val($('#id_2tablas-7-mdm').val()*$('#id_2tablas-7-mprx').val()); 
});
$('#id_2tablas-7-mprx').change(function() {
        $('#id_2tablas-7-multiplicacion').val($('#id_2tablas-7-mdm').val()*$('#id_2tablas-7-mprx').val()); 
});
$('#id_2tablas-8-mdm').change(function() {
        $('#id_2tablas-8-multiplicacion').val($('#id_2tablas-8-mdm').val()*$('#id_2tablas-8-mprx').val()); 
});
$('#id_2tablas-8-mprx').change(function() {
        $('#id_2tablas-8-multiplicacion').val($('#id_2tablas-8-mdm').val()*$('#id_2tablas-8-mprx').val()); 
});
$('#id_2tablas-9-mdm').change(function() {
        $('#id_2tablas-9-multiplicacion').val($('#id_2tablas-9-mdm').val()*$('#id_2tablas-9-mprx').val()); 
});
$('#id_2tablas-9-mprx').change(function() {
        $('#id_2tablas-9-multiplicacion').val($('#id_2tablas-9-mdm').val()*$('#id_2tablas-9-mprx').val()); 
});