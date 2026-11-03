# 📊 Sistema de Análise de Vendas (Streamlit + Pandas + Plotly)

Aplicação web em Python para **cadastrar vendas**, **consultar o histórico** e **visualizar indicadores** em um dashboard interativo. Os dados ficam em um arquivo CSV local.

## Funcionalidades

| Aba | Recursos |
|-----|----------|
| 📝 Cadastrar Venda | Formulário com data, vendedor, produto e quantidade. O valor é **calculado automaticamente** pelo preço do produto |
| 📋 Vendas Cadastradas | Tabela ordenada da mais recente para a mais antiga, com datas em dd/mm/aaaa, valores em R$ e exportação do CSV filtrado |
| 📈 Dashboard | KPIs (faturamento, nº de vendas, ticket médio, itens vendidos) e gráficos por mês, vendedor, produto e evolução diária |
| 🔎 Filtros (sidebar) | Vendedor, produto e período. Aplicados à tabela e ao dashboard |

## Pré-requisitos

| Item | Versão / Observação |
|------|---------------------|
| Python | 3.9 ou superior (testado com 3.11) |
| Streamlit | 1.28 ou superior (necessário para `format="DD/MM/YYYY"` em `date_input`) |
| Pandas | Qualquer versão recente |
| Plotly | Qualquer versão recente |

## Estrutura

```
sistema_python/
├── sistema.py      # aplicação
├── vendas.csv      # base de dados
└── README.md
```

## Formato do `vendas.csv`

```csv
data,vendedor,produto,quantidade,valor
2026-06-03,Carla,Celular,1,2000.0
```

| Coluna | Tipo | Formato / Regra |
|--------|------|-----------------|
| `data` | Data | `AAAA-MM-DD` (ISO 8601) |
| `vendedor` | Texto | Nome do vendedor |
| `produto` | Texto | Nome do produto |
| `quantidade` | Inteiro | ≥ 1 |
| `valor` | Decimal | `quantidade × preço unitário`, separador decimal `.` |

> O cabeçalho é obrigatório. Se o arquivo não existir, ele é criado com cabeçalho no primeiro cadastro. Porém, a leitura inicial exige o arquivo com pelo menos uma venda (ver Limitações).

## Instalação

### Windows (PowerShell)

```powershell
cd "caminho\para\sistema_python"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install streamlit pandas plotly
```

### Linux / macOS

```bash
cd "caminho/para/sistema_python"
python3 -m venv .venv
source .venv/bin/activate
pip install streamlit pandas plotly
```

Opcional, para reprodutibilidade:

```bash
pip freeze > requirements.txt
```

## Execução

```bash
python -m streamlit run sistema.py
```

Acesse: <http://localhost:8501>

O CSV é localizado **relativo ao script** (`Path(__file__).parent`), então o app funciona independentemente da pasta de onde o comando é executado. Por exemplo, a partir da raiz do repositório:

```bash
python -m streamlit run sistema_python/sistema.py
```

## Configuração (`sistema.py`)

| Constante | Descrição |
|-----------|-----------|
| `ARQUIVO` | Caminho do CSV |
| `PRECOS` | Dicionário `produto → preço unitário`. Define as opções do cadastro e o cálculo do valor |
| `VENDEDORES` | Lista de vendedores disponíveis no cadastro |

### Adicionar um produto

```python
PRECOS = {"Celular": 2000.0, "Notebook": 3500.0, "Fone": 150.0, "Tablet": 2500.0}
```

O produto passa a aparecer no cadastro. Nos filtros e gráficos, ele aparece após a primeira venda registrada.

### Alterar um preço

Edite o valor em `PRECOS`. Vendas já cadastradas **mantêm o valor gravado**, o que é o comportamento correto para histórico.

## Indicadores do dashboard

| KPI | Cálculo |
|-----|---------|
| Faturamento | Soma de `valor` |
| Nº de vendas | Quantidade de linhas |
| Ticket médio | Faturamento ÷ nº de vendas |
| Itens vendidos | Soma de `quantidade` |

| Gráfico | Agrupamento |
|---------|-------------|
| Faturamento por mês | `valor` somado por mês (`AAAA-MM`) |
| Faturamento por vendedor | `valor` somado por vendedor, em ordem decrescente |
| Participação por produto | Proporção de `valor` por produto (rosca) |
| Evolução diária | `valor` somado por dia |

Todos os indicadores respeitam os filtros da sidebar.

## Backup

O cadastro **altera o arquivo `vendas.csv`**. Antes de testar, faça uma cópia:

```powershell
Copy-Item vendas.csv "vendas_backup_$(Get-Date -Format yyyyMMdd_HHmmss).csv"
```

```bash
cp vendas.csv "vendas_backup_$(date +%Y%m%d_%H%M%S).csv"
```

## Troubleshooting

| Sintoma | Causa provável | Ação |
|---------|----------------|------|
| `FileNotFoundError: vendas.csv` | Arquivo ausente ou nome diferente | Confirme que `vendas.csv` está na mesma pasta do `sistema.py` |
| `ModuleNotFoundError: plotly` (ou `pandas`) | Dependência não instalada no ambiente ativo | Ative o venv e rode `pip install streamlit pandas plotly` |
| `TypeError` em `date_input` com `format` | Streamlit anterior à 1.28 | `pip install --upgrade streamlit` |
| A venda cadastrada não aparece | Cache não invalidado | Confirme que `carregar_dados.clear()` está em `salvar_venda` |
| Aviso "Nenhuma venda para os filtros selecionados" | Filtros sem interseção (ex.: nenhum vendedor marcado) | Ajuste os filtros na sidebar |
| Datas ou valores estranhos após editar o CSV manualmente | Formato fora do padrão (`dd/mm/aaaa`, vírgula decimal, linha em branco) | Siga o formato da seção "Formato do `vendas.csv`" |
| Cabeçalho repetido no meio do arquivo | O CSV foi recriado sem cabeçalho, ou editado manualmente | Remova a linha duplicada e mantenha o cabeçalho só na primeira linha |

## Limitações conhecidas

1. **CSV como banco de dados:** não há controle de concorrência. Cadastros simultâneos de mais de um usuário podem corromper o arquivo. Para uso multiusuário, migre para SQLite ou outro banco.
2. **Sem ID de venda:** não é possível editar ou excluir uma venda específica pela interface, nem distinguir duplicatas legítimas de erros de digitação.
3. **CSV vazio ou ausente na inicialização:** o app depende de dados existentes para montar os filtros. Um arquivo só com cabeçalho causa erro no cálculo das datas mínima e máxima.
4. **Preços e vendedores fixos no código:** alterações exigem editar `sistema.py`.
5. **Sem autenticação:** pensado para uso local. Não exponha a porta 8501 em rede sem um reverse proxy com autenticação.
6. **Sem prévia do valor no formulário:** campos dentro de `st.form` não disparam atualização. O valor só é calculado e exibido após o envio.

## Próximos passos sugeridos

- [ ] Migrar o armazenamento para SQLite, com ID e data de cadastro
- [ ] Permitir edição e exclusão de vendas
- [ ] Mover `PRECOS` e `VENDEDORES` para um arquivo de configuração ou tabela
- [ ] Tratar a inicialização com CSV vazio
- [ ] Adicionar metas por vendedor e comparação com o período anterior nos KPIs