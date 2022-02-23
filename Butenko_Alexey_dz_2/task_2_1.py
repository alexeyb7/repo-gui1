test_var = 15 * 3
if isinstance(test_var, int) == True:
    print ('Выражение 15*3 - тип integer')
test_var2 = 15 / 3
if isinstance(test_var2, int) == True:
    print('Выражение 15/3 - тип integer')
elif isinstance(test_var2, float) == True:
    print('Выражение 15/3 - тип float')
test_var3 = 15 // 2
if isinstance(test_var3, int) == True:
    print('Выражение 15//2 - тип integer')
test_var4 = 15 ** 2
if isinstance(test_var4, int) == True:
    print('Выражение 15**2 - тип integer')
print ('Выражение 15*3', type(test_var))
print ('Выражение 15/3', type(test_var2))
print ('Выражение 15//2', type(test_var3))
print ('Выражение 15**2', type(test_var4))
