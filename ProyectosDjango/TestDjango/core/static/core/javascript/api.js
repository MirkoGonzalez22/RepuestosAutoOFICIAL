 $.getJSON('https://mindicador.cl/api', function(data) {
    var dailyIndicators = data;
    $('<p/>', {
        html: '<p align="center">El valor actual de la UF es $' + dailyIndicators.uf.valor+'</p>'
    }).appendTo("#uf");
}).fail(function() {
    console.log('Error al consumir la API!');
});