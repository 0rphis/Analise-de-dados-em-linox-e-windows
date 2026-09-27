import csv
import gc
import os
import time


TAMANHOS_MB = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
REPETICOES = 100
NOME_ARQUIVO = "benchmark_memoria_100a1000mb.csv"


def em_milisegundos(inicio, fim):
    return (fim - inicio) / 1_000_000

def gravar_tempo_total(pasta, tempo_total):
    nome_resumo = "tempo_execucao.csv"
    caminho_resumo = os.path.join(pasta, nome_resumo)
    arquivo_ja_existe = os.path.exists(caminho_resumo)

    with open(caminho_resumo, "a", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)

        if not arquivo_ja_existe:
            escritor.writerow([
                "tempo_total_segundos",
                "tempo_total_minutos",
            ])

        escritor.writerow([
            f"{tempo_total:.6f}",
            f"{tempo_total / 60:.2f}",
        ])

    return caminho_resumo


def main():
    # Salva o CSV na mesma pasta deste programa, independentemente do sistema
    # operacional ou da pasta usada para executar o script.
    pasta_do_script = os.path.dirname(os.path.abspath(__file__))
    caminho_arquivo = os.path.join(pasta_do_script, NOME_ARQUIVO)
    inicio_total = time.perf_counter()

    print("Iniciando benchmark. O arquivo sera salvo em:")
    print(caminho_arquivo)
    print()

    # newline="" permite que o modulo csv controle as quebras de linha.
    # Isso evita linhas vazias extras ao abrir o arquivo no Windows.
    with open(caminho_arquivo, "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow([
            "tamanho_mb",
            "tamanho_bytes",
            "iteracao",
            "alloc_ms",
            "write_ms",
            "read_ms",
            "free_ms",
        ])

        for tamanho_mb in TAMANHOS_MB:
            tamanho_bytes = tamanho_mb * 1024 * 1024
            padrao = b"\xAA" * tamanho_bytes

            print(f"=== Processando {tamanho_mb} MB ({REPETICOES} repeticoes) ===")

            for iteracao in range(1, REPETICOES + 1):
                inicio = time.perf_counter_ns()
                bloco = bytearray(tamanho_bytes)
                fim = time.perf_counter_ns()
                alloc_ms = em_milisegundos(inicio, fim)

                inicio = time.perf_counter_ns()
                bloco[:] = padrao
                fim = time.perf_counter_ns()
                write_ms = em_milisegundos(inicio, fim)

                inicio = time.perf_counter_ns()
                soma = sum(bloco)
                fim = time.perf_counter_ns()
                read_ms = em_milisegundos(inicio, fim)

                # "del" remove a referencia ao bloco. Nao usamos clear(), pois
                # ele zera cada byte e alteraria o que esta sendo medido.
                inicio = time.perf_counter_ns()
                del bloco
                fim = time.perf_counter_ns()
                free_ms = em_milisegundos(inicio, fim)

                escritor.writerow([
                    tamanho_mb,
                    tamanho_bytes,
                    iteracao,
                    f"{alloc_ms:.6f}",
                    f"{write_ms:.6f}",
                    f"{read_ms:.6f}",
                    f"{free_ms:.6f}",
                ])

                if iteracao % 10 == 0 or iteracao == REPETICOES:
                    print(f"  -> Progresso: {iteracao}/{REPETICOES} iteracoes concluidas")

            # Mantem os dados seguros caso o programa seja interrompido depois.
            arquivo.flush()
            del padrao
            gc.collect()
            print()

    print("Benchmark concluido com sucesso!")
    print(f"Dados exportados para: {caminho_arquivo}")

    fim_total = time.perf_counter()
    tempo_total = fim_total - inicio_total

    caminho_resumo = gravar_tempo_total(pasta_do_script, tempo_total)

    print(f"Tempo total: {tempo_total:.2f} segundos")
    print(f"Tempo total: {tempo_total / 60:.2f} minutos")
    print(f"Resumo salvo em: {caminho_resumo}")


if __name__ == "__main__":
    main()

