password = 'a123456'
i = 3 #剩餘機會
while i > 0:
    user = input('請輸入密碼： ')
    if user == password:
        print('登入成功！') #逃出迴圈
        break
    else:
        i -= 1
        print('密碼錯誤！還有', i, '次機會')