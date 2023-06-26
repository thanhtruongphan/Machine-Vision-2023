import cv2 as cv
import numpy as np

img = cv.imread('halloween.jpg', cv.IMREAD_COLOR)
# print('dạng biến của từng pixel ', img.dtype)

#%% Lấy dữ liệu của file hình
# print('so chieu data', img.ndim)
# print('tổng số pixel', img.size)
# print('số pixel trong từng dimension', img.shape)

# Chiều dài và chiều rộng của tấm hình
width = img.shape[1]
height = img.shape[0]

#%% Đọc và gán giá trị cho pixel
# print(' giá trị pixel tại cột 312, hàng 313 = ',img[4,3])
# img[4,3] = 255
# print(' giá trị pixel tại cột 312, hàng 313 = ',img[4,3])

#%% Example: Tạo hiệu ứng màn che cho tấm hình
out = np.zeros((height,width,3),dtype=np.uint8)

# vd1:
# for i in np.arange(height-1,-1,-1):
#     out[i,:,:] = img[i,:,:] 
#     cv.imshow('Halloween', out)
#     cv.waitKey(10)
# vd2: 
for i in np.arange(0,width,1):
    out[:,i,:] = img[:,i,:]
    cv.imshow('Halloween', out)
    cv.waitKey(10)

cv.destroyAllWindows()