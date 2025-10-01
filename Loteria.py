import random
class Processo:
    def __init__(self, pid, chegada, execucao, prioridade):
        self.pid = pid
        self.chegada = chegada
        self.execucao = execucao
        self.prioridade = prioridade
        self.bilhetes = 0
        self.tempo_restante = execucao
        self.tempo_conclusao = 0
        self.tempo_retorno = 0
        self.tempo_espera = 0

def escalonamento_loteria(processos, semente_aleatoria=42):
    random.seed(semente_aleatoria)

    for p in processos:
        p.bilhetes = 4 - p.prioridade
        p.tempo_restante = p.execucao

    tempo_atual = 0
    processos_concluidos = []
    ordem_execucao = []
    lista_processos = list(processos)

    while len(processos_concluidos) < len(processos):
        processos_prontos = [p for p in lista_processos if p.chegada <= tempo_atual and p.tempo_restante > 0]

        if not processos_prontos:

            tempo_atual += 1
            continue

        urna_de_bilhetes = []
        for p in processos_prontos:
            for _ in range(p.bilhetes):
                urna_de_bilhetes.append(p.pid)

        pid_sorteado = random.choice(urna_de_bilhetes)

        processo_a_executar = None
        for p in lista_processos:
            if p.pid == pid_sorteado:
                processo_a_executar = p
                break

        if not ordem_execucao or ordem_execucao[-1] != processo_a_executar.pid:
            ordem_execucao.append(processo_a_executar.pid)

        processo_a_executar.tempo_restante -= 1
        tempo_atual += 1

        if processo_a_executar.tempo_restante == 0:
            processo_a_executar.tempo_conclusao = tempo_atual
            processo_a_executar.tempo_retorno = processo_a_executar.tempo_conclusao - processo_a_executar.chegada
            processo_a_executar.tempo_espera = processo_a_executar.tempo_retorno - processo_a_executar.execucao
            processos_concluidos.append(processo_a_executar)

    processos_concluidos.sort(key=lambda p: p.pid)

    return " → ".join(ordem_execucao), processos_concluidos


def imprimir_resultados(titulo, ordem_execucao, processos_resultados):

    print(f"\n--- {titulo} ---")
    print(f"Ordem de Execução: {ordem_execucao}")
    print("\nProcesso\tTempo de Espera\t\tTempo de Retorno")

    total_espera = 0
    total_retorno = 0

    processos_resultados.sort(key=lambda p: p.pid)

    for p in processos_resultados:
        print(f"{p.pid}\t\t{p.tempo_espera}\t\t\t{p.tempo_retorno}")
        total_espera += p.tempo_espera
        total_retorno += p.tempo_retorno

    num_processos = len(processos_resultados)
    print(f"\nTempo Médio de Espera: {total_espera / num_processos:.2f}")
    print(f"Tempo Médio de Retorno: {total_retorno / num_processos:.2f}")
    print("-" * (len(titulo) + 8))

if __name__ == "__main__":
    # Exemplo de Entrada fornecido
    dados_processos = [
        Processo('P1', 0, 5, 1),
        Processo('P2', 2, 3, 1),
        Processo('P3', 4, 8, 3),
        Processo('P4', 5, 6, 2),
        Processo('P5', 11, 8, 1)
    ]

    ordem_loteria, resultados_loteria = escalonamento_loteria(dados_processos, semente_aleatoria=42)
    imprimir_resultados("Escalonamento por Loteria (Lottery Scheduling)", ordem_loteria, resultados_loteria)