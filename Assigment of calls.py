#Assigment of calls 

calls = [1, 2, 3, 4, 5, 6,7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
staff = ["anna", "ben", "cherry"]
staff_count = len(staff)
early_staff = 2
early_calls = calls[:5]

#diccionario vacío para poner el staff como claves y las listas de las calls como valores
early_allocation = {}
for employee in staff[:early_staff]:
    #el método .index() devuelve 0 para Anna y 1 para Ben (su posción en la lista)
    position = staff.index(employee)
    early_allocation[employee] = early_calls[position::early_staff] #notación start:stop:step

    print(early_allocation)

    late_calls = calls[5:]
    #la lista debe invertirse para que cherry tome la primera llamada en lugar de anna
    late_staff = staff[::-1]
    late_allocation = {}

    for employee in late_staff:
        position = late_staff.index(employee)
        late_allocation[employee] = late_calls[position::staff_count]

    print(late_allocation)