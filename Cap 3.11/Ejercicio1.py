
print("Ejericicio 1")
print("Calculo de salario")

horas = float(input("Intoduzaca las horas: "))
tarifa = float(input("Introduza la tarifa por hora: "))


if horas > 40 :
    resto = horas - 40
    mas_tarifa = (resto*tarifa)*1.5
    salario_bruto = (40*tarifa) + mas_tarifa
    
    salario_total = str(salario_bruto)
    print("Salario: " + salario_total)
    
else: 
    salario_bruto = horas*tarifa
    salario_total = str(salario_bruto)
    print("Salario: " + salario_total)
    
print("Fin del calculo")


