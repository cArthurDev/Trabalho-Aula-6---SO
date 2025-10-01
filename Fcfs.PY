processos = [
    {'pid': 'P1', 'chegada': 0, 'executa': 5, 'prioridade': 2},
    {'pid': 'P2', 'chegada': 2, 'executa': 3, 'prioridade': 1},
    {'pid': 'P3', 'chegada': 4, 'executa': 8, 'prioridade': 3},
    {'pid': 'P4', 'chegada': 5, 'executa': 6, 'prioridade': 2},
    {'pid': 'P5', 'chegada': 11, 'executa': 8, 'prioridade': 1}
]

processos = sorted(processos, key=lambda p: p['chegada'])
tempo = 0
ordem_execucao = []
total_espera = 0
total_retorno = 0
resultados = []

for p in processos:
    if tempo < p['chegada']:
        tempo = p['chegada']
    espera = tempo - p['chegada']
    tempo_final = tempo + p['executa']
    retorno = tempo_final - p['chegada']
    tempo = tempo_final
    ordem_execucao.append(p['pid'])
    total_espera += espera
    total_retorno += retorno
    resultados.append({'pid': p['pid'], 'espera': espera, 'retorno': retorno})

bloco = []
bloco.append("FCFS (First-Come, First-Served)")
bloco.append("-------")
bloco.append("Ordem de Execução: " + " → ".join(ordem_execucao))
bloco.append("Processo|  Espera           | Retorno")
for r in resultados:
 bloco.append(f"{r['pid']}      |   {r['espera']}               |{r['retorno']}")
bloco.append(f"Tempo Médio de Espera: {total_espera / len(processos):.2f}")
bloco.append(f"Tempo Médio de Retorno: {total_retorno / len(processos):.2f}")
bloco.append("-------")

with open("resultadosFCFS.txt", "w", encoding="utf-8") as arquivo:

    arquivo.write('\n'.join(bloco) + '\n')
