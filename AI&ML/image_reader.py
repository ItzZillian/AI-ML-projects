import cv2
path1 = r"C:\Users\divis\OneDrive\Desktop\testing.jpg"
img = cv2.imread(path1, cv2.IMREAD_INCREASED_GRAYSCALE_2)

cv2.imshow('Anime', img)
cv2.waitKey(1000)
cv2.destroyAllWindows()