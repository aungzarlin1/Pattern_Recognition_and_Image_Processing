import cv2
import numpy as np

# crete black image
img = np.zeros((480, 640, 3), np.uint8)  

# draw is dictionary with key is draw type and 
# line and rectangle,value is start point, end point, color and thickness
# for circle, value is center coordinates, radius, color and thickness
# for text, value is text, org, font, fontScale, color, thickness, lineType
draw = {"line": [(0,0), (640, 480), (0, 255, 0), 2], 
        "rectangle" : [(0,0), (320, 380), (0, 0, 255), 2],
        "circle" : [(400, 100), 50, (255, 255, 0), 4],
        "text" : ["OPENCV", (320, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 4, cv2.LINE_AA]}

# draw a line
img = cv2.line(img, draw['line'][0], draw['line'][1], draw['line'][2], draw['line'][3])

# draw a rectangle
img = cv2.rectangle(img, draw['rectangle'][0], draw['rectangle'][1], draw['rectangle'][2], draw['rectangle'][3])

# draw a circle
img = cv2.circle(img, draw['circle'][0], draw['circle'][1], draw['circle'][2], draw['circle'][3])

# draw a text
img = cv2.putText(img, draw['text'][0], draw['text'][1], draw['text'][2], draw['text'][3], draw['text'][4], draw['text'][5], draw['text'][6])


# shoow image
cv2.imshow("image from numpy", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('Resources/lab3_1.jpg', img)
