#猜數字
import random
x = int(input('請輸入猜測範圍最小值'))
y = int(input('請輸入猜測範圍最大值'))
r_num = random.randint(x, y)
count = 0
while True:
	print('你設定的範圍是', x, '-', y)
	num = int(input('猜一個範圍內的整數'))
	count += 1 # count = count + 1
	if num == r_num:
		print('恭喜你猜中了!')
		print('你在第', count, '次猜中')
		break
	elif num == 999:
			print(r_num)
	else:
		if num > y or num < x:
			print('你猜的數字超過範圍')
		elif num > r_num:
			print('你猜的數字太大，再猜一次')
		elif num < r_num:
			print('你猜的數字太小，再猜一次')
	print('這是你猜的第', count, '次')