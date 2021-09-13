class Productos:

    contadorProductos = 0

    def __init__(self,nombre,precio):
        Productos.contadorProductos +=1
        self._idProducto = Productos.contadorProductos
        self._nombre = nombre
        self._precio = precio

    @property
    def precio(self):
        return self._precio

    def __str__(self):
        return f' el producto es: {self._idProducto}, {self._nombre}, y precio: {self._precio}'

if __name__ == '__main__':
    producto1 = Productos('camisa', 500)
    producto2 = Productos('pantalon', 800)
    print(producto1, producto2)