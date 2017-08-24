import cv2

# Implemented based on this: https://github.com/Venkatesh-GitTest/opencv_contrib/blob/e159befdf0c6a66ff46234b4577411202977a67b/modules/ximgproc/src/ridgedetectionfilter.cpp

class RidgeDetection(object):
	@classmethod
	def getSobelX(cls, img):
		return cv2.Sobel(img, cv2.CV_32F, 1, 0, ksize=3)

	@classmethod
	def getSobelY(cls, img):
		return cv2.Sobel(img, cv2.CV_32F, 0, 1, ksize=3)

	@classmethod
	def getRidges(cls, img):
		sbx = cls.getSobelX(img)
		sby = cls.getSobelY(img)
		sbxx = cls.getSobelX(sbx)
		sbyy = cls.getSobelY(sby)
		sbxy = cls.getSobelY(sbx)
		sb2xx = sbxx * sbxx
		sb2yy = sbyy * sbyy
		sb2xy = sbxy * sbxy
		sbxxyy = sbxx * sbyy
		rootex = (sb2xx + (sb2xy + sb2xy + sb2xy + sb2xy) - (sbxxyy + sbxxyy) + sb2yy)
		root = np.sqrt(rootex)
		ridgexp = (sbxx + sbyy) + root
		ridges = ridgexp / 2
		return ridges
