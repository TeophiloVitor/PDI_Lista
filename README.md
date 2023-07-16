# 💡 Listas de exercícios de Processamento Digital de Imagens

## Discente
Teophilo Vitor de Carvalho Clemente | 20220080516  
Graduação em Engenharia da Computação - UFRN  
<teophilo.vitor.709@ufrn.edu.br>  

## Objetivo 
Neste repositório serão apresentados os códigos, resultados e explicações acerca dos exercícios desenvolvidos ao longo da disciplina de Processamento Digital de Imagens, os respectivos enunciados e material da disciplina podem ser encontrados na página do professor Dr. Agostinho [[Link]](https://agostinhobritojr.github.io/tutorial/pdi/). Os códigos foram desenvolvidos em Python juntamente com a biblioteca OpenCV, para isso converti os códigos disponibilizados pelo professor para Python e no discorrer desde README eles serão apresentados e explicados.

## Solução

Para rodar os códigos, é preciso ter Python instalado na sua máquina e a biblioteca OpenCV, em alguns casos foram utilizados outras biblioetecas especificadas em cada código. Contudo, a seguir serão apresentados os códigos, explicações e os respectivos resultados obtidos em cada um. Para melhor organização eles estão dividos em Parte I, II, III e IV como no tutotial do professor.

## Sumário

[[CAPÍTULO 2]](https://github.com/TeophiloVitor/PDI_Lista#-exerc%C3%ADcio-21)  

[[CAPÍTULO 3]](https://github.com/TeophiloVitor/PDI_Lista#-exerc%C3%ADcio-3)  

[[CAPÍTULO 4]](https://github.com/TeophiloVitor/PDI_Lista#-exerc%C3%ADcio-4)  

[[CAPÍTULO 5]](https://github.com/TeophiloVitor/PDI_Lista#-exerc%C3%ADcio-51)  

[[CAPÍTULO 6]](https://github.com/TeophiloVitor/PDI_Lista#-exerc%C3%ADcio-61)  

[[CAPÍTULO 7]](https://github.com/TeophiloVitor/PDI_Lista#-exerc%C3%ADcio-7)  

[[CAPÍTULO 8]](https://github.com/TeophiloVitor/PDI_Lista#-exerc%C3%ADcio-8)  

[[CAPÍTULO 9]](https://github.com/TeophiloVitor/PDI_Lista#-exerc%C3%ADcio-9)  

[[CAPÍTULO 11]](https://github.com/TeophiloVitor/PDI_Lista#-exerc%C3%ADcio-11)  

[[CAPÍTULO 12]](https://github.com/TeophiloVitor/PDI_Lista#-exerc%C3%ADcio-12)  

## 🔔 PARTE I

## 🔭 Exercício 2.1

Utilizando o programa exemplos/pixels.cpp como referência, implemente um programa regions.cpp. Esse programa deverá solicitar ao usuário as coordenadas de dois pontos P1 e P2 localizados dentro dos limites do tamanho da imagem e exibir que lhe for fornecida. Entretanto, a região definida pelo retângulo de vértices opostos definidos pelos pontos P1 e P2 será exibida com o negativo da imagem na região correspondente.

## Solução

Para resolver foram implementas entradas para o usuário escolher qual região ele queria deixar em negativo. Para deixar deixar a região em negativo foi feito um for para percorrer área escolhida e fazer a operação que faz com que o pixel da imagem se torne negativo, como mostrado no código a seguir:
```python
import cv2
import requests
import numpy as np
from io import BytesIO

def main():
    image_url = "https://agostinhobritojr.github.io/tutorial/pdi/figs/biel.png"

    response = requests.get(image_url)
    if response.status_code != 200:
        print("Erro ao fazer o download da imagem")
        return

    image = cv2.imdecode(np.frombuffer(response.content, np.uint8), cv2.IMREAD_GRAYSCALE)
    if image is None:
        print("Não foi possível ler a imagem")
        return

    p_1 = int(input("Informe o P1: "))
    p_2 = int(input("Informe o P2: "))

    width = image.shape[1]
    height = image.shape[0]
    print(f"{width}x{height}")

    if p_1 >= height:
        p_1 = height
    if p_2 >= width:
        p_2 = width

    for i in range(p_1, p_2):
        for j in range(p_1, p_2):
            image[i, j] = 255 - image[i, j]

    cv2.imshow("Janela", image)
    cv2.waitKey(0)

if __name__ == "__main__":
    main()
```
Entrada:  

<p align='center'><img src='./1 - regions/ebiel.png'></p>  
    
Saída:  

<p align='center'><img src='./1 - regions/resultex1.png'></p>  
    
## 🔭 Exercício 2.2

Utilizando o programa exemplos/pixels.cpp como referência, implemente um programa trocaregioes.cpp. Seu programa deverá trocar os quadrantes em diagonal na imagem. Explore o uso da classe Mat e seus construtores para criar as regiões que serão trocadas.

## Solução

Diferente do regions, esse agora não precisamos de interação com o usuário, é simplesmente manipulação da imagem. E para fazer isso feita a quebra da imagem para pegar pedaços e salva-los em uma imagem final com método copy para fazer a modificação na imagem atual, assim conseguindo modificar as áreas da imagem, como mostrado no código a seguir:
```python
import cv2
import requests
import numpy as np
from io import BytesIO

def main():
    image_url = "https://agostinhobritojr.github.io/tutorial/pdi/figs/biel.png"

    response = requests.get(image_url)
    if response.status_code != 200:
        print("Erro ao fazer o download da imagem")
        return

    image = cv2.imdecode(np.frombuffer(response.content, np.uint8), cv2.IMREAD_GRAYSCALE)
    if image is None:
        print("Não foi possível abrir a imagem")
        return

    cv2.namedWindow("janela", cv2.WINDOW_AUTOSIZE)

    width = image.shape[1]  # largura
    height = image.shape[0]  # altura

    image_aux = image[0:height // 2, 0:width // 2].copy()
    cv2.imwrite("biel_1.png", image_aux)

    image[0:height // 2, 0:width // 2] = image[height // 2:height, width // 2:width].copy()
    cv2.imwrite("biel_2.png", image)

    image[height // 2:height, width // 2:width] = image_aux.copy()
    cv2.imwrite("biel_3.png", image)

    image_aux = image[0:height // 2, width // 2:width].copy()
    cv2.imwrite("biel_4.png", image_aux)

    image[0:height // 2, width // 2:width] = image[height // 2:height, 0:width // 2].copy()
    cv2.imwrite("biel_5.png", image)

    image[height // 2:height, 0:width // 2] = image_aux.copy()
    cv2.imwrite("biel_6.png", image)

    cv2.imshow("janela", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
```
Entrada:  

<p align='center'><img src='./1 - regions/ebiel.png'></p>   
    
Saída:  

<p align='center'><img src='./2 - trocaregions/biel_6.png'></p> 

## 🔭 Exercício 3

Utilizando o programa filestorage.cpp como base, crie um programa que gere uma imagem de dimensões 256x256 pixels contendo uma senóide de 4 períodos com amplitude de 127 desenhada na horizontal, como aquela apresentada na Figura 6 do material. Grave a imagem no formato PNG e no formato YML. Compare os arquivos gerados, extraindo uma linha de cada imagem gravada e comparando a diferença entre elas. Trace um gráfico da diferença calculada ao longo da linha correspondente extraída nas imagens. O que você observa?

## Solução

Para resolver esse problema foram feitas algumas modificações no código original, como resultado disso e da diminuição do número de períodos usados, agora 4, vemos uma redução na amostragem e traços mais grossos na representação da senóide, fato esse também comprovado no arquivo YML, como mostrado no código a seguir:
```python
import cv2
import numpy as np
import math

SIDE = 256 # Dimensão da imagem (256x256 pixels)
PERIODOS = 4 # Número de períodos da senoide

# Criar uma matriz de zeros para a imagem
image = np.zeros((SIDE, SIDE), dtype=np.float32)

for i in range(SIDE):
    for j in range(SIDE):
        image[i, j] = 127 * math.sin(2 * math.pi * PERIODOS * j / SIDE) + 128

# Salvar a imagem em formato YML
ss_yml = f"senoide-{SIDE}.yml"
fs = cv2.FileStorage(ss_yml, cv2.FILE_STORAGE_WRITE)
fs.write("mat", image)
fs.release()

# Normalizar a imagem
image_normalized = cv2.normalize(image, None, 0, 255, cv2.NORM_MINMAX)

image_normalized_uint8 = image_normalized.astype(np.uint8)

# Salvar a imagem em formato PNG
ss_png = f"senoide-{SIDE}.png"
cv2.imwrite(ss_png, image_normalized_uint8)

# Exibir a imagem
cv2.imshow("Senoide", image_normalized_uint8)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
Saídas:  

<p align='center'><img src='./3 - senoide/senoideatt.png'></p>   
    
[[Link arquivo YML]](https://github.com/TeophiloVitor/PDI_Lista/blob/main/3%20-%20senoide/senoideatt.yml)

## 🔭 Exercício 4

Usando o programa esteg-encode.cpp como referência para esteganografia, escreva um programa que recupere a imagem codificada de uma imagem resultante de esteganografia. Lembre-se que os bits menos significativos dos pixels da imagem fornecida deverão compor os bits mais significativos dos pixels da imagem recuperada. O programa deve receber como parâmetros de linha de comando o nome da imagem resultante da esteganografia.

## Solução

Para resolver esse problema for montada a estrutura para receber a imagem portadora, em seguida é criada uma matriz de zeros para a imagem que vamos recuperar e após a fazemos uma estrutura de for aninhado para percorrer a imagem portadora e obter a imagem recuperada a cada interação, como mostrado no código a seguir:
```python
import cv2
import numpy as np
import sys

nbits = 3

def recover_image():
    # Verificar se o nome do arquivo de imagem foi fornecido como argumento de linha de comando
    if len(sys.argv) < 2:
        sys.exit(1)

    # Carregar a imagem resultante da esteganografia
    imagem_resultante = cv2.imread(sys.argv[1], cv2.IMREAD_COLOR)

    if imagem_resultante is None:
        print("Não foi possível carregar a imagem resultante da esteganografia.")
        sys.exit(1)

    # Criar uma matriz de zeros para a imagem recuperada
    imagem_recuperada = np.zeros_like(imagem_resultante)

    for i in range(imagem_resultante.shape[0]):
        for j in range(imagem_resultante.shape[1]):
            val_resultante = imagem_resultante[i, j]
            val_recuperada = np.zeros(3, dtype=np.uint8)

            for k in range(3):
                val_recuperada[k] = val_resultante[k] << (8 - nbits) & 0xFF

            imagem_recuperada[i, j] = val_recuperada

    filename = 'imagem_final.png'

    cv2.imwrite(filename, imagem_recuperada)
    # Exibir a imagem recuperada
    cv2.imshow("Imagem Final", imagem_recuperada)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    recover_image()
```
Entrada:  

<p align='center'><img src='./4 - esteganografia/esteno.png'></p>   
    
Saída:  

<p align='center'><img src='./4 - esteganografia/imagem_final.png'></p> 

## 🔭 Exercício 5.1

Observando-se o programa labeling.cpp como exemplo, é possível verificar que caso existam mais de 255 objetos na cena, o processo de rotulação poderá ficar comprometido. Identifique a situação em que isso ocorre e proponha uma solução para este problema.

## Solução

Para resolver o problema de casos que a imagem tenha mais que 255 objetos a serem rotulados, podemos usar uma estrategia de fazer o rotulo ser em pontu flutuante, ou rotula usando a operação mod de 255.

## 🔭 Exercício 5.2

Aprimore o algoritmo de contagem apresentado para identificar regiões com ou sem buracos internos que existam na cena. Assuma que objetos com mais de um buraco podem existir. Inclua suporte no seu algoritmo para não contar bolhas que tocam as bordas da imagem. Não se pode presumir, a priori, que elas tenham buracos ou não.

## Solução

Para retirar as bolhas e buracos que estão nas bordas eu fiz o processo de excluir tanto a primeira e última linha, como também primeira e última coluna e assim usar a semente no floodFill. Já para conta os buracos, usei uma estrategia de pinta o fundo da imagem de branco usando o floodFill assim, a parte de dentro dos buracos ainda ficaria com a cor do fundo original e eu poderia contar agora quantos buracos tem. Sabendo a quantidade de buracos é só aplicar o floodFill na imagem, ver quantos objetos ele encontrou e diminuir do número de buracos, assim nos temos a quantidade de bolhas e buracos, como veremos a seguir:
```python
import cv2
import requests
import numpy as np
from io import BytesIO

def main():
    image_url = "https://agostinhobritojr.github.io/tutorial/pdi/figs/bolhas.png"

    response = requests.get(image_url)
    if response.status_code != 200:
        print("Erro ao fazer o download da imagem")
        return

    image = cv2.imdecode(np.frombuffer(response.content, np.uint8), cv2.IMREAD_GRAYSCALE)

    if image is None:
        print("Imagem não carregou corretamente")
        return

    cv2.imshow("imagem original", image)

    width = image.shape[1]
    height = image.shape[0]
    print(f"{width}x{height}")

    # Excluir bordas
    for i in range(height):
        if image[0, i] == 255:
            cv2.floodFill(image, None, (i, 0), 0)
        if image[width - 1, i] == 255:
            cv2.floodFill(image, None, (i, width - 1), 0)

    for i in range(width):
        if image[i, 0] == 255:
            cv2.floodFill(image, None, (0, i), 0)
        if image[i, height - 1] == 255:
            cv2.floodFill(image, None, (height - 1, i), 0)

    cv2.imwrite("image_semborda.png", image)

    # Buscar objetos presentes
    nobjects = 0
    for i in range(height):
        for j in range(width):
            if image[i, j] == 255:
                nobjects += 1
                cv2.floodFill(image, None, (j, i), nobjects)

    equalized = cv2.equalizeHist(image)
    cv2.imshow("imagem contada", image)
    cv2.imshow("realce", equalized)

    cv2.imwrite("image_realce.png", equalized)

    # Pintar fundo de branco para contagem de buracos
    cv2.floodFill(image, None, (0, 0), 255)

    # Procurando buracos
    counter = 0
    for i in range(height):
        for j in range(width):
            if image[i, j] == 0 and image[i, j - 1] > counter:
                counter += 1
                cv2.floodFill(image, None, (j - 1, i), counter)

    print(f"bolhas: {nobjects} e bolhas com buracos: {counter}")
    cv2.imshow("image final", image)
    cv2.imwrite("labeling.png", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

```
Entrada:  

<p align='center'><img src='./5 - labelling/bolhas.png'></p>   
    
Saídas:  

Imagem sem borda:  

<p align='center'><img src='./5 - labelling/image_semborda.png'></p>   
    
Imagem realce:  

<p align='center'><img src='./5 - labelling/image_realce.png'></p>   
    
Imagem preenchida:  

<p align='center'><img src='./5 - labelling/labeling.png'></p>   
    
Comparativo final:  

<p align='center'><img src='./5 - labelling/resultado_fim_5.2.png'></p>   
    
Valores:  

<p align='center'><img src='./5 - labelling/resultado_fimparci_5.2.png'></p> 

## 🔭 Exercício 6.1

Utilizando o programa exemplos/histogram.cpp como referência, implemente um programa equalize.cpp. Este deverá, para cada imagem capturada, realizar a equalização do histogram antes de exibir a imagem. Teste sua implementação apontando a câmera para ambientes com iluminações variadas e observando o efeito gerado. Assuma que as imagens processadas serão em tons de cinza.

## Solução

Para simular uma entrada em tons de cinza foi usada função cvtColor. Para fazer a equalização do histograma utiizei a função equalizeHist, logo depois fiz propriamente dito o histrograma da imagem original e da equalizada, assim tendo uma comparação entre as duas, como veremos a seguir:
```python
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
```
Saída em GIF:  

<p align='center'><img src='./6 - equalize/exemplo6_1.gif'></p>   

## 🔭 Exercício 6.2

Utilizando o programa exemplos/histogram.cpp como referência, implemente um programa motiondetector.cpp. Este deverá continuamente calcular o histograma da imagem (apenas uma componente de cor é suficiente) e compará-lo com o último histograma calculado. Quando a diferença entre estes ultrapassar um limiar pré-estabelecido, ative um alarme. Utilize uma função de comparação que julgar conveniente.

## Solução

Para solucionar esse exercício tive que criar um histograma que ficasse sempre salvando o último histograma do último frame e comparando com o histograma mais recente. Para fazer a comparação dos histogramas utilizei a função compareHist que me devolve a correlação entre os histogramas, assim consigo criar um if e verificar se esse correlação é alta ou baixa e criar um alerta "Movimento detectado - Ordem:", onde é apresentado no terminal um valor a mais a cada vez que for detectado movimento, como veremos a seguir:
```python
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
```
Saída em GIF:  

<p align='center'><img src='./6 - equalize/exemplo6_2.gif'></p> 

## 🔭 Exercício 7

Utilizando o programa exemplos/filtroespacial.cpp como referência, implemente um programa laplgauss.cpp. O programa deverá acrescentar mais uma funcionalidade ao exemplo fornecido, permitindo que seja calculado o laplaciano do gaussiano das imagens capturadas. Compare o resultado desse filtro com a simples aplicação do filtro laplaciano.

## Solução

Para solucionar esse exercício foi mais simples simples, foi somente adicionar a mascara do laplaciano do gaussiano junto as mascaras dos outros filtro e colocar a opção de escolher digitando a tecla p. Analisando o filtro laplaciano com o laplaciano do gaussiano percebe-se uma acentuação dos contornos, deixando a listra mais espessa e também mais contornos visíveis, como veremos a seguir:
```python
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
```
Saída em GIF:  

<p align='center'><img src='./7 - laplgauss/exemplo_7.gif'></p> 

## 🔭 Exercício 8

Utilizando o programa exemplos/addweighted.cpp como referência, implemente um programa tiltshift.cpp. Três ajustes deverão ser providos na tela da interface:  

-Um ajuste para regular a altura da região central que entrará em foco;  

-Um ajuste para regular a força de decaimento da região borrada;  

-Um ajuste para regular a posição vertical do centro da região que entrará em foco. Finalizado o programa, a imagem produzida deverá ser salva em arquivo.

## Solução

Para a resolução primeiramente foi definida a classe TiltShift, que contém variáveis irão armazenar configurações e parâmetros. Utilizando o método construtor, definimos os parâmetros iniciais para a altura l1, o centro l2 e o decaimento d do efeito tilt-shift, em seguida criamos as barras de controle que permitirão alterar os parâmetros e calculamos o alpha entre 0 e 1, baseado nos parâmetros fornecidos. Quando um parâmetro é alterado o método change altera os pesos pela imagem desfocada e utiliza um filtro de média para sua geração e realiza uma normalização da mesma, por fim é apresentada a imagem desfocada de acordo com os parâmetros e posterioemente salva, como veremos a seguir:

```python
import cv2
import numpy as np

class TiltShift:
    __slider_max = 100
    __track_bars = False
    __d_window_name = "forca decaimento"
    __l1_window_name = "altura"
    __l2_window_name = "centro"
    __window_name = "Tilt-Shift"
    __original_image: np.ndarray = None
    __blurred_image: np.ndarray = None
    __ones: np.ndarray = None
    tilt_shift: np.ndarray = None
    __delay = -1

    def __init__(self, l1=30, l2=60, d=30):
        self.__d = d
        self.__l1 = l1
        self.__l2_len = l2
        self.__mean_kernel = np.ones((9, 9), np.float32) / 81

    def __create_track_bars(self, window_name: str):
        try:
            cv2.getWindowProperty(window_name, 0)
        except:
            cv2.namedWindow(window_name)

        self.__window_name = window_name
        cv2.createTrackbar(self.__d_window_name, window_name, self.__d, self.__slider_max, self.__change)
        cv2.createTrackbar(self.__l1_window_name, window_name, self.__l1, self.__slider_max, self.__change)
        cv2.createTrackbar(self.__l2_window_name, window_name, self.__l2_len, self.__slider_max, self.__change)
        self.__track_bars = True

    def __alpha_f(self, x) -> float:
        l2 = self.__l1 + self.__l2_len
        return 0.5 * (np.tanh((x - self.__l1) / self.__d) - np.tanh((x - l2) / self.__d))

    def __change(self, value: int):
        self.__update_parameters()

        original_weight = np.zeros(self.__original_image.shape)
        blurred_weight = np.zeros(self.__blurred_image.shape)

        for x in range(int(original_weight.shape[0])):
            alpha = self.__alpha_f(x)

            blurred_weight[x, :] += 1 - alpha
            original_weight[x, :, :] += alpha

        tilt = np.multiply(original_weight, self.__original_image) / 255
        shift = np.multiply(blurred_weight, self.__blurred_image) / 255

        self.tilt_shift = tilt + shift
        if self.__delay > -1:
            cv2.imshow(self.__window_name, self.tilt_shift)

    @staticmethod
    def __normalize(x: int, t: int) -> float:
        return x * t / 100

    def __update_parameters(self):
        if self.__track_bars:
            self.__l1 = cv2.getTrackbarPos(self.__l1_window_name, self.__window_name) - 1
            self.__l2_len = cv2.getTrackbarPos(self.__l2_window_name, self.__window_name)
            self.__d = 0.5 * cv2.getTrackbarPos(self.__d_window_name, self.__window_name) + 1
            self.__l1 = self.__normalize(self.__l1, self.__original_image.shape[0])
            self.__l2_len = self.__normalize(self.__l2_len, self.__original_image.shape[1] / 2)

    def show_track_bars(self, window_name: str):
        if not self.__track_bars:
            self.__create_track_bars(window_name)

    def show_tilt_shift(self, delay: int):
        self.__delay = delay
        self.__change(0)

        if delay > -1:
            cv2.imshow("original image", self.__original_image)
            cv2.waitKey(delay)

    def __blurring_image(self):
        self.__blurred_image = cv2.filter2D(self.__original_image, cv2.CV_32F, self.__mean_kernel)

        for i in range(5):
            self.__blurred_image = cv2.filter2D(self.__blurred_image, cv2.CV_32F, self.__mean_kernel)

    def load_image(self, image_path: str):
        self.__original_image = cv2.imread(image_path)
        if self.__original_image is None:
            print("erro ao localizar")
            exit(1)
        self.__blurring_image()

    def set_image(self, image: np.ndarray):
        self.__original_image = image
        self.__blurring_image()

    def test_function_alpha(self):
        from matplotlib import pyplot

        x = np.array([i for i in range(129)])
        y = self.__alpha_f(x)
        pyplot.plot(x, 1 - y)
        pyplot.show()

    def save_image(self, path: str):
        cv2.imwrite(path, cv2.UMat(self.tilt_shift * 255))

if __name__ == '__main__':
    tilt_shift = TiltShift()
    tilt_shift.load_image("aquatico.jpg")
    tilt_shift.show_track_bars("Tilt-Shift")
    tilt_shift.show_tilt_shift(0)
    tilt_shift.save_image("tiltShift_aquatico.jpg")
```
Entrada:  

<p align='center'><img src='./8 - tiltshift/aquatico.jpg'></p>   
    
Saída em GIF:  

<p align='center'><img src='./8 - tiltshift/exemplo_8.gif'></p>   
    
Exemplo de imagem salva:  

<p align='center'><img src='./8 - tiltshift/tiltShift_aquatico.jpg'></p> 

## 🔔 PARTE II

## 🔭 Exercício 9

Utilizando os programa exemplos/dftimage.cpp, calcule e apresente o espectro de magnitude da imagem Figura 7.  

Compare o espectro de magnitude gerado para a figura Figura 7 com o valor teórico da transformada de Fourier da senóide.  

Usando agora o filestorage.cpp, mostrado na Listagem 4 como referência, adapte o programa exemplos/dftimage.cpp para ler a imagem em ponto flutuante armazenada no arquivo YAML equivalente (ilustrado na Listagem 5).  

Compare o novo espectro de magnitude gerado com o valor teórico da transformada de Fourier da senóide. O que mudou para que o espectro de magnitude gerado agora esteja mais próximo do valor teórico? Porque isso aconteceu?

## Solução

O resultado do espectro de magnitude gerado pelo código representa a magnitude da transformada de Fourier da imagem, mas essa não é idêntica ao valor teórico da transformada de Fourier de uma senoide pura, visto que, para o funcionamento do código foram feitas alterações no valor do log e consequentemente ocorrer uma modificação na distribuição de valores do espectro. Além disso, a diferença é esperada devido às características específicas da imagem processada e às transformações aplicadas durante o cálculo e visualização do espectro, como veremos a seguir:  

Código original convertido para python:  

```python
import cv2
import numpy as np
import matplotlib.pyplot as plt

def swap_quadrants(image):
    # se a imagem tiver tamanho ímpar, recorta a região para o maior
    image = image[:image.shape[0] & -2, :image.shape[1] & -2]

    centerX = image.shape[1] // 2
    centerY = image.shape[0] // 2

    # rearranja os quadrantes da transformada de Fourier de forma que 
    # a origem fique no centro da imagem
    # A B   ->  D C
    # C D       B A
    A = image[:centerY, :centerX]
    B = image[:centerY, centerX:]
    C = image[centerY:, :centerX]
    D = image[centerY:, centerX:]

    # swap quadrants (Top-Left with Bottom-Right)
    tmp = A.copy()
    A[:] = D
    D[:] = tmp

    # swap quadrant (Top-Right with Bottom-Left)
    tmp = B.copy()
    B[:] = C
    C[:] = tmp

def calculate_magnitude_spectrum(image):
    dft_M = cv2.getOptimalDFTSize(image.shape[0])
    dft_N = cv2.getOptimalDFTSize(image.shape[1])
    padded = cv2.copyMakeBorder(image, 0, dft_M - image.shape[0], 0, dft_N - image.shape[1], cv2.BORDER_CONSTANT, value=0)

    # calcula a DFT
    complex_image = cv2.dft(np.float32(padded), flags=cv2.DFT_COMPLEX_OUTPUT)
    swap_quadrants(complex_image)

    # calcula o espectro de magnitude
    magnitude = cv2.magnitude(complex_image[:, :, 0], complex_image[:, :, 1])
    magnitude += 1
    magnitude = np.log(magnitude)
    magnitude = cv2.normalize(magnitude, None, 0, 1, cv2.NORM_MINMAX)

    return magnitude

image = cv2.imread("teste9.png", cv2.IMREAD_GRAYSCALE)

# Calcula o espectro de magnitude
magnitude_spectrum = calculate_magnitude_spectrum(image)

# Exibe a imagem original e o espectro de magnitude
plt.subplot(121), plt.imshow(image, cmap="gray")
plt.title("Imagem"), plt.axis("off")
plt.subplot(122), plt.imshow(magnitude_spectrum, cmap="gray")
plt.title("Espectro de magnitude"), plt.axis("off")
plt.show()
```
A seguir o código modificado para ponto flutuante:  

```python
import cv2
import numpy as np
import matplotlib.pyplot as plt

def swap_quadrants(image):
    tmp = np.copy(image)
    cx = image.shape[1] // 2
    cy = image.shape[0] // 2
    image[:cy, :cx] = tmp[cy:, cx:]
    image[cy:, cx:] = tmp[:cy, :cx]
    image[:cy, cx:] = tmp[cy:, :cx]
    image[cy:, :cx] = tmp[:cy, cx:]

def main():
    # Carrega a imagem em ponto flutuante a partir do arquivo YAML
    fs = cv2.FileStorage("senoideatt.yml", cv2.FILE_STORAGE_READ)
    image = fs.getNode("mat").mat()
    fs.release()

    # Calcula a transformada de Fourier
    complex_image = cv2.dft(image, flags=cv2.DFT_COMPLEX_OUTPUT)
    swap_quadrants(complex_image)

    # Separa os planos real e imaginário
    planes = cv2.split(complex_image)

    # Calcula o espectro de magnitude
    magnitude = cv2.magnitude(planes[0], planes[1])
    magnitude += 1
    cv2.log(magnitude, magnitude)

    # Normaliza a magnitude
    cv2.normalize(magnitude, magnitude, 0, 1, cv2.NORM_MINMAX)

    # Exibe as imagens processadas
    cv2.imshow("Imagem", image.astype(np.uint8))
    cv2.imshow("Espectro de magnitude", magnitude)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
```
Saída código original:  

<p align='center'><img src='./9 - fourier/result9_1.png'></p>   
    
Saída código ponto flutuante:  

<p align='center'><img src='./9 - fourier/result9_2.png'></p> 

## 🔔 PARTE III

## 🔭 Exercício 11

Utilizando os programas exemplos/canny.cpp e exemplos/pontilhismo.cpp como referência, implemente um programa cannypoints.cpp. A idéia é usar as bordas produzidas pelo algoritmo de Canny para melhorar a qualidade da imagem pontilhista gerada. A forma como a informação de borda será usada é livre. Entretanto, são apresentadas algumas sugestões de técnicas que poderiam ser utilizadas:  

-Desenhar pontos grandes na imagem pontilhista básica;  

-Usar a posição dos pixels de borda encontrados pelo algoritmo de Canny para desenhar pontos nos respectivos locais na imagem gerada;  

-Experimente ir aumentando os limiares do algoritmo de Canny e, para cada novo par de limiares, desenhar círculos cada vez menores nas posições encontradas;  

-Escolha uma imagem de seu gosto e aplique a técnica que você desenvolveu;  

-Descreva no seu relatório detalhes do procedimento usado para criar sua técnica pontilhista.

## Solução

Para a resolução deste exercício eu adaptei o código do pontilhismo aplicando o algoritmo de Canny na imagem em questão, após isso é feito um for aninhado onde a posição e cor original são preservados, posteriormente desenhamos os círculos pequenos com os pontos obtidos das bordas de Canny e com isso obtemos a imagem final, como veremos a seguir, o código e após os resultados:
```python
import cv2
import numpy as np
import random
import requests
from io import BytesIO

STEP = 6
JITTER = 4
RAIO = 6
RAIO_PEQUENO = 3

url = 'https://cdn.wizard.com.br/wp-content/uploads/2017/01/05115936/aprenda-os-nomes-das-frutas-em-ingles.jpg'
# Faz a requisição GET para obter a imagem
response = requests.get(url)
image_data = response.content

# Carrega a imagem usando o OpenCV
image = cv2.imdecode(np.array(bytearray(image_data), dtype=np.uint8), cv2.IMREAD_COLOR)

height, width, _ = image.shape
xrange = list(range(0, height, STEP))
yrange = list(range(0, width, STEP))

points = np.full((height, width, 3), (255, 255, 255), dtype=np.uint8)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Aplica o algoritmo de Canny na imagem
border = cv2.Canny(gray, 80, 240)

cv2.imshow("bordas_canny", border)
cv2.waitKey(0)

# Realiza amostragem dos pontos
random.shuffle(xrange)
random.shuffle(yrange)

# for aninhado
for i in xrange:
    for j in yrange:
        x = i + random.randint(-JITTER, JITTER)
        y = j + random.randint(-JITTER, JITTER)

        x = min(max(x, 0), height - 1)
        y = min(max(y, 0), width - 1)

        color = tuple(map(int, image[x, y]))
        cv2.circle(points, (y, x), RAIO, color, -1, cv2.LINE_AA)

cv2.imshow("imagem_pontilhista", points)
cv2.waitKey(0)

pontos = []
for i in range(height):
    for j in range(width):
        if border[i, j] != 0:
            color = tuple(map(int, image[i, j]))
            pontos.append([j, i, color[0], color[1], color[2], 0])

random.shuffle(pontos)

for ponto in pontos:
    x, y, b, g, r, _ = ponto
    color = (b, g, r)
    cv2.circle(points, (x, y), RAIO_PEQUENO, color, -1, cv2.LINE_AA)

cv2.imshow("imagem_pontilhista_corrigida", points)
cv2.waitKey(0)
# imagem aprimorada
cv2.imwrite("cannypoints.png", points)
cv2.destroyAllWindows()
```
Entrada:  

<p align='center'><img src='./11 - pontcanny/exer11.jpg'></p>   
    
Saídas:  

Aplicação de Canny:  

<p align='center'><img src='./11 - pontcanny/borda_canny.png'></p>   
    
Aplicação do Pontilhismo:  

<p align='center'><img src='./11 - pontcanny/pontilhada.png'></p>   
    
Resultado da correção do pontilhismo pelas bordas de Canny:  

<p align='center'><img src='./11 - pontcanny/cannypoints.png'></p> 

## 🔭 Exercício 12

Utilizando o programa kmeans.cpp como exemplo prepare um programa exemplo onde a execução do código se dê usando o parâmetro nRodadas=1 e inciar os centros de forma aleatória usando o parâmetro KMEANS_RANDOM_CENTERS ao invés de KMEANS_PP_CENTERS. Realize 10 rodadas diferentes do algoritmo e compare as imagens produzidas. Explique porque elas podem diferir tanto.

## Solução

A solução é dada da seguinte forma, a matriz com as amostras samples deve conter em cada linha uma das amostras a ser processada pela função nClusters que informa a quantidade de aglomerados que se deseja obter, no nosso caso 8. A matriz rotulos é um objeto do tipo Mat preenchido com elementos do tipo int, onde cada elemento identifica a classe à qual pertence a amostra na matriz samples. Aqui realizamos o máximo de até 10000 iterações ou tolerância de 0.0001 para finalizar o algoritmo. O algoritmo é repetido por uma quantidade de vezes definida por nRodadas, assim a rodada que produz a menor soma de distâncias dos pontos para seus respectivos centros é escolhida como vencedora. Foi utilizada a inicialização dos centros de forma aleatória com KMEANS_RANDOM_CENTERS, como veremos a seguir:
```python
import cv2
import numpy as np
import requests
import io

nClusters = 8
nRodadas = 1

image_url = "https://img.freepik.com/fotos-premium/colecao-de-frutas-de-fundo-alimentar-macas-bagas-banana-quadrado-laranjas-frutas_770123-2578.jpg?w=2000"

# Faz o download da imagem da internet
response = requests.get(image_url)
image = cv2.imdecode(np.frombuffer(response.content, np.uint8), cv2.IMREAD_COLOR)

samples = np.float32(image.reshape(-1, 3))

for i in range(10):
    criteria = (cv2.TERM_CRITERIA_MAX_ITER + cv2.TERM_CRITERIA_EPS, 10000, 0.0001)
    flags = cv2.KMEANS_RANDOM_CENTERS

    compactness, labels, centers = cv2.kmeans(samples, nClusters, None, criteria, nRodadas, flags)

    centers = np.uint8(centers)
    clustered_image = centers[labels.flatten()]
    clustered_image = clustered_image.reshape(image.shape)

    cv2.imshow("clustered image", clustered_image)

    nome1 = "kmeans_image_" + str(i) + ".png"
    cv2.imwrite(nome1, clustered_image)
    print("IMG*")

    if cv2.waitKey(0) == ord('q'):
        break

cv2.destroyAllWindows()
```
Entrada:  

<p align='center'><img src='./12 - kmeans/exe12.jpg'></p>   
    
Saída em GIF com as 10 imagens geradas:  

<p align='center'><img src='./12 - kmeans/kmeans.gif'></p> 

## Referências
-Página da disciplina de PDI [[Link]](https://agostinhobritojr.github.io/tutorial/pdi/)  

-Repositório Professor Agostinho [![Repository](https://img.shields.io/badge/-Repo-191A1B?style=flat-square&logo=github)](https://github.com/agostinhobritojr)
