# Sistema de Gestão de Peças 🏭

Projeto desenvolvido para a disciplina **Algoritmos e Lógica de Programação — UniFECAF**.

Protótipo de automação digital para controle de qualidade e armazenamento de peças industriais.

---

## Funcionalidades

- Cadastro de peças com avaliação automática de qualidade
- Armazenamento de peças aprovadas em caixas (10 peças por caixa)
- Fechamento automático de caixas ao atingir capacidade
- Remoção de peças cadastradas
- Relatório consolidado com aprovações, reprovações e caixas utilizadas

---

## Critérios de Qualidade

| Atributo     | Critério               |
|--------------|------------------------|
| Peso         | Entre 95g e 105g       |
| Cor          | Azul ou Verde          |
| Comprimento  | Entre 10cm e 20cm      |

---

## Como Rodar

**Pré-requisito:** Python 3.x instalado ([python.org](https://www.python.org/downloads/))

```bash
# Clone o repositório
git clone https://github.com/SEU_USUARIO/sistema-pecas.git
cd sistema-pecas

# Execute o programa
python sistema_pecas.py
```

Não há dependências externas — apenas a biblioteca padrão do Python.

---

## Menu Interativo

```
╔══════════════════════════════════════════╗
║   SISTEMA DE GESTÃO DE PEÇAS             ║
╠══════════════════════════════════════════╣
║  1. Cadastrar nova peça                  ║
║  2. Listar peças aprovadas/reprovadas    ║
║  3. Remover peça cadastrada              ║
║  4. Listar caixas fechadas               ║
║  5. Gerar relatório final                ║
║  0. Sair                                 ║
╚══════════════════════════════════════════╝
```

---

## Exemplos de Entrada e Saída

### Peça Aprovada

```
── Cadastrar Nova Peça ──────────────────────
  ID da peça: P001
  Peso (g): 100
  Cor: azul
  Comprimento (cm): 15
  ✔ Peça 'P001' APROVADA e armazenada.
```

### Peça Reprovada (múltiplos motivos)

```
── Cadastrar Nova Peça ──────────────────────
  ID da peça: P002
  Peso (g): 80
  Cor: vermelho
  Comprimento (cm): 25
  ✗ Peça 'P002' REPROVADA:
     • Peso fora do intervalo (80g — esperado 95g a 105g)
     • Cor inválida ('vermelho' — esperado: azul ou verde)
     • Comprimento fora do intervalo (25cm — esperado 10cm a 20cm)
```

### Fechamento automático de caixa

```
  📦  Caixa 1 fechada com 10 peças!
```

### Relatório Final

```
════════════════════════════════════════════
           RELATÓRIO FINAL
════════════════════════════════════════════

  Total de peças cadastradas : 12
  Total aprovadas            : 10
  Total reprovadas           : 2

  Caixas fechadas            : 1
  Caixa em aberto            : não
  Total de caixas utilizadas : 1

  ── Motivos de Reprovação ────────────────

    Peça 'P002':
      • Peso fora do intervalo (80g — esperado 95g a 105g)
      • Cor inválida ('vermelho' — esperado: azul ou verde)
      • Comprimento fora do intervalo (25cm — esperado 10cm a 20cm)
```

---

## Estrutura do Projeto

```
sistema-pecas/
├── sistema_pecas.py   # Código principal
└── README.md          # Este arquivo
```

---

## Tecnologias

- Python 3.x
- Sem dependências externas

---

## Autor

Eduardo Bruniere Silva — [github.com/Devduhub](https://github.com/Devduhub)