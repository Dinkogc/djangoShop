from django.http import Http404
from django.shortcuts import render

CATEGORIAS = {
    'electronica': {'nombre': 'Electrónica', 'color': 'primary'},
    'juguetes': {'nombre': 'Juguetes', 'color': 'success'},
    'ropa': {'nombre': 'Ropa', 'color': 'warning'},
}

PRODUCTOS = {
    'electronica': [
        {'nombre': 'TV',        'img': 'img/tv.png', 'precio': '$399.990'},
        {'nombre': 'Iphone',     'img': 'img/iphone.png', 'precio': '$799.000'},
        {'nombre': 'PlayStation', 'img': 'img/ps5.png', 'precio': '$599.000'},
    ],
    'juguetes': [
        {'nombre': 'Auto',             'img': 'img/auto.png', 'precio': '$29.990'},
        {'nombre': 'Pelota de Fútbol', 'img': 'img/ball.png', 'precio': '$12.990'},
        {'nombre': 'Figura de Acción', 'img': 'img/figura.png', 'precio': '$13.990'},
    ],
    'ropa': [
        {'nombre': 'Pantalones',       'img': 'img/pantalon.png', 'precio': '$9.990'},
        {'nombre': 'Chaqueta',       'img': 'img/chaqueta.png', 'precio': '$25.990'},
        {'nombre': 'Camisa',       'img': 'img/camisa.png', 'precio': '$16.990'},
    ],   
}

def index(request):
    categorias = [
        {'slug': slug, 'nombre': data['nombre'], 'color': data['color']}
        for slug, data in CATEGORIAS.items()
    ]
    return render(request, 'index.html', {'categorias': categorias})

def categoria(request, categoria):
    if categoria not in PRODUCTOS:
        raise Http404("Categoría no encontrada")
    nombre_categoria = CATEGORIAS[categoria]['nombre']
    items = PRODUCTOS[categoria]
    contexto = {
        'categoria_slug': categoria,
        'categoria_nombre': nombre_categoria,
        'productos': items,
    }
    return render(request, 'productos.html', contexto)