import statistics
# A MODA E A MEDIA E DESVIO DE PADRÃO, 
# DAS NOTAS DE ALUNOS DE UM COLÉGIO, 
# ALÉM DE MOSTRAR MENOR E A  MAIOR NOTA, 
def media_notas(frequencia):
    media  =  statistics.mean(frequencia)
    return media


def moda_notas(frequencia):
    moda = statistics.mode(frequencia)
    return moda


def desvio_notas(frequencia):
    desvio_p = statistics.stdev(frequencia)
    return desvio_p


def menor_maior(frequencia):
    menor =  min(frequencia)
    maior =  max(frequencia)
    print('Menor nota', menor)
    print('Maior nota', maior)


def mediana_nota (frequencia):
    medi =  statistics.median(frequencia)
    print(medi) 