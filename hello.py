from sense_hat import SenseHat
from time import sleep
from random import choice
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import imutils

sense = SenseHat()

r = (255,255,255)
b = (0, 0, 0)
g = (20,218,0)
h = (170,250,29)
p = (174,25,202)
w = (17,232,225)
j = (12,135,255)
y = (12,135,255)
u = (255,171,33)
o = (255,0,5)

colorRanges=[
	((20,100,100), (30,255,255), "yellow")]

logo=[
	b,b,w,w,w,w,w,w,
	b,b,w,w,w,w,w,w,
	b,b,w,w,w,w,w,w,
	b,b,w,b,b,b,b,w,
	b,b,w,b,b,b,b,w,
	w,w,w,b,b,w,w,w,
	w,w,w,b,b,w,w,w,
	w,w,w,b,b,w,w,w
]

a_up=[
	b,b,b,o,o,b,b,b,
	b,b,o,r,r,o,b,b,
	b,o,r,r,r,r,o,b,
	o,r,r,r,r,r,r,o,
	o,o,o,r,r,o,o,o,
	b,b,o,r,r,o,b,b,
	b,b,o,r,r,o,b,b,
	b,b,o,o,o,o,b,b
]

a_up_g=[
	b,b,b,h,h,b,b,b,
	b,b,h,g,g,h,b,b,
	b,h,g,g,g,g,h,b,
	h,g,g,g,g,g,g,h,
	h,h,h,g,g,h,h,h,
	b,b,h,g,g,h,b,b,
	b,b,h,g,g,h,b,b,
	b,b,h,h,h,h,b,b,
]
 
a_down=[
	b,b,y,y,y,y,b,b,
	b,b,y,r,r,y,b,b,
	b,b,y,r,r,y,b,b,
	y,y,y,r,r,y,y,y,
	y,r,r,r,r,r,r,y,
	b,y,r,r,r,r,y,b,
	b,b,y,r,r,y,b,b,
	b,b,b,y,y,b,b,b
]

a_down_g=[
	b,b,h,h,h,h,b,b,
	b,b,h,g,g,h,b,b,
	b,b,h,g,g,h,b,b,
	h,h,h,g,g,h,h,h,
	h,g,g,g,g,g,g,h,
	b,h,g,g,g,g,h,b,
	b,b,h,g,g,h,b,b,
	b,b,b,h,h,b,b,b,
]

a_left=[
	b,b,b,u,u,b,b,b,
	b,b,u,r,u,b,b,b,
	b,u,r,r,u,u,u,u,
	u,r,r,r,r,r,r,u,
	u,r,r,r,r,r,r,u,
	b,u,r,r,u,u,u,u,
	b,b,u,r,u,b,b,b,
	b,b,b,u,u,b,b,b
]

a_left_g=[
	b,b,b,h,h,b,b,b,
	b,b,h,g,h,b,b,b,
	b,h,g,g,h,h,h,h,
	h,g,g,g,g,g,g,h,
	h,g,g,g,g,g,g,h,
	b,h,g,g,h,h,h,h,
	b,b,h,g,h,b,b,b,
	b,b,b,h,h,b,b,b,
]

a_right=[
	b,b,b,p,p,b,b,b,
	b,b,b,p,r,p,b,b,
	p,p,p,p,r,r,p,b,
	p,r,r,r,r,r,r,p,
	p,r,r,r,r,r,r,p,
	p,p,p,p,r,r,p,b,
	b,b,b,p,r,p,b,b,
	b,b,b,p,p,b,b,b,
]

a_right_g=[
	b,b,b,h,h,b,b,b,
	b,b,b,h,g,h,b,b,
	h,h,h,h,g,g,h,b,
	h,g,g,g,g,g,g,h,
	h,g,g,g,g,g,g,h,
	h,h,h,h,g,g,h,b,
	b,b,b,h,g,h,b,b,
	b,b,b,h,h,b,b,b,
]

pixels = [
    [255, 0, 0], [255, 0, 0], [255, 87, 0], [255, 196, 0], [205, 255, 0], [95, 255, 0], [0, 255, 13], [0, 255, 122],
    [255, 0, 0], [255, 96, 0], [255, 205, 0], [196, 255, 0], [87, 255, 0], [0, 255, 22], [0, 255, 131], [0, 255, 240],
    [255, 105, 0], [255, 214, 0], [187, 255, 0], [78, 255, 0], [0, 255, 30], [0, 255, 140], [0, 255, 248], [0, 152, 255],
    [255, 223, 0], [178, 255, 0], [70, 255, 0], [0, 255, 40], [0, 255, 148], [0, 253, 255], [0, 144, 255], [0, 34, 255],
    [170, 255, 0], [61, 255, 0], [0, 255, 48], [0, 255, 157], [0, 243, 255], [0, 134, 255], [0, 26, 255], [83, 0, 255],
    [52, 255, 0], [0, 255, 57], [0, 255, 166], [0, 235, 255], [0, 126, 255], [0, 17, 255], [92, 0, 255], [201, 0, 255],
    [0, 255, 66], [0, 255, 174], [0, 226, 255], [0, 117, 255], [0, 8, 255], [100, 0, 255], [210, 0, 255], [255, 0, 192],
    [0, 255, 183], [0, 217, 255], [0, 109, 255], [0, 0, 255], [110, 0, 255], [218, 0, 255], [255, 0, 183], [255, 0, 74]
]

arrows=[a_up,a_down,a_left,a_right]

pause=1
score=0
logo_var = 0

while logo_var < 1:
	sense.set_pixels(logo)
	for event in sense.stick.get_events():
		if event.direction == 'up':
			sense.clear()
			logo_var = 1
			break

camera = PiCamera()
camera.resolution = (640, 360)
rawCapture = PiRGBArray(camera, size=(640, 360))
camera.rotation = 180
camera.hflip = True
time.sleep(0.1)

def a_d():
	arrow=choice(arrows)
	return (arrow)
	
def change_direction():
	direction = a_d()
	sense.set_pixels(direction)
	return direction
	
def change_direction_color(direction):
	sense.set_pixels(direction)
	
def next_colour(pix):
				r = pix[0]
				g = pix[1]
				b = pix[2]

				if (r == 255 and g < 255 and b == 0):
					g += 1

				if (g == 255 and r > 0 and b == 0):
					r -= 1

				if (g == 255 and b < 255 and r == 0):
					b += 1

				if (b == 255 and g > 0 and r == 0):
					g -= 1

				if (b == 255 and r < 255 and g == 0):
					r += 1

				if (r == 255 and b > 0 and g == 0):
					b -= 1

				pix[0] = r
				pix[1] = g
				pix[2] = b

time_start=time.time()

display_dir = change_direction()

rainbow = 0
prevcX = 400
prevcY = 400
	
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	image = frame.array 
	images = cv2.GaussianBlur(image, (11,11), 0)
	hsv = cv2.cvtColor(images, cv2.COLOR_BGR2HSV)
    
	for (lower, upper, colorName) in colorRanges:
		mask = cv2.inRange(hsv, lower, upper)
		cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
			cv2.CHAIN_APPROX_SIMPLE)
		cnts = cnts[0] if imutils.is_cv2() else cnts[1]
 
		if len(cnts) > 0:
			c = max(cnts, key=cv2.contourArea)
			((x, y), radius) = cv2.minEnclosingCircle(c)
			M = cv2.moments(c)
			if M["m00"] == 0:
				continue
			(cX, cY) = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
			
			if radius > 10:
				cv2.circle(image, (int(x), int(y)), int(radius), (0, 255, 255), 2)
				cv2.putText(image, str(cX) + " , " + str(cY), (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,
					1.0, (0, 255, 255), 2)
					
				
				if cX - prevcX > 75 and display_dir == a_right:
					change_direction_color(a_right_g)
					score += 100
					sleep(1)
					display_dir = change_direction()
									
				if cX - prevcX < -75 and display_dir == a_left:
					change_direction_color(a_left_g)
					score += 100
					sleep(1)
					display_dir = change_direction()
					
					
				if cY - prevcY > 40 and display_dir == a_down:
					change_direction_color(a_down_g)
					score += 100
					sleep(1)
					display_dir = change_direction()
										
				if cY - prevcY < -40 and display_dir == a_up:
					change_direction_color(a_up_g)
					score += 100
					sleep(1)
					display_dir = change_direction()
									
				prevcX = cX
				prevcY = cY
	
	
	rawCapture.truncate(0) 				
	cv2.imshow("Mask",mask)
	cv2.imshow("Frame",image)
	key = cv2.waitKey(1) & 0xFF			
				
	if time.time() - time_start  > 60:
		sense.show_message("GAME OVER", text_colour=(220,2,2), scroll_speed=0.07)
		sense.show_message(str(score)) 
		print score
		if score >= 3700:
			
			msleep = lambda x: time.sleep(x / 1000.0)
			
			while rainbow < 2500:
				for pix in pixels:
					next_colour(pix)
					
						
				sense.set_pixels(pixels)
				msleep(2)
				rainbow += 1
				
		break

sense.clear()
cv2.destroyAllWindows()
