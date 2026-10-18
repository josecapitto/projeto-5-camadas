# Projeto 6 - DTMF

O projeto contém duas aplicações independentes:

- `emissor.py`: solicita um número de 0 a 9, gera as duas frequências DTMF,
  reproduz o áudio e plota o sinal no tempo e na frequência.
- `receptor.py`: grava o áudio pelo microfone, calcula a FFT, encontra pelo
  menos cinco picos, identifica as duas frequências DTMF e informa o número.
- `projeto.py`: oferece um menu para abrir qualquer um dos lados.

## Instalação

As dependências já estão instaladas no ambiente isolado `.venv`. Se for
necessário recriá-lo em outro computador, execute:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

## Execução em dois computadores

No computador que produzirá o áudio:

```powershell
.\.venv\Scripts\python.exe emissor.py
```

No computador que captará o áudio:

```powershell
.\.venv\Scripts\python.exe receptor.py
```

Primeiro inicie o receptor. Quando ele solicitar, faça o emissor começar a
tocar. Só então pressione ENTER no receptor, para não gravar silêncio.

Também é possível executar `.\.venv\Scripts\python.exe projeto.py` e escolher
a função no menu.

## Observação sobre as frequências

O código usa a grade DTMF padrão: 697, 770, 852 e 941 Hz nas linhas; 1209,
1336, 1477 e 1633 Hz nas colunas. Para o trabalho numérico são usadas somente
as colunas de 1209, 1336 e 1477 Hz.
