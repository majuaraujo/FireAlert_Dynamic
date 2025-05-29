import heapq
from utils import calcular_prioridade

#Recebe uma lista de chamadas e organiza em uma heap (fila de prioridade).
#Retorna uma heap com chamadas organizadas pela maior prioridade.


def processar_chamadas_prioritarias(chamadas):

    heap = []
    for chamada in chamadas:
        prioridade = -calcular_prioridade(chamada)
        heapq.heappush(heap, (prioridade, chamada))
    return heap
