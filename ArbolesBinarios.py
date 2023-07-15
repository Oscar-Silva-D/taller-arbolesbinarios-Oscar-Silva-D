class NodoMonticulo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None


class MonticuloBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if not self.raiz:
            self.raiz = NodoMonticulo(valor)
        else:
            cola = [self.raiz]
            while cola:
                nodo = cola.pop(0)
                if not nodo.izquierda:
                    nodo.izquierda = NodoMonticulo(valor)
                    break
                elif not nodo.derecha:
                    nodo.derecha = NodoMonticulo(valor)
                    break
                else:
                    cola.append(nodo.izquierda)
                    cola.append(nodo.derecha)

                cola.append(nodo.izquierda)
                cola.append(nodo.derecha)

        self.flotar(self.raiz)

    def eliminar(self):
        if not self.raiz:
            return None

        nodo_elim = self.raiz
        valor = nodo_elim.valor

        cola = [self.raiz]
        while cola:
            nodo = cola.pop(0)
            if nodo.izquierda:
                if nodo.izquierda is nodo_elim:
                    nodo.izquierda = None
                    break
                else:
                    cola.append(nodo.izquierda)
            if nodo.derecha:
                if nodo.derecha is nodo_elim:
                    nodo.derecha = None
                    break
                else:
                    cola.append(nodo.derecha)

        ultimo_nodo = self.get_ultimo_nodo()
        if ultimo_nodo:
            nodo_elim.valor = ultimo_nodo.valor
            self.hundir(nodo_elim)

        return valor

    def get_ultimo_nodo(self):
        if not self.raiz:
            return None

        cola = [self.raiz]
        ultimo_nodo = None
        while cola:
            nodo = cola.pop(0)
            ultimo_nodo = nodo
            if nodo.izquierda:
                cola.append(nodo.izquierda)
            if nodo.derecha:
                cola.append(nodo.derecha)

        return ultimo_nodo

    def flotar(self, nodo):
        if not nodo:
            return

        padre = self.get_padre(nodo)
        if padre and nodo.valor < padre.valor:
            nodo.valor, padre.valor = padre.valor, nodo.valor
            self.flotar(padre)

    def hundir(self, nodo):
        if not nodo:
            return

        menor = nodo
        if nodo.izquierda and nodo.izquierda.valor < menor.valor:
            menor = nodo.izquierda
        if nodo.derecha and nodo.derecha.valor < menor.valor:
            menor = nodo.derecha

        if menor is not nodo:
            nodo.valor, menor.valor = menor.valor, nodo.valor
            self.hundir(menor)

    def get_padre(self, nodo):
        if not self.raiz or nodo is self.raiz:
            return None

        cola = [self.raiz]
        while cola:
            padre = cola.pop(0)
            if padre.izquierda is nodo or padre.derecha is nodo:
                return padre
            if padre.izquierda:
                cola.append(padre.izquierda)
            if padre.derecha:
                cola.append(padre.derecha)

        return None

    def preorden(self):
        if not self.raiz:
            return []

        resultado = []

        def preorden_recursivo(nodo):
            if not nodo:
                return
            resultado.append(nodo.valor)
            preorden_recursivo(nodo.izquierda)
            preorden_recursivo(nodo.derecha)

        preorden_recursivo(self.raiz)
        return resultado

    def por_niveles(self):
        if not self.raiz:
            return []

        resultado = []
        cola = [self.raiz]

        while cola:
            nodo = cola.pop(0)
            resultado.append(nodo.valor)
            if nodo.izquierda:
                cola.append(nodo.izquierda)
            if nodo.derecha:
                cola.append(nodo.derecha)

        return resultado



monticulo = MonticuloBinario()
monticulo.insertar(7)
monticulo.insertar(3)
monticulo.insertar(5)
monticulo.insertar(9)
monticulo.insertar(1)

print("Recorrido en preorden:", monticulo.preorden())
print("Recorrido por niveles:", monticulo.por_niveles())

valor_eliminado = monticulo.eliminar()
print("Valor eliminado:", valor_eliminado)

print("Recorrido en preorden después de eliminar:", monticulo.preorden())
print("Recorrido por niveles después de eliminar:", monticulo.por_niveles())