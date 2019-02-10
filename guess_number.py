#猜數字
import random
nu = random.randint(1, 100)
count = 0
while True:
	input_nu = input('猜一個 1-100 的整數')
	input_nu = int(input_nu)
	count += 1 # count = count + 1
	if input_nu == nu:
		print('恭喜你猜中了!')
		print('你在第', count, '次猜中')
		break
	elif input_nu == 999:
			print(nu)
	else:
		if input_nu > nu:
			print('你猜的數次太大，再猜一次')
		else:
			print('你猜的數次太小，再猜一次')
	print('這是你猜的第', count, '次')