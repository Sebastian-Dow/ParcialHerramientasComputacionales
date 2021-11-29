###Parcial Final
###Herramientas Computacionales
###Sebastin Dow Valenzuela
###Código: 8950987

""" La siguiente función se utiliza para acotar las entradas y prevenir
los distintoserrores que puedan surgir en la ejecución del programa. 
Esta función recibe como argumentos cadenas que corresponden a la entrada 
a ser verificada y a una clave que definirá de qué tipo sebe ser esa 
clave y retornará un único argumento correspondiente a una cadena con 
la entrada más apropiada. """

def validar(cad, clas):
    profesor = ('profesor', 'Profesor', 'PROFESOR')     # Variantes de los roles que se admiten
    estudiante = ('estudiante', 'Estudiante', 'ESTUDIANTE')
    ans = ''
    end = False
    
    ### Prueba de verificación para entradas que deberían ser números enteros
    
    if clas == 'num':
        while end == False:
            try: 
                int(cad)
                ans = cad
                end = True
            except ValueError:
                cad = input("Digite un valor válido (número entero sin espacios o símbolos): ")
    
    ### Prueba de verificación para entradas que deberían ser roles admitidos
    
    if clas == 'rol':
        while end == False:
            if cad in profesor:
                ans = 'profesor'
                end = True
            elif cad in estudiante:
                ans = 'estudiante'
                end = True
            else: 
                cad = str(input("Digite un rol válido (profesor o estudiante): "))

    return ans
    
""" La siguiente función desarrolla el proceso de solicitar y almacenar
los datos, realizar operaciones con ellos y finalmente retornar el 
mensaje esperado. """

def compra():
    ans = ''
    registrando = True
    productos = dict()
    cant = 0
    valor = 0

    ### Los siguiente inputs corresponden a los datos que inicialmente se solicitan:

    print("Por favor, ingrese los siguientes datos:")
    cedula = validar(input("Cédula: "), 'num')
    rol = validar(input("rol (Profesor o estudiante): "), 'rol')
    ans += 'El ' + str(rol) + ' con cedula ' + str(cedula)
    
    ### Ciclo que permite almacenar en diccionarios, múltiples productos con sus
    ### respectivos precios y cantidades:

    while registrando == True:
        codigo = input("Código del producto: ")

        productos[codigo] = []
        productos[codigo].append(validar(input("Precio del producto: "), 'num'))
        productos[codigo].append(validar(input("Cantidad del producto: "), 'num'))
        end = input("Para registrar otro producto presione enter, para terminar de registrar presione e y luego presione enter.\n")

        if end == 'e':
            registrando = False
            
    ### Operaciones que definen el valor a pagar aplicando el descuento:

    for e in productos:
        if rol == 'profesor':
            valor += int(productos[e][0])*int(productos[e][1])*4/5
        elif rol == 'estudiante':
            valor += int(productos[e][0])*int(productos[e][1])*1/2

    ans += ' debe pagar ' + str(valor) + ' por ' 
    
    ### Finalmente, se determina un mensaje para un único o varios productos:

    for i in range(len(productos)):
        cant += 1

    if cant == 1:
        ans += 'el producto ' + str(codigo)
    else:
        ans += 'los productos con los códigos:\n'
    for e in productos:
        ans += str(e) + '\n'

    print(ans)

compra()
