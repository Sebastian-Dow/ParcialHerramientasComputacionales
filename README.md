# ParcialHerramientasComputacionales
Desarrollo del parcial final de curso de Herramientas Computacionales 2021 - 2 por Sebastián Dow Valenzuela
Proyecto iniciado el 28 de Noviembre de 2021.

## Descripción general

Para el desarrollo del programa, se busca crear un código que solicite la información requerida al usuario,
la almacene en memoria, realice las operaciones que sean necesarias para la aplicación de los descuentos
y el cálculo del valor total a pagar y finalmente, retorne un mensaje con formato preestablecido en el
planteamiento del problema.

## Elementos de entrada

El programa se basa en un modelo computacional que registra datos para un único usuario y desarrolla operaciones
en base a los datos registrados. Este programa debe recibir los siguientes datos:

1. Rol del usuario en la institución educativa: Variable cualitativa binominal.
2. Documento de identidad del usuario: Variable cuantitativa entera (Nominal).

Luego, debe recibir una serie de n productos definidos por un código y asociados a un valor monetario
(En pesos) y una cantidad entera:

1. Código del producto: Variable cualitativa nominal.
2. Precio del producto: Variable cuantitativa entera.
3. cantidad del producto: Variable cuantitativa entera.

## Operaciones

Se desarrollará una función que acote las entradas en las que se define el rol del cliente por medio de
ciclos y condicionales que retornen mensajes hasta que se digite un valor válido para ser almacenado en
memoria.

Posteriormente, se deben realizar las operaciones para aplicar los descuentos y calcular el valor total de la
compra, las cuales serían:

Para cada artículos se multiplica la cantidad por el precio, y después de esto, se multiplicará por la razón
del total que se deberá pagar si es estudiante o profesor.

Se deberá repetir este producto para el número total de artículos y finalmente, se deberán sumar todos los
productos para determinar el total.

## Salida

Finalmente, el código debe retornar el siguiente mensaje:

### ”El Rol con cedula -Numero-, debe pagar -Valor- por el producto -Codigo-”

Se puede realizará un cambio en el mensaje de salida para compras de múltiples productos.
