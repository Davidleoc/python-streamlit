# 🍽️ Modelos de Restaurantes (POO)

Exercício de Programação Orientada a Objetos em Python. Ele modela restaurantes e as avaliações dos clientes.

## Arquivos

| Arquivo | Descrição |
|---------|-----------|
| `app.py` | Ponto de entrada. Cria restaurantes, altera o estado de um deles e lista todos |
| `restaurante.py` | Classe `Restaurante` |
| `avaliacao.py` | Classe `Avaliacao`, com validação de nota (0 a 10) |

## Pré-requisitos

- Python 3.9 ou superior
- Sem dependências externas

## Execução

```bash
cd modelos_restaurantes
python app.py
```

> Execute de dentro da pasta. Os imports são locais (`from restaurante import Restaurante`).

## Conceitos praticados

| Conceito | Onde |
|----------|------|
| Construtor `__init__` e `self` | `Restaurante`, `Avaliacao` |
| Atributo de classe compartilhado | `Restaurante.restaurantes` |
| Atributos protegidos (`_nome`) | Todas as classes |
| `__str__` | `Restaurante` |
| `@classmethod` | `Restaurante.listar_restaurantes` |
| `@property` | `Restaurante.media_avaliacoes` |
| Composição | `Restaurante` contém uma lista de `Avaliacao` |
| Validação com `raise ValueError` | `Avaliacao._validar_nota` |

## Exemplo de saída

```
Nome do Restaurante       | Categoria                 | Avaliação                 | Status
...
Praça                     | Gourmet                   | 0                         | False
Pizza Express             | Italiana                  | 0                         | False
Japa-Jantas               | Japones                   | 0                         | True
```

## Limitações conhecidas (código em desenvolvimento)

1. **`receber_avaliacao` gera erro hoje.** Em `avaliacao.py`, `_validar_nota` está marcado com `@classmethod`, mas não recebe `cls`. A correção é usar `@staticmethod`.
2. **`Avaliacao` não expõe `nota`.** `media_avaliacoes` usa `avaliacao.nota`, mas o atributo é `_nota`. Falta um `@property nota`.
3. **A property `ativo` está dentro de `listar_restaurantes`,** indentada no método errado. Ela nunca é registrada na classe, e a listagem mostra `True`/`False` em vez de `Ativo`/`Inativo`.
