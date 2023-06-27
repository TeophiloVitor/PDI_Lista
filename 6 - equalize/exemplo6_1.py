import cv2

def main():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Câmeras indisponíveis")
        return

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        equalized = cv2.equalizeHist(grayscale)

        cv2.namedWindow("normal", cv2.WINDOW_NORMAL)
        cv2.namedWindow("equalizada", cv2.WINDOW_NORMAL)

        cv2.imshow("normal", grayscale)
        cv2.imshow("equalizada", equalized)

        cv2.imwrite("frame_normal.png", grayscale)
        cv2.imwrite("frame_equalizada.png", equalized)

        key = cv2.waitKey(30)
        if key == 27:  # Pressione Esc para sair
            break

    cv2.destroyAllWindows()
    cap.release()

if __name__ == "__main__":
    main()
