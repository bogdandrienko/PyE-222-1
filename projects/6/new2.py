#У нас есть массив чисел от 1 до 50 четных чисел нужно вывести в текстовый документ азными сточками в квадатах этих чисел
s = [i for i in range(2,51,2)]
print(s)
with open('new.txt','w') as f:
    f.write('Abuka')
    for i in s:
        f.write(f'{i**2} \n')

