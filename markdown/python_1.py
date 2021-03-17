print('猜數字遊戲, 請心中想一個0~7之間的數字, 然後回答問題\n有沒有看到心中的數字:\n1, 3, 5, 7')
answer = input('輸入y或Y代表有, 其他代表無:')
if answer is 'y' or 'Y' :
  num = (1 or 3 or 5 or 7)
  input('有沒有看到心中的數字:\n2, 3, 6, 7\n輸入y或Y代表有, 其他代表無:')
    if answer is 'y' or 'Y' :
      num = (3 or 7)
    elif answer is 'n' or 'N' :
      num = (0 or 4)
elif answer is 'n' or 'N' :
  num = (0 or 2 or 4 or 6)
  input('有沒有看到心中的數字:\n2, 3, 6, 7\n輸入y或Y代表有, 其他代表無:')