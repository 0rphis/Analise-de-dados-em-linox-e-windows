# Comparação de desempenho de operações de memória

## Objetivo

Comparar o tempo de operações de memória executadas por um microbenchmark em
Python nos sistemas Linux, macOS e Windows, sob condições experimentais
previamente definidas.

A comparação principal da atividade é entre Linux e Windows. O resultado do
macOS é apresentado como referência complementar.

As operações avaliadas são:

- alocação de memória (`alloc_ms`);
- escrita em memória (`write_ms`);
- leitura da memória (`read_ms`);
- liberação da referência (`free_ms`).

## Pergunta norteadora

Nas condições experimentais definidas, qual sistema operacional apresenta
melhor desempenho nas operações de memória e quais evidências sustentam essa
conclusão?

## Estrutura do repositório

```text
.
├── index.py
├── benchmark_memoria_linux.csv
├── benchmark_memoria_macos.csv
├── benchmark_memoria_windows.csv
├── tempo_execucao_linux.csv
├── tempo_execucao_macos.csv
├── tempo_execucao_windows.csv
└── README.md
```

## Requisitos

- Python 3.x;
- sistema Linux, macOS ou Windows;
- memória disponível para testes de até 1000 MB;
- ambientes com configurações registradas.

Verifique a versão do Python:

```bash
python --version
```

Em Linux e macOS, caso necessário:

```bash
python3 --version
```

## Como executar o microbenchmark

1. Clone ou baixe este repositório no sistema a ser testado.
2. Feche aplicações que possam consumir muita CPU ou memória.
3. Registre as informações do ambiente utilizado.
4. Execute o programa:

```bash
python3 index.py
```

No Windows, caso `python3` não funcione:

```bash
python index.py
```

5. Ao final da execução, renomeie os CSVs gerados de acordo com o sistema utilizado.

Exemplo para uma execução no Linux:

```text
benchmark_memoria_100a1000mb.csv → benchmark_memoria_linux.csv
tempo_execucao.csv → tempo_execucao_linux.csv
```

Repita o mesmo protocolo nos demais sistemas operacionais.

## Protocolo experimental

O microbenchmark executa 100 repetições para cada tamanho de memória:

```text
100, 200, 300, 400, 500, 600, 700, 800, 900 e 1000 MB
```

Em cada repetição, o programa mede os tempos de alocação, escrita, leitura e
liberação de memória. Os dados são registrados em arquivos CSV.

Para reduzir interferências nos resultados, foram controlados:

- mesmo código do microbenchmark;
- mesmos tamanhos de memória;
- mesma quantidade de repetições;
- mesma versão do Python, quando possível;
- mesmo hardware ou máquinas virtuais equivalentes;
- ausência de programas pesados em segundo plano;
- mesmo método de coleta e armazenamento dos dados.

## Ambientes utilizados

| Item | Linux | macOS | Windows |
|---|---|---|---|
| Distribuição/versão | Preencher | Preencher | Preencher |
| Kernel/versão do sistema | Preencher | Preencher | Preencher |
| Processador | Preencher | Preencher | Preencher |
| Memória RAM | Preencher | Preencher | Preencher |
| Armazenamento | Preencher | Preencher | Preencher |
| Versão do Python | Preencher | Preencher | Preencher |
| Tipo de execução | Dual boot/VM | Máquina física/VM | Dual boot/VM |

## Formato dos dados

Os arquivos `benchmark_memoria_*.csv` possuem as seguintes colunas:

| Coluna | Descrição |
|---|---|
| `tamanho_mb` | Quantidade de memória testada, em MB |
| `tamanho_bytes` | Quantidade de memória testada, em bytes |
| `iteracao` | Número da repetição |
| `alloc_ms` | Tempo de alocação, em milissegundos |
| `write_ms` | Tempo de escrita, em milissegundos |
| `read_ms` | Tempo de leitura, em milissegundos |
| `free_ms` | Tempo de liberação da referência, em milissegundos |

Os arquivos `tempo_execucao_*.csv` registram o tempo total de cada execução.

## Plano de análise

Os registros serão agrupados por sistema operacional e tamanho de memória.

Para cada grupo, serão calculados:

- média;
- mediana;
- desvio padrão;
- valores mínimo e máximo;
- comparação dos tempos de alocação, escrita, leitura e liberação.

Os resultados serão apresentados por tabelas comparativas e gráficos.

Um sistema será considerado mais eficiente em determinada operação quando
apresentar menor tempo médio e mediano de forma consistente para o mesmo
tamanho de memória.

Caso os resultados sejam diferentes entre operações ou tamanhos, a conclusão
será apresentada separadamente, sem afirmar que um sistema é superior em todas
as situações.

## Resultados e conclusão

A análise comparativa e os gráficos estão disponíveis em **[inserir nome do
arquivo de análise ou notebook]**.

Com base nos dados coletados, o sistema com melhor desempenho nas condições
avaliadas foi **[preencher após a análise]**.

A evidência principal foi **[preencher com os valores, tabelas e gráficos]**.

Esta conclusão é limitada ao hardware, às versões dos sistemas operacionais,
ao microbenchmark e às condições experimentais registradas neste repositório.
Ela não deve ser generalizada para outras máquinas ou aplicações.

## Integrantes

- Nome do integrante — contribuição
- Nome do integrante — contribuição
- Nome do integrante — contribuição
