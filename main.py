import cv2
import numpy as np
import os

IMG_PATH = "mangga.jpg"
OUTPUT_DIR = "hasil"

os.makedirs(OUTPUT_DIR, exist_ok=True)

# =====================================================
# LOAD IMAGE
# =====================================================
img = cv2.imread(IMG_PATH)
if img is None:
    raise FileNotFoundError("mangga.jpg tidak ditemukan!")

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imwrite(os.path.join(OUTPUT_DIR, "original.png"), img)

# =====================================================
# PREPROCESSING
# =====================================================
gaussian = cv2.GaussianBlur(img_rgb, (7, 7), 0)
median = cv2.medianBlur(img_rgb, 7)
bilateral = cv2.bilateralFilter(img_rgb, 9, 75, 75)

cv2.imwrite(os.path.join(OUTPUT_DIR, "gaussian.png"), cv2.cvtColor(gaussian, cv2.COLOR_RGB2BGR))
cv2.imwrite(os.path.join(OUTPUT_DIR, "median.png"), cv2.cvtColor(median, cv2.COLOR_RGB2BGR))
cv2.imwrite(os.path.join(OUTPUT_DIR, "bilateral.png"), cv2.cvtColor(bilateral, cv2.COLOR_RGB2BGR))

# =====================================================
# SEGMENTASI HSV
# =====================================================
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower = np.array([5, 80, 80])
upper = np.array([35, 255, 255])

mask_hsv = cv2.inRange(img_hsv, lower, upper)
segmented_hsv = cv2.bitwise_and(img_rgb, img_rgb, mask=mask_hsv)

cv2.imwrite(os.path.join(OUTPUT_DIR, "mask_hsv.png"), mask_hsv)
cv2.imwrite(os.path.join(OUTPUT_DIR, "segment_hsv.png"),
            cv2.cvtColor(segmented_hsv, cv2.COLOR_RGB2BGR))

# =====================================================
# SEGMENTASI K-MEANS
# =====================================================
Z = img_rgb.reshape((-1, 3))
Z = np.float32(Z)

K = 3
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
_, labels, centers = cv2.kmeans(Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
centers = np.uint8(centers)
segmented_image = centers[labels.flatten()].reshape(img_rgb.shape)

cluster_scores = centers[:, 0] + centers[:, 1]
target_cluster = np.argmax(cluster_scores)

mask_kmeans = (labels.flatten() == target_cluster).astype(np.uint8) * 255
mask_kmeans = mask_kmeans.reshape(img_rgb.shape[:2])
segmented_kmeans = cv2.bitwise_and(img_rgb, img_rgb, mask=mask_kmeans)

cv2.imwrite(os.path.join(OUTPUT_DIR, "mask_kmeans.png"), mask_kmeans)
cv2.imwrite(os.path.join(OUTPUT_DIR, "segment_kmeans.png"),
            cv2.cvtColor(segmented_kmeans, cv2.COLOR_RGB2BGR))

print("\n[INFO] Semua hasil preprocessing & segmentasi sudah disimpan ke folder 'hasil/'.")
