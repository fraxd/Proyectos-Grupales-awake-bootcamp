window.carro=[];

carro = JSON.parse(localStorage.getItem('carro'))


console.log(carro[1])
window.addEventListener('load', function () {
    window.cargarPag();
})

window.cargarPag = function () {
   
    let llenar = document.querySelector("#tbody");
    let total=0;
    for (let i = 0; i < window.carro.length; i++) {
        
    let articuloactual=window.carro[i];
    let totalactual= articuloactual.total;
    let row = document.createElement('tr');
    let col4 = document.createElement('td');
    col4.innerText = articuloactual.nombre;
    let col5 = document.createElement('td');
    col5.innerText = articuloactual.cantidad;
    let col6 = document.createElement('td');
    col6.innerText = " $"+articuloactual.precio;
    let col7 = document.createElement('td');
    col7.innerText="$"+articuloactual.total;
   
    
    
    llenar.appendChild(row);
    row.appendChild(col4);
    row.appendChild(col5);
    row.appendChild(col6);
    row.appendChild(col7);
    
    total=total+totalactual;
    }
    let rtotal = document.querySelector("#rtotal");
    
    let col8 = document.createElement('th');
    col8.classList.add("col-3", "col-lg-12");
    col8.innerText="$"+total;
    rtotal.appendChild(col8)
}
    
