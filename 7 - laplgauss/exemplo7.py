import cv2
import numpy as np

def printmask(m):
    for i in range(m.shape[0]):
        for j in range(m.shape[1]):
            print(m[i, j], end=",")
        print()

def main():
    cap = cv2.VideoCapture(0)
    media = np.array([0.1111, 0.1111, 0.1111, 0.1111, 0.1111, 0.1111, 0.1111, 0.1111, 0.1111], dtype=np.float32)
    gauss = np.array([0.0625, 0.125, 0.0625, 0.125, 0.25, 0.125, 0.0625, 0.125, 0.0625], dtype=np.float32)
    horizontal = np.array([-1, 0, 1, -2, 0, 2, -1, 0, 1], dtype=np.float32)
    vertical = np.array([-1, -2, -1, 0, 0, 0, 1, 2, 1], dtype=np.float32)
    laplacian = np.array([0, -1, 0, -1, 4, -1, 0, -1, 0], dtype=np.float32)
    boost = np.array([0, -1, 0, -1, 5.2, -1, 0, -1, 0], dtype=np.float32)
    laplgauss = np.array([0, 0, -1, 0, 0, 0, -1, -2, -1, 0, -1, -2, 16, -2, -1, 0, -1, -2, -1, 0, 0, 0, -1, 0, 0], dtype=np.float32)

    if not cap.isOpened():
        print("Câmeras indisponíveis")
        return -1

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    print("largura =", width)
    print("altura =", height)
    print("fps =", cap.get(cv2.CAP_PROP_FPS))
    print("formato =", cap.get(cv2.CAP_PROP_FORMAT))

    cv2.namedWindow("filtroespacial", cv2.WINDOW_NORMAL)
    cv2.namedWindow("original", cv2.WINDOW_NORMAL)

    mask = np.zeros((3, 3), dtype=np.float32)
    absolut = 1

    while True:
        ret, frame = cap.read()
        framegray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        framegray = cv2.flip(framegray, 1)
        cv2.imshow("original", framegray)

        frame32f = framegray.astype(np.float32)
        frameFiltered = cv2.filter2D(frame32f, -1, mask, anchor=(1, 1), delta=0)

        if absolut:
            frameFiltered = np.abs(frameFiltered)

        result = frameFiltered.astype(np.uint8)

        cv2.imshow("filtroespacial", result)

        key = cv2.waitKey(10)
        if key == 27:
            break  # Esc pressed!
        elif key == ord('a'):
            absolut = not absolut
        elif key == ord('m'):
            mask = np.reshape(media, (3, 3))
            printmask(mask)
        elif key == ord('g'):
            mask = np.reshape(gauss, (3, 3))
            printmask(mask)
        elif key == ord('h'):
            mask = np.reshape(horizontal, (3, 3))
            printmask(mask)
        elif key == ord('v'):
            mask = np.reshape(vertical, (3, 3))
            printmask(mask)
        elif key == ord('l'):
            mask = np.reshape(laplacian, (3, 3))
            printmask(mask)
        elif key == ord('p'):
            mask = np.reshape(laplgauss, (5, 5))
            printmask(mask)
        elif key == ord('b'):
            mask = np.reshape(boost, (3, 3))

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
