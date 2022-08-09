arreglo = ["10", "20", "30", "40", "50", "60"]

def approvedCoursesCounter():
    counter = 0
    longitude = len(arreglo)
    for i in range(longitude):
            counter += int(arreglo[i])
    return counter

a = approvedCoursesCounter()
print(a)