import cv2

path = r'C:\Users\Aung Zar Lin\OneDrive\Desktop\Pattern Recognition and Image Processing\Lab01\Resources\sample-mp4-file.mp4'

cap = cv2.VideoCapture(path)

while(True):
    
    ret, frame = cap.read()

    cv2.imshow("Frames", frame)
        
    if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()

cv2.destroyAllWindows()