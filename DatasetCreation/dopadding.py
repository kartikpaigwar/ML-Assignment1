import cv2
#from matplotlib import pyplot as plt
import os
import glob

desired_size = 40

im_pth = "./positives1"
os.chdir(im_pth)
images = glob.glob("*.JPG")


for img in images:
	im1 = cv2.imread(img)
	old_size = im1.shape[:2] # old_size is in (height, width) format
	ratio = float(desired_size)/max(old_size)
	new_size = tuple([int(x*ratio) for x in old_size])	# new_size should be in (width, height) format

	im = cv2.resize(im1, (new_size[1], new_size[0]), interpolation = cv2.INTER_AREA)

	delta_w = desired_size - new_size[1]
	delta_h = desired_size - new_size[0]
	top, bottom = delta_h//2, delta_h-(delta_h//2)
	left, right = delta_w//2, delta_w-(delta_w//2)

	color = [0, 0, 0]
	new_im = cv2.copyMakeBorder(im, top, bottom, left, right, cv2.BORDER_CONSTANT, value=color)

	new_path = "/home/s/skylark/negatives_2/" + img
	cv2.imwrite(new_path, new_im)

'''
plt.subplot(231),plt.imshow(im,'gray'),plt.title('ORIGINAL')
plt.subplot(233),plt.imshow(new_im,'gray'),plt.title('NEW')
plt.show()

'''
# print(new_im)
# print(im1)
cv2.imshow("image", new_im)
cv2.imshow("image1", im1)
cv2.waitKey(0)
cv2.destroyAllWindows()