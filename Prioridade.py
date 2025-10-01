import sys

class Processo:
    def __init__(self, pid, chegada, execucao, prioridade):
        self.pid = pid
        self.chegada = chegada
        self.execucao = execucao
        self.prioridade = prioridade
        self.tempo_restante = execucao  # Usado na versão preemptiva
        self.tempo_conclusao = 0
        self.tempo_retorno = 0
        self.tempo_espera = 0

def escalonamento_prioridade_nao_preemptivo(processos):
    tempo_atual = 0
    processos_concluidos = []
    ordem_execucao = []

    lista_processos = list(processos)

    while len(lista_processos) > 0:
        processos_prontos = [p for p in lista_processos if p.chegada <= tempo_atual]

        if not processos_prontos:

            tempo_atual = min(p.chegada for p in lista_processos)
            continue

        processo_a_executar = min(processos_prontos, key=lambda p: p.prioridade)

        ordem_execucao.append(processo_a_executar.pid)
        tempo_atual += processo_a_executar.execucao

        processo_a_executar.tempo_conclusao = tempo_atual
        processo_a_executar.tempo_retorno = processo_a_executar.tempo_conclusao - processo_a_executar.chegada
        processo_a_executar.tempo_espera = processo_a_executar.tempo_retorno - processo_a_executar.execucao

        processos_concluidos.append(processo_a_executar)
        lista_processos.remove(processo_a_executar)

    return " → ".join(ordem_execucao), processos_concluidos

def escalonamento_prioridade_preemptivo(processos):
    tempo_atual = 0
    processos_concluidos = []
    ordem_execucao = []

    for p in processos:
        p.tempo_restante = p.execucao

    lista_processos = list(processos)

    while len(processos_concluidos) < len(processos):
        processos_prontos = [p for p in lista_processos if p.chegada <= tempo_atual and p.tempo_restante > 0]

        if not processos_prontos:
            tempo_atual += 1
            continue

        processo_a_executar = min(processos_prontos, key=lambda p: p.prioridade)

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

    for p in processos_resultados:
        print(f"{p.pid}\t\t{p.tempo_espera}\t\t\t{p.tempo_retorno}")
        total_espera += p.tempo_espera
        total_retorno += p.tempo_retorno

    num_processos = len(processos_resultados)
    print(f"\nTempo Médio de Espera: {total_espera / num_processos:.2f}")
    print(f"Tempo Médio de Retorno: {total_retorno / num_processos:.2f}")
    print("-" * (len(titulo) + 8))



if __name__ == "__main__":
    dados_processos = [
        Processo('P1', 0, 5, 2),
        Processo('P2', 2, 3, 1),
        Processo('P3', 4, 8, 3),
        Processo('P4', 5, 6, 2),
        Processo('P5', 11, 8, 1)
    ]

    ordem_nao_preemptivo, resultados_nao_preemptivo = escalonamento_prioridade_nao_preemptivo(dados_processos)
    imprimir_resultados("Escalonamento por Prioridade (Não-Preemptivo)", ordem_nao_preemptivo,
                        resultados_nao_preemptivo)

    ordem_preemptivo, resultados_preemptivo = escalonamento_prioridade_preemptivo(dados_processos)
    imprimir_resultados("Escalonamento por Prioridade (Preemptivo)", ordem_preemptivo, resultados_preemptivo)