# 导入需要的库
import cv2
import numpy as np
import matplotlib.pyplot as plt

# ====================== 任务1：使用OpenCV读取测试图片 ======================
img = cv2.imread("test.jpg")  # 读取当前目录下的test.jpg
if img is None:
    print("❌ 错误：未找到 test.jpg 图片，请确认图片在当前目录！")
else:
    print("✅ 任务1：图片读取成功！")

# ====================== 任务2：输出图像基本信息 ======================
height, width = img.shape[:2]  # 提取图片高度、宽度
channels = img.shape[2] if len(img.shape) == 3 else 1  # 提取通道数（彩色=3，灰度=1）
dtype = img.dtype  # 提取像素数据类型
print("\n✅ 任务2：图像基本信息：")
print(f"  宽度：{width} 像素")
print(f"  高度：{height} 像素")
print(f"  通道数：{channels}")
print(f"  像素数据类型：{dtype}")

# ====================== 任务3：显示原图（Matplotlib） ======================
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # OpenCV读取是BGR，Matplotlib需要转RGB才不会颜色失真
plt.figure("原图")
plt.imshow(img_rgb)
plt.axis("off")  # 隐藏坐标轴，让图片更干净
plt.title("Original Image")
plt.savefig("original_image.png")  # 保存原图到当前目录（WSL没配置图形界面时，用保存文件查看）
print("\n✅ 任务3：原图已保存为 original_image.png，可在Windows中打开查看")

# ====================== 任务4：转换为灰度图并显示 ======================
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 彩色转灰度
plt.figure("灰度图")
plt.imshow(gray_img, cmap="gray")  # cmap="gray" 表示用灰度模式显示
plt.axis("off")
plt.title("Gray Image")
plt.savefig("gray_image.png")  # 保存灰度图
print("\n✅ 任务4：灰度图已保存为 gray_image.png，可在Windows中打开查看")

# ====================== 任务5：保存灰度图为新文件 ======================
cv2.imwrite("gray_test.jpg", gray_img)  # 用OpenCV保存灰度图为jpg格式
print("\n✅ 任务5：灰度图已保存为 gray_test.jpg（OpenCV格式）")

# ====================== 任务6：NumPy简单操作 ======================
# 1. 输出坐标(100,100)的像素值（注意：OpenCV坐标是(行,列) = (高度y, 宽度x)）
pixel_value = img[100, 100]
print(f"\n✅ 任务6：坐标(100,100)的BGR像素值：{pixel_value}")

# 2. 裁剪左上角100x100区域（NumPy切片：[y_start:y_end, x_start:x_end]）
crop_img = img[0:100, 0:100]
cv2.imwrite("crop_top_left.jpg", crop_img)  # 保存裁剪后的图片
print("✅ 任务6：左上角100x100区域裁剪图已保存为 crop_top_left.jpg")

# 显示所有图片（如果WSL配置了VcXsrv图形界面，可取消下面注释弹出窗口；否则看保存的文件即可）
# plt.show()

