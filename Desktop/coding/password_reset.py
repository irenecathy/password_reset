password = 'a123456'
i = 0
while True:
    user = input('請輸入密碼： ')
    if user != password:
        i += 1
        if i == 1:
            print('密碼錯誤！還有兩次機會')
        elif i == 2:
            print('密碼錯誤！還有一次機會')
        else:
            break
    else:
        print('登入成功！')
        break