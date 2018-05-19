import cv2


def rescale_img(img, dims=None, width=1024):
	"""Rescale image, either to the dimensions provided or to the width
	provided, returning the image and it's dimensions

	:param img:
		The input image
	:type img:
		numpy.ndarray
	:param dims:
		Provide this parameter to fit the image to a specific size
	:type dims:
		Tuple[int, int]
	:param width:
		The width to resize the image to, (overridden by dims) deafualts to 1024
	:type width:
		int
	:return:
		Tuple of image and its dimensions
	:rtype:
		Tuple[numpy.ndarray, Tuple[int, int]]
	"""
	grey = img
	if dims is None:
		r = float(width) / grey.shape[1]
		dims = (width, int(grey.shape[0] * r))
	else:
		dims = dims[::-1]
	scale = (dims[1] / float(grey.shape[0]), dims[0] / float(grey.shape[1]))
	return cv2.resize(grey, dims, interpolation=cv2.INTER_AREA), scale
