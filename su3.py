from sympy import Matrix, I, sqrt, symbols, linear_eq_to_matrix, latex
from comun import tensor, conmutador, anticonmutador

# BASE DE SU(3) 
l0 = Matrix((
    (1,0,0), 
    (0,1,0), 
    (0,0,1)
))
l1 = Matrix((
    (0,1,0), 
    (1,0,0), 
    (0, 0, 0)
))
l2 = Matrix((
    (0,-I,0), 
    (I,0,0), 
    (0, 0, 0)
))
l3 = Matrix((
    (1,0,0), 
    (0,-1,0), 
    (0, 0, 0)
))
l4 = Matrix((
    (0,0,1), 
    (0,0,0), 
    (1,0,0)
))
l5 = Matrix((
    (0,0,-I), 
    (0,0,0), 
    (I, 0, 0)
))
l6 = Matrix((
    (0,0,0), 
    (0,0,1), 
    (0,1,0)
))
l7 = Matrix((
    (0,0,0), 
    (0,0,-I), 
    (0, I, 0)
))
l8 = 1/sqrt(3)*Matrix((
    (1,0,0), 
    (0,1,0), 
    (0,0,-2)
))

base_su3 = (l0, l1, l2, l3, l4, l5, l6, l7, l8)

# TENSORES DESEADOS
f = tensor()
d = tensor()


## RESOLUCIÓN DE COEFICIENTES DE MATRICES EN LA BASE DE SU(3).
# Se definen 9 variables, que son los 9 coeficientes de las bases
x0, x1, x2, x3, x4, x5, x6, x7, x8 = symbols('x0 x1 x2 x3 x4 x5 x6 x7 x8')
syms = (x0, x1, x2, x3, x4, x5, x6, x7, x8)

# Se genera un sistema de ecuaciones en la matrix
matriz_de_ecuaciones = l0*x0 + l1*x1 + l2*x2 + l3*x3 + l4*x4 + l5*x5 + l6*x6 + l7*x7 + l8*x8

# Se crea una matrix 9x9 con el sistema de ecuaciones arriba y se obtiene su inversa
M = linear_eq_to_matrix(list(iter(matriz_de_ecuaciones)), *syms)[0]
M_inv = M.inv()


# Resuelve Mx = A mediante x = M^(-1)A
def resolucion_base_su_3(A):
    return M_inv*A.reshape(9,1)


# CÁLCULO DE LOS TENSORES d, f
for indice_1, l_a in enumerate(base_su3):
    for indice_2, l_b in enumerate(base_su3[indice_1:], indice_1):
        res_conm = conmutador(l_a, l_b)
        res_anti_conm = anticonmutador(l_a, l_b)

        indices_base_conm = resolucion_base_su_3(res_conm)
        indices_base_anti_conm = resolucion_base_su_3(res_anti_conm)

        for i, item in enumerate(iter(indices_base_conm)):
            f[indice_1][indice_2][i] = item
            f[indice_2][indice_1][i] = -item

        for i, item in enumerate(iter(indices_base_anti_conm)):
            d[indice_1][indice_2][i] = item
            d[indice_2][indice_1][i] = item


# Funcion para crear 9 matrices a partir de los tensores de 3 dimensiones
def aplastar_1_nivel(tensor):
    matrices = []
    for i, level_1 in tensor.items():
        matriz = [
            [item for item in level_1[j].values()] for j in level_1
        ]
        matrices.append(Matrix(matriz))    

    return matrices


# Generar el Latex de las 18 matrices (9 de f_ijk, 9 de d_ijk).
def generar_latex_tensores(matrices, simbolo):
    lineas = []
    for indice, matriz in enumerate(matrices):
        lineas.append('\[')
        lineas.append(f'{simbolo}_{{{indice}ij}} = {latex(matriz)}')
        lineas.append('\]')

    return '\n'.join(lineas)


# Comandos para imprimir los tensores f, d como 9 matrices en Latez
def imprimir_tensores_latex():
    tensores_f = aplastar_1_nivel(f)
    tensores_d = aplastar_1_nivel(d)
    print(generar_latex_tensores(tensores_f, 'f'), generar_latex_tensores(tensores_d, 'd'))

# Si se corre directamente, se imprime un Latex con f, d
if __name__ == '__main__':
    imprimir_tensores_latex()