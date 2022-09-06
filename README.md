# Quitrits-Correlations
Repositorio que contiene código relevante a mi proyecto de grado. Hecho usando Sympy.

# Archivos:

## su3.py

Contiene una caracterización del espacio SU(3), incluyendo:

* `li` (i = 0, 1, 2, ..., 8), la base de SU(3), junto con la unidad.
* `f[i][j][k]`, `d[i][j][k]`, los tensores que definen las constantes de estructura.
* `resolver_su_3(matriz)`, función que devuelve un vector con los coeficientes de la combinación lineal de los `li` que conforman la matriz proporcionada.
* Si se corre como un script individual, devuelve una representación en LaTex de los tensores `f`, `d` representados en matrices.

## comun.py

Contiene operaciones y estructuras comunes.

* `conmutador(A, B)`, `anticonmutador(A, B)`, equivalentes a aplicar la operación correspondiente
* `tensor()`, función que devuelve una estructura de datos que puede funcionar como un tensor de dimensión arbitraria
