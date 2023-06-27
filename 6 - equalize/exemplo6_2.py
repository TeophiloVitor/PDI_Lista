import cv2

def histograma(imagem, bins):
    hist = cv2.calcHist([imagem], [0], None, [bins], [0, 256])
    return hist

def main():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Câmeras indisponíveis")
        return

    ret, imagem = cap.read()
    hist_novo = histograma(imagem, 256)
    hist_anterior = hist_novo.copy()
    temp = 0

    while True:
        ret, imagem = cap.read()
        imagem_gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
        hist_novo = histograma(imagem_gray, 256)

        compara = cv2.compareHist(hist_novo, hist_anterior, cv2.HISTCMP_CORREL)

        if compara <= 0.93:  # Altere o valor de comparação conforme necessário
            print("Movimento detectado - Ordem:", temp)
            temp += 1

        cv2.imshow("Detector de Movimento", imagem)
        
        if cv2.waitKey(1) == ord('q'):  # Pressione 'q' para sair
            break

        hist_anterior = hist_novo.copy()

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
