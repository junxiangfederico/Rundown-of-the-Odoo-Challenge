
idx = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
tmp = [5, 38, 36, 3, 3, 0, 0, 4, 3, 14, 37, 38, 40, 5, 9, 11, 1, 5, 3, 5]
pwd = []
for i in tmp:
    pwd.append(idx[i])
print(''.join(pwd))