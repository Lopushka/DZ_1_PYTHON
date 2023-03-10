print('Ведите размер шоколадки:')
n = int(input())
m = int(input())
k = int(input('Кол-во долек: '))

print("Можно." if k < n * m and ((k % n == 0) or (k % m == 0)) else "Нельзя" )