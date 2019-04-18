# -*- coding:utf-8 -*-
import cv2
import matplotlib.pyplot as plt
import numpy as np


def seg_kmeans_gray():
    # 读取图片
    img = cv2.imread('pic.jpg', cv2.IMREAD_GRAYSCALE)

    # 展平
    img_flat = img.reshape((img.shape[0] * img.shape[1], 1))
    img_flat = np.float32(img_flat)

    # 迭代参数
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TermCriteria_MAX_ITER, 20, 0.5)
    flags = cv2.KMEANS_RANDOM_CENTERS

    # 进行聚类
    compactness, labels, centers = cv2.kmeans(img_flat, 2, None, criteria, 10, flags)

    # 显示结果
    img_output = labels.reshape((img.shape[0], img.shape[1]))
    plt.subplot(121), plt.imshow(img, 'gray'), plt.title('input')
    plt.subplot(122), plt.imshow(img_output, 'gray'), plt.title('kmeans')
    plt.show()


if __name__ == '__main__':
    seg_kmeans_gray()