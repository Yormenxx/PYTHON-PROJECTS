print("APLICACION PARA CALCULAR EL INTERES DE UN PRESTAMO")


prestamo = float(input("Ingrese el valor del prestamo : "))

apr = float(input("Ingrese el valor de la tasa de interes : "))

anios = int(input("Ingrese la cantidad de años : "))


interes_mensual = apr/1200

cantidad_meses = anios * 12

pago_mensual = prestamo * interes_mensual / (1- (1 + interes_mensual) ** (- cantidad_meses))


print("el pago mensual para el prestamo es: %.2f" % pago_mensual)