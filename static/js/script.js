(function(d,w){
    let i = d.getElementById('tbody');
    let a = i.children;

    

    total = 0;
    
    let cantidadCarrito = d.getElementById('cantidadCarrito');
    
    cantidadCarrito.addEventListener('change', function(){
        
        for (const hijos in a) {
            let numero = 0;
            let contenido = a[numero];
            // console.log(hijos);
            console.log(contenido);
            console.log(numero);
            numero = numero + 1;
        }
        
    });

    
    // console.log(a);


})(document, window);
