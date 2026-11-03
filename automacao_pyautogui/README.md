# 🤖 Automação de Cadastro de Produtos (PyAutoGUI)

Script de RPA que abre o navegador, faz login em um sistema web de exemplo e cadastra todos os produtos de `produtos.csv`. Ele simula teclado e mouse.

## Arquivos

| Arquivo | Descrição |
|---------|-----------|
| `teste_automacao.py` | Script de automação |
| `produtos.csv` | Base com 292 produtos |

## Pré-requisitos

| Item | Observação |
|------|------------|
| SO | Windows. O script usa a tecla `win` para abrir o Chrome |
| Navegador | Google Chrome instalado |
| Python | 3.9 ou superior |
| Pacotes | `pyautogui`, `pandas` |

```bash
pip install -r requirements.txt
```

## Execução

```bash
python teste_automacao.py
```

O sistema alvo é a página de treino `https://dlp.hashtagtreinamentos.com/python/intensivao/login`. Ela aceita qualquer login.

## Fluxo

1. Abre o Chrome pelo menu Iniciar e acessa o link.
2. Preenche e-mail e senha de teste e faz login.
3. Lê `produtos.csv` com pandas.
4. Para cada linha, clica no primeiro campo, preenche os 7 campos com `Tab`, envia e rola a página para cima.

## Formato do `produtos.csv`

| Coluna | Exemplo |
|--------|---------|
| `codigo` | `MOLO000251` |
| `marca` | `Logitech` |
| `tipo` | `Mouse` |
| `categoria` | `1` |
| `preco_unitario` | `25.95` |
| `custo` | `6.50` |
| `obs` | Opcional. Se vazio, o campo não é preenchido |

## ⚠️ Riscos e cuidados

- **O script controla teclado e mouse.** Não use o computador durante a execução.
- **Parada de emergência:** mova o mouse para o canto superior esquerdo da tela. O *failsafe* do PyAutoGUI interrompe o script.
- **Coordenadas fixas:** `pyautogui.click(x=637, y=382)` depende da resolução, do zoom e da posição da janela. Ajuste para o seu monitor. Use `pyautogui.position()` para descobrir as coordenadas.
- **Tempo fixo de espera** (`sleep(2)`): em conexões lentas, os comandos podem ser digitados antes de a página carregar.
- **Layout do teclado:** `pyautogui.write` pode falhar com caracteres acentuados em alguns layouts.

## Limitações conhecidas

1. O script lê `Produtos.csv` (com P maiúsculo), mas o arquivo é `produtos.csv`. No Windows funciona porque o sistema não diferencia maiúsculas. Em Linux/macOS, corrija o nome no código.
2. O CSV é lido por caminho relativo. Execute de dentro desta pasta.
3. Não há confirmação de que cada cadastro funcionou nem tratamento de erros.
