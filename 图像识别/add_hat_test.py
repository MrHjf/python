import cv2
import numpy as np
import dlib

# img目标图， 添加图
def add_hat(img, hat_img):
	r,g,b,a = cv2.split(hat_img)
	rgb_hat = cv2.merge((r,g,b))
	cv2.imwrite("images/hat_alpha.jpg", a)

	# dbli人脸关键点检测器
	predictor_path = "shape_predictor_5_face_landmarks.dat"
	predictor = dlib.shape_predictor(predictor_path)

	# dlib正脸检测器
	detector = dlib.get_frontal_face_detector()

	# 正脸检测
	dets = detector(img, 1)

	print(dets)
	return rgb_hat

# 读取帽子图， 第二个参数表示读取的rgba还是rgb通道
hat_img = cv2.imread("images/hat2.png", -1)

img = cv2.imread("images/test.jpg")
output = add_hat(img, hat_img)

cv2.imshow("output", output)
cv2.waitKey(0)
cv2.imwrite("./images/output.jpg", output)

cv2.destroyAllWindows()

