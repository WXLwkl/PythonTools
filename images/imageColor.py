#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image
import os, sys

print(os.getcwd())#获得当前工作目录
print(os.path.abspath('.')) #获得当前工作目录
print(os.path.abspath('..'))#获得当前工作目录的父目录
print(os.path.abspath(os.curdir))#获得当前工作目录

class ChangeImageColor(object):

	@classmethod
	def startHandle(self, rgb):
		# 获取当前路径，并创建新目录用于输出结果image
		path = os.getcwd() + '/res'
		npath = os.getcwd() + '/res/result/'

		print("路径：", os.getcwd())

		if not os.path.exists(npath):
			os.makedirs(npath)
		else:
			# 如果存在相同新目录，那么删除下面文件
			for root, dirs, files in os.walk(npath):
				for file_name in files:
					os.remove(npath + file_name)

		# 新颜色值
		nr, ng, nb = rgb
		# 存放背景颜色
		br, bg, bb, ba = 0, 0, 0, 0
		# 遍历目录
		for root, dirs, files in os.walk(path):
			print("root: %s" % root) # 当前目录路径
			print(f"firs: {files}") # 当前路径下所有子目录
			print("files: ", files) # 当前路径下所有非目录子文件

			# 遍历所有图片文件
			for file_name in files:
				if file_name != '.DS_Store':
					image = Image.open(root + '/' + file_name)
					if image is not None:
						image_width, image_height = image.size
						# 遍历Image每个像素
						for i in range(image_width):
							for j in range(image_height):
								xy = (i, j)
								#下面是获取像素和比较像素
								color = image.getpixel(xy)
								color_num = len(color)
								# 判断颜色是否有alpha值
								if color_num == 4:
									r, g, b, a = color
									if i == 0 and j == 0:
										br, bg, bb, ba = color
									if br != r or bg != g or bb != b:
										# 替换像素并保留alpha值
										image.putpixel(xy, (nr, ng, nb, a))
								elif color_num == 3:
									r, g, b = color
									if i == 0 and j == 0:
										br, bg, bb = color
									if br != r or bg != b or bb != b:
										image.putpixel(xy, (nr, ng, nb))
						image.save(npath + file_name)
		print("------end-----")
	# 把16进制转换为rgb
	@classmethod
	def hex2rgb(self, hexcolor):
		rgb = ((hexcolor >> 16) & 0xff,
			   (hexcolor >> 8) & 0xff,
			   hexcolor & 0xff
			   )
		return rgb

if __name__ == '__main__':
	# hexColor = int(input("请输入新16进制颜色值："), 16)
	hexColor = int("0x1A86D5", 16)
	ChangeImageColor.startHandle(ChangeImageColor.hex2rgb(hexColor))


