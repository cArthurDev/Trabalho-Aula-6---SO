class Processo:
    def __init__(self, pid, chegada, executa, prioridade):
        self.pid = pid
        self.chegada = chegada
        self.executa = executa
        self.prioridade = prioridade
        self.espera = 0
        self.retorno = 0
        self.finalizado = False

def priority_multi_queue_fcfs(processos):
    tempo = 0
    finalizados = 0
    n = len(processos)
    media_espera = 0
    media_retorno = 0
    ordem_execucao = []

    filas = {}
    for p in processos:
        if p.prioridade not in filas:
            filas[p.prioridade] = []
        filas[p.prioridade].append(p)


    prioridades_ordenadas = sorted(filas.keys())

    for prio in prioridades_ordenadas:
        fila = sorted(filas[prio], key=lambda x: x.chegada)
        for p in fila:
            if tempo < p.chegada:
                tempo = p.chegada
            p.espera = tempo - p.chegada
            p.retorno = p.espera + p.executa
            tempo += p.executa
            p.finalizado = True
            ordem_execucao.append(p.pid)
            media_espera += p.espera
            media_retorno += p.retorno

    bloco = ["Priority Scheduling - Multiple Queues (FCFS)\n-------"]
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

resultado_priority = priority_multi_queue_fcfs(processos)

with open("resultadosPriority.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write(resultado_priority + "\n")
