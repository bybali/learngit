import pyautogui
from tkinter import *
from tkinter import messagebox
import time

        
# 获取鼠标位置
def get_mouse_position():
	time.sleep(3) # 准备时间
	print('开始获取鼠标位置')
	try:
		for i in range(1):
			x, y = pyautogui.position()
			positionStr = '鼠标坐标点（X,Y）为：{},{}'.format(str(x).rjust(4), str(y).rjust(4))
			pix = pyautogui.screenshot().getpixel((x, y)) # 获取鼠标所在屏幕点的RGB颜色
			positionStr += ' RGB:(' + str(pix[0]).rjust(3) + ',' + str(pix[1]).rjust(3) + ',' + str(pix[2]).rjust(3) + ')'
			print(positionStr)
			time.sleep(0.5) # 停顿时间
	except:
		print('获取鼠标位置失败')
	print ('return is:',x,y)
	return x,y


# 设置播放器=play, 检测5秒，仍为白色，说明是暂停状态，点击一次
def set_player_start(x, y):
#   播放状态下防治鼠标长期不动，此处移动一下
	pyautogui.moveTo (900,200,0.25)
	temp = 0
	for j in range(5):
		pix = pyautogui.screenshot().getpixel((x,y))
		for i in range(3):
			if pix[i] == 255:
				temp += 1
		time.sleep(1)
	print ('temp is:', temp)
	if temp == 15:
		pyautogui.moveTo(x,y,0.5)
		pyautogui.click()


if __name__ == "__main__":
	# init the screen size
	pyautogui.moveTo(100,100,duration=1.5)
	# storing the size of the screen
	size=pyautogui.size()
	print(size.width, size.height)

	# 获取fresh鼠标位置：
	if 'OK' == pyautogui.confirm(text='In 5s', title='GET WEB FRESH POSISION', buttons=['OK', 'Cancel']):
		time.sleep(2)
		x_fresh,y_fresh = get_mouse_position()
		print ('(x_fresh,y_fresh）为：{},{}'.format(x_fresh,y_fresh))

	if 'OK' == pyautogui.confirm(text='In 5s', title='MOVE TO THE START', buttons=['OK', 'Cancel']):
		time.sleep(2)
		#mac zgdaoyou: x,y=(140,720),播放器按键位置
		x,y = get_mouse_position()
		print ('(x,y）：{},{}'.format(x,y))
		runtime = pyautogui.confirm(text='',title='分钟选择',buttons=[10,60,360])
		for p in range(int(runtime)*6):
			set_player_start(x,y)
			time.sleep(5)
			pyautogui.moveTo(200,200)
			if p % 60 == 0:
				pyautogui.moveTo(x_fresh,y_fresh,0.5)
				print ('fresh the web to check the status..')
				pyautogui.click()


# click the screen by just writting the code
#pyautogui.click(100,200)
 
# scroll the screen
#pyautogui.scroll(100)