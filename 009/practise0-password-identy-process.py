# test for Python

# password identy process

times = 3
correct_password = '123'

while times > 0:
    password = input('your password is :  ')
    if password == correct_password:
        print('right password, loging....')
        break
    elif '*' in password:
        print(times, 'times left')
        continue
    else:
        times -= 1
        print('wrong password')
        print('left', times, 'times')
        
        
        
