# question 1:
import pandas as pd
import cv2
import numpy as np
import matplotlib.image as mpimg
import numpy as np  # type: ignore
arr1 = np.arange(0, 10, 1)
print(arr1)

# -----------------------------------------------
# question 2:
arr = np.ones((3, 3)) > 0
print(arr)

arr = np.ones((3, 3), dtype=bool)
print(arr)

arr = np.full((3, 3), fill_value=True, dtype=bool)
print(arr)

# -----------------------------------------------
# question 3:
arr = np.arange(0, 10)
print(arr[arr % 2 == 1])

# -----------------------------------------------
# question 4:
arr = np.arange(0, 10)
arr[arr % 2 == 1] = -1
print(arr)

# -----------------------------------------------
# question 5:
arr5 = np.arange(10)
arr_2d = arr5.reshape(2, -1)
print(arr_2d)

# -----------------------------------------------
# question 6:
arr1 = np.arange(0, 10).reshape(2, -1)
arr2 = np.repeat(1, 10).reshape(2, -1)
arr = np.concatenate((arr1, arr2), axis=0)
print(arr)

# -----------------------------------------------
# question 7:
arr1 = np.arange(0, 10).reshape(2, -1)
arr2 = np.repeat(1, 10).reshape(2, -1)
arr = np.concatenate((arr1, arr2), axis=1)
print('C:\n', arr)

# -----------------------------------------------
# question 8:
arr9 = np.array([1, 2, 3])
arr10 = np.repeat(arr9, 3)
print(arr10)
print()
print(np.tile(arr9, 3))

# -----------------------------------------------
# question 9:
a = np.array([2, 6, 1, 9, 10, 3, 27])
index = np.nonzero((a >= 5) & (a <= 10))[0]
print("result:", a[index])

# -----------------------------------------------
# question 10:


def maxx(x, y):
    if x > y:
        return x
    else:
        return y


a = np.array([5, 7, 9, 8, 6, 4, 5])
b = np.array([6, 3, 4, 8, 9, 7, 1])
pair_max = np.vectorize(maxx, otypes=[float])
print(pair_max(a, b))
print(np.where(a < b, b, a))

# -----------------------------------------------
# question 12:
# download ảnh
'''!gdown 1i9dqan21DjQoG5Q_VEvm0LrVwAlXD0vB'''
img = mpimg.imread('/content/dog.jpeg')


def gray_scale(img):
    max_color = np.apply_along_axis(np.max, 2, img)
    min_color = np.apply_along_axis(np.min, 2, img)

    # tính giá trị trung bình max và min
    ave_color = (max_color + min_color) / 2
    return ave_color


gray_img = gray_scale(img)
print(gray_img[0, 0])

# -----------------------------------------------
# question 13:


def gray_scale(img):
    ave_color = np.apply_along_axis(np.mean, 2, img)
    return ave_color


gray_img = gray_scale(img)
print(gray_img[0, 0])
# -----------------------------------------------
# question 14:


def color2grayscale(vector):
    return vector[0]*0.21 + vector[1]*0.72 + vector[2]*0.07


def gray_scale(img):
    grayscale_image = np.apply_along_axis(color2grayscale, axis=2, arr=img)
    return grayscale_image


gray_img = gray_scale(img)
print(gray_img[0, 0])

# -----------------------------------------------
# question 15:
# download data
'''! gdown 1iA0WmVfW88HyJvTBSQDI5vesf-pgKabq'''
df = pd.read_csv('/content/advertising.csv')
data = df. to_numpy()

max_data = data[:, 3].max()
# sử dụng hàm where để trả về giá trị index
index = np.nonzero(data[:, 3] == max_data)[0][0]
print(f'max: {max_data}, index: {index}')

# -----------------------------------------------
# question 16:
mean_data = data[:, 0].mean()
print(mean_data)

# -----------------------------------------------
# question 17:
sales = data[:, 3]
sales_cond = np.nonzero(sales >= 20)[0]
print(len(sales_cond))

# -----------------------------------------------
# question 18:
radio = data[:, 1]
sales = data[:, 3]
sales_cond = np.nonzero(sales >= 15)[0]

mean_radio = np.mean(radio[sales_cond])
print(mean_radio)

# -----------------------------------------------
# question 19:
newspaper = data[:, 2]
sales = data[:, 3]
mean_newspaper = np.mean(newspaper)

sales_cond = np.nonzero(newspaper >= mean_newspaper)[0]
sales_sum = sales[sales_cond].sum()
print(sales_sum)

# -----------------------------------------------
# question 20:
sales = data[:, 3]
mean_sales = np.mean(sales)
new_sales = np.where(sales > mean_sales, 'Good', sales)
new_sales = np.where(sales == mean_sales, 'Average', new_sales)
new_sales = np.where(sales < mean_sales, 'Bad', new_sales)
print(new_sales[7:10])

# -----------------------------------------------
# question 21:
sales = data[:, 3]
mean_sales = np.mean(sales)
min_index = np.argmin(abs(sales - mean_sales))
print(f'min index, value are: {min_index}, {sales[min_index]}')
print('mean value is:', mean_sales)
new_sales = np.where(sales > sales[min_index], 'Good', sales)
new_sales = np.where(sales == sales[min_index], 'Average', new_sales)
new_sales = np.where(sales < sales[min_index], 'Bad', new_sales)
print(new_sales[7:10])
