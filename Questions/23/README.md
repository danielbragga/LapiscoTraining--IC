Abrir uma imagem colorida, transformar para tom de cinza e aplique a técnica de Crescimento de Regiões. Para isto, pegue uma imagem qualquer real, com tanto que a mesma possua um objeto se destaque do fundo. Inicializar uma semente com um clique neste objeto, conforme o Tópico 21 e encontrar uma regra de adesão que seja capaz de segmentar este objeto. Aplique o Crescimento de regiões de forma iterativa, em que o algoritmo irá estabilizar apenas quando a região parar de crescer.