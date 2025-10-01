# SJF (Shortest Job First)

class Processo:
    def __init__(self, pid, chegada, executa, prioridade):
        self.pid = pid
        self.chegada = chegada
        self.executa = executa
        self.prioridade = prioridade
        self.espera = 0
        self.retorno = 0
        self.finalizado = False

def sjf(processos):
    tempo = 0
    finalizados = 0
    ordem_execucao = []
    n = len(processos)
    media_espera = 0
    media_retorno = 0

    while finalizados < n:
        prontos = [p for p in processos if not p.finalizado and p.chegada <= tempo]
        
        if not prontos:
            tempo += 1
            continue

        proximo = min(prontos, key=lambda x: x.executa)
        proximo.espera = max(0, tempo - proximo.chegada)
        proximo.retorno = proximo.espera + proximo.executa
        tempo = max(tempo, proximo.chegada) + proximo.executa
        proximo.finalizado = True
        finalizados += 1
        ordem_execucao.append(proximo.pid)
        media_espera += proximo.espera
        media_retorno += proximo.retorno

    bloco = ["SJF (Shortest Job First)\n-------"]
    bloco.append("Ordem de Execução: " + " → ".join(ordem_execucao))
    bloco.append("Processo | Espera | Retorno")
    for p in processos:
        bloco.append(f"{p.pid}       | {p.espera}       | {p.retorno}")
    bloco.append(f"Tempo Médio de Espera: {media_espera / n:.2f}")
    bloco.append(f"Tempo Médio de Retorno: {media_retorno / n:.2f}")
    bloco.append("-------")
    return "\n".join(bloco)

processos = [
    Processo("P1", 0, 5, 2),
    Processo("P2", 2, 3, 1),
    Processo("P3", 4, 8, 3),
    Processo("P4", 5, 6, 2),
    Processo("P5", 11, 8, 1)
]

resultado_sjf = sjf(processos)

with open("resultados.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(resultado_sjf)
