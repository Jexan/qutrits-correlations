from collections import defaultdict

# Tensor definido como un diccionario recursivo
tensor = lambda: defaultdict(tensor)


def conmutador(A, B):
    return A*B - B*A

def anticonmutador(A, B):
    return A*B + B*A