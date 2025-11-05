#getting and setting

from __future__ import print_function
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
                help= "Path to folder")

args = vars(ap.parse_args())

image = cv2.imread(args["image"])

cv2.imshow("Original", image)

cv2.waitKey(0)

cv2.destroyAllWindows()

(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - Red: {}, Green {}, Blue {}".format(r, g, b))

image[0, 0] = (0, 0, 225)
(b, g, r) = image [0, 0]
print ("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))


cv2.imshow("TopcornerRed", image)

cv2.waitKey(0)

cv2.destroyAllWindows()

corner = image[0:100, 0:100]
cv2.imshow("corner", corner)
cv2.waitKey(0)

image[0:100, 0:100] = (0, 255, 0)

cv2.imshow("updated", image)
cv2.waitKey(0)
