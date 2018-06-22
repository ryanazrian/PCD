import numpy as np
import cv2
import kumpulanKode as libs
import object_size as size
import glob

images = sorted(glob.glob('tomat/*.JPG'))
kernel = np.ones((5,5), np.uint8)
i= 1
j = 1

csv = open("mytomat.csv", "w")

#header = 'nama_file, red_avg, green_avg, blue_avg, h_avg, s_avg, v_avg'
#header = header +'\n'
#csv.write(header)

for tomat in images:
	img = cv2.imread(tomat)
	red = 0
	blue = 0
	green = 0
	
	hue = 0
	sat = 0
	val = 0

	ha=0
	sa=0
	va=0

	re = 0
	gr = 0
	bl  = 0
	
	hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
	gray = cv2.cvtColor(hsv, cv2.COLOR_RGB2GRAY)
	
	#img = cv2.resize(img, (0, 0), fx=0.1, fy=0.1)
	#b, g, r = cv2.split()
	#b = libs.treshold(libs.substract(r, g))
	ret, b = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
	
	dilate = cv2.dilate(b, kernel, iterations = 10)
	final = cv2.erode(dilate, kernel, iterations= 10)
	hasil = libs.subrgbgray(img, final)
	
	row, col, ch  = hasil.shape
	for x in range (0, row):
		for y in range (0, col):
			b, g, r = hasil[x, y]
			if(b & g & r):
				red = red + r
				green = green + g
				blue = blue +b

				if(b):
					bl = bl+ 1
				if(r):
					re = re + 1
				if(g):
					gr = gr +1
	red = red / re
	green = green/ gr
	blue = blue / bl
	jumlah_frek =  re + gr +bl

	HSV = cv2.cvtColor(hasil, cv2.COLOR_RGB2HSV)
	row, col, ch = HSV.shape
	for x in range (0, row):
		for y in range (0, col):
			h, s, v = HSV[x, y]
			if(h & s & v):
				hue = hue + h
				sat = sat + s
				val = val + v
				
				if(h):
					ha = ha+1
				if(s):
					sa = sa+1
				if(v):
					va = va+1

	hue = hue / ha
	sat = sat / sa
	val = val / va

	#ambil ukuran
	panjang = 0
	lebar = 0
	float(panjang)
	float(lebar)
	panjang, lebar = size.cari_size(hasil)

			
	print('Hasil1/%d/%d_%d.jpg' %(i, i, j))
	name = 'Hasil1/%d/%d_%d.jpg' %(i, i, j)
	
	myTomat = '%s, %d, %d, %d, %d, %d, %d, %d, %s' %(name, red, green, blue, hue, sat, val, jumlah_frek, panjang)
	myTomat = myTomat + '\n'
	#print(myTomat)
	csv.write(myTomat)
	
	
	#cv2.imwrite(name, hasil)
	if(j == 15) :
		i = i + 1
		j = 0
	j = j + 1
	#name = '%s' %(tomat)
	#cv2.imwrite(name, img)
	#print(name)
