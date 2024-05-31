//declaracion de los eventos de los botones
    const botonNumero = document.getElementsByName("numero");
    const botonOpe = document.getElementsByName("operador");
    const botonIgual = document.getElementsByName("igual")[0];
    const botonReset = document.getElementsByName("reset")[0];

//declaracion de variables
    var pantalla =document.getElementById("pantalla");
    var opeActual= '';
    var opeAnterior= '';
    var operacion= undefined;

//eventos "forEach" recorre los numeros
    botonNumero.forEach(function(boton){//agrega numeros
        boton.addEventListener('click', function(){
        //llamamos a esta funcion
            agregarNumero(boton.innerText);
        })
    });

    botonOpe.forEach(function(boton){//agrega las operaciones
        boton.addEventListener('click', function(){
        //llamamos a esta funcion
        selectOperacion(boton.innerText);
        })
    });

    botonIgual.addEventListener('click',function(){//manda llamar la funcion resultado
        //llamamos a dos funciones
        calcular();
        actualizarDisplay();
    });

    botonReset.addEventListener('click',function(){//se borra todo lo hecho con el boton C
            //llamamos a dos funciones
            clear();
            actualizarDisplay();
    }); 

//acciones de cada funcion

function selectOperacion(op){//seleccion de la operacion.
    if(opeActual == '') return;
    if(opeAnterior !==''){
        calcular();//llamamos a esta funcion para poder hacer mas operaciones
    }
    operacion= op.toString();
    opeAnterior= opeActual;
    opeActual='';
}

function calcular(){// funcion para cada operacion.
    var calculo;
    const anterior = parseFloat(opeAnterior);//tranformacion a numeros flotantes
    const actual = parseFloat(opeActual);
    
//seleccion de operacion
    switch(operacion){
        case '+':
            calculo= anterior + actual;
            break;
        case '-':
            calculo= anterior - actual;
            break;
        case 'x':
            calculo= anterior* actual;
            break;
        case '/':
            calculo= anterior/ actual;
            break;
        default:
        return;
    }
    //regresamos a su forma original
    opeActual= calculo;
    operacion= undefined;
    opeAnterior= '';
}

function agregarNumero(num){
    opeActual = opeActual.toString() + num.toString(); //se agregan los numeros sin hacer ninguna ope.
    actualizarDisplay();//llamamos la funcion
}

function clear(){
    //se borra todo lo que se haya echo cada que se recarga la pag.
    opeActual = '';
    opeAnterior='';
    operacion= undefined;
}

function actualizarDisplay(){//miuestra el resultado
    pantalla.value= opeActual;
}

clear();