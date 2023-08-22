
print("Ejericicio 2")
print("Calculo de Salario con try y except")

num_horas = (input("Intoduzaca las horas: "))

try:
    horas = float(num_horas)
except:
    print("Error, porfavor introduzca un numero")
    print()
else :
    tarifa_hora = (input("Introduza la tarifa por hora: "))
    try:
        tarifa = float(tarifa_hora) 
    except:
        print("Error, porfavor introduzca un numero")
        print()
    else:
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
