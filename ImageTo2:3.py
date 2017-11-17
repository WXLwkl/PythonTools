#!/usr/bin/env python
# coding: utf-8
import sys, os

try:
	from PIL import Image
except:
	print('\033[31m' + '缺少Image模块，正在安装Image模块，请等待...' + '\033[0m')
	success = os.system('pip3 install Pillow')
	if success == 0:
		print('\033[7;32m' + 'Image模块安装成功.' + '\033[0m')
		from PIL import Image
	else:
		print('\033[31m' + 'Image安装失败，请手动在终端执行：\'pip3 install Pillow\'重新安装.' + '\033[0m')
		quit()


if len(sys.argv) <= 1:
	print('\033[31m' + '请输入图片路径,eg: python autoExportAppIcon.py /path/xxx.png' + '\033[1m')
	quit()


ImageName = sys.argv[1]
# ImageName = '/Users/xingl/Desktop/AppIcon/button.png'
fileName = os.path.basename(ImageName)
folderName = os.path.splitext(fileName)[0]
# print('--->',os.path.basename(ImageName))
print('图片名字为：' + ImageName)
originImg = ''
try:
	originImg = Image.open(ImageName)
	# print(originImg.format, originImg.size, originImg.mode)
except:
	print('\033[31m' + '\'' + ImageName + '\'' + '，该文件不是图片文件，请检查文件路径.' + '\033[0m')
	quit()

# 输出路径
outPutPath = os.path.expanduser('~') + '/Desktop/%s/' % folderName
if not os.path.exists(outPutPath):
	os.mkdir(outPutPath)


w, h = originImg.size
print('Original image size: %s*%s' % (w, h))

img2x = originImg.resize(( w*2//3,h*2//3),Image.ANTIALIAS)
img3x = originImg.resize((w,h),Image.ANTIALIAS)
img2x.save(outPutPath + '%s@2x.png' % folderName,"png")
img3x.save(outPutPath + '%s@3x.png' % folderName,"png")

fileName2 = '%s@2x.png' % folderName
fileName3 = '%s@3x.png' % folderName

# 创建Contents.json文件
content = '''
{
  "images" : [
    {
      "idiom" : "iphone",
      "scale" : "1x"
    },
    {
      "idiom" : "iphone",
      "filename" : %s,
      "scale" : "2x"
    },
    {
      "idiom" : "iphone",
      "filename" : %s,
      "scale" : "3x"
    }
  ],
  "info" : {
    "version" : 1,
    "author" : "xcode"
  }
}
''' % (fileName2, fileName3)

f = open(outPutPath + 'Contents.json', 'w')
f.write(content)

print('\033[7;32m' + '文件输出文件夹：' + outPutPath + '\033[0m')
os.system('open ' + outPutPath)
