### Ejercicio 5: Análisis + Desarrollo
La serie de Fibonacci se construye utilizando la siguiente relación de recurrencia: `Fn = Fn1 + Fn2, donde F1 = 1 y F2 = 1`. Por ende, los primeros doce términos de esta serie son: `1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144`

Ahora, consideremos los divisores de estos términos:

```text
1 = 1
1 = 1
2 = 1, 2
3 = 1, 3
5  = 1, 5
8 = 1, 2, 4, 8
13 = 1, 13
21 = 1, 3, 7, 21
34 = 1, 2, 17, 34
55 = 1, 5, 11, 55
89 = 1, 89
144 = 1, 2, 3, 4, 6, 8, 9, 12, 16, 18, 24, 36, 48, 72, 144
```

Como se puede ver, 144 es el primer número de la serie de Fibonacci que tiene más de 10 divisores (de hecho tiene 15).
Crea un script en tu lenguaje favorito que obtenga el primer número de Fibonacci que tiene más de 1000 divisores.

###  Requerimientos
```text
   Python >=3.6
```
Para ejecutar el ejercicio solo se necesita la consola de python.
