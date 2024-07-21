import numpy as np
import cv2
import matplotlib.pyplot as plt

# đưa ảnh vào, đổi hệ màu, thay đổi kích thước của ảnh
bg = cv2.imread('picture/background.jpg', 1)
bg = cv2.cvtColor(bg, cv2.COLOR_BGR2RGB)
bg = cv2.resize(bg, (1920, 2560))
fg = cv2.imread('picture/forceground.jpg', 1)
fg = cv2.cvtColor(fg, cv2.COLOR_BGR2RGB)
fg = cv2.resize(fg, (1920, 2560))
obj = cv2.imread('picture/object.jpg', 1)
obj = cv2.cvtColor(obj, cv2.COLOR_BGR2RGB)
obj = cv2.resize(obj, (1920, 2560))

# lấy hai ảnh có trừ cho nhau (ảnh có vật, và ảnh background ban đầu)
diff_img = cv2.absdiff(fg, obj)

# tạo thành ảnh xám (1 channel)
difference_gray = np.apply_along_axis(np.mean,  axis=-1, arr=diff_img)

# chuyển đổi nhị phân, những giá trị nào >255 sẽ chuyển thành 255, ngược lại là 0
# binary_threshold = cv2.threshold(difference_gray, 55, 255, cv2.THRESH_BINARY)[1]
binary_threshold = np.where(difference_gray > 55, 255, 0)


# ----chuyển ảnh xám 1 kênh màu, thành ảnh xám 3 kênh màu------
# (gray_image,) là một tuple
# => (gray_image,)*3 = (gray_image, gray_image, gray_image)
# stack: xếp chồng 3 mảng theo trục axis = 2

gray_image_3_channel = np.stack((binary_threshold,)*3, axis=-1)

# nếu không dùng tuple mà để là "gray_image * 3"
# thì đây sẽ là ma trận nhân với hệ số 3 => sai mục đích
# ---------------------------------------
output=np.where(gray_image_3_channel==0,bg,obj)
plt.imshow(output)
plt.show()
#---- tạo một ảnh mới trong folder____
output = cv2.cvtColor(output, cv2.COLOR_RGB2BGR)
cv2.imwrite('output.jpg',output)
