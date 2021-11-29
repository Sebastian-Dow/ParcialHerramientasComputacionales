###Parcial Final
###Herramientas Computacionales
###Sebastin Dow Valenzuela
###Código: 8950987

def validar(cad, clas):
    profesor = ('profesor', 'Profesor', 'PROFESOR')
    estudiante = ('estudiante', 'Estudiante', 'ESTUDIANTE')
    ans = ''
    end = False

    if clas == 'num':
        while end == False:
            try: 
                int(cad)
                ans = cad
                end = True
            except ValueError:
                cad = input("Digite un valor válido (número entero sin espacios o símbolos): ")

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

def compra():
    ans = ''
    registrando = True
    productos = dict()
    cant = 0
    valor = 0

    print("Por favor, ingrese los siguientes datos:")
    cedula = validar(input("Cédula: "), 'num')
    rol = validar(input("rol (Profesor o estudiante): "), 'rol')
    ans += 'El ' + str(rol) + ' con cedula ' + str(cedula)

    while registrando == True:
        codigo = input("Código del producto: ")

        productos[codigo] = []
        productos[codigo].append(validar(input("Precio del producto: "), 'num'))
        productos[codigo].append(validar(input("Cantidad del producto: "), 'num'))
        end = input("Para registrar otro producto presione enter, para terminar de registrar presione e y luego presione enter.\n")

        if end == 'e':
            registrando = False

    for e in productos:
        if rol == 'profesor':
            valor += int(productos[e][0])*int(productos[e][1])*4/5
        elif rol == 'estudiante':
            valor += int(productos[e][0])*int(productos[e][1])*1/2

    ans += ' debe pagar ' + str(valor) + ' por ' 

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