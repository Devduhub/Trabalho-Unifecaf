# Sistema de Gestão de Peças – Controle de Qualidade 🏭

Um protótipo de automação industrial que simula um sistema real de inspeção, classificação e armazenamento de peças em uma fábrica.

**Desenvolvido para:** Disciplina Algoritmos e Lógica de Programação — UniFECAF

---

## O que é esse projeto?

Imagina uma fábrica onde centenas de peças passam por controle de qualidade todo dia. O método antigo? Uma pessoa olha para cada uma, anota em um papel se passou ou reprovou, e depois manualmente organiza em caixas. Demorado, cansativo, sujeito a erros.

Esse sistema automatiza **tudo**: recebe as informações da peça (peso, cor, tamanho), avalia instantaneamente se está dentro dos padrões, aprova ou reprova com motivo documentado, e armazena automaticamente em caixas de 10 peças cada.

O resultado? Precisão, velocidade e auditoria completa. 📊

---

## Como Funciona (In 3 Steps)

### 1️⃣ **Cadastro**
Você insere os dados de uma peça: ID, peso, cor e comprimento. O sistema recebe tudo.

### 2️⃣ **Avaliação Automática**
O sistema verifica:
- ✅ Peso entre 95g e 105g?
- ✅ Cor é azul ou verde?
- ✅ Comprimento entre 10cm e 20cm?

Se alguma coisa falhar, ele liga todas as falhas de uma vez.

### 3️⃣ **Resultado**
- Se aprovada → vai direto para a caixa (que fecha quando enche com 10 peças)
- Se reprovada → registrada com motivo, você vê o quê deu errado, pode remover depois

---

## Critérios de Qualidade (As Regras)

| O que é checado | Aceita | Rejeita |
|---|---|---|
| **Peso** | 95g a 105g | Menos de 95g ou mais de 105g |
| **Cor** | Azul ou Verde | Vermelho, amarelo, qualquer outra coisa |
| **Comprimento** | 10cm a 20cm | Menos de 10cm ou mais de 20cm |

Se uma peça não passa em qualquer um desses, ela é marcada como reprovada. É tudo ou nada — ou entra na caixa boa, ou fica registrada como defeituosa.

---

## Menu (O que você pode fazer)

Quando o programa roda, você vê um menu bonito:

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

### Opção 1: Cadastrar nova peça
Digite ID, peso, cor e comprimento. O sistema avalia na hora e diz se passou ou não. Se passou, entra na caixa. Se reprovou, fica no registro com os motivos.

### Opção 2: Listar peças
Vê todas as peças que você cadastrou até agora, separadas em dois grupos:
- **Aprovadas** (saíram direto para a caixa)
- **Reprovadas** (com o motivo de cada falha)

### Opção 3: Remover peça
Quer apagar uma peça que cadastrou? Colocou errado? Sem problema, digita o ID e remove. (Se já estiver em uma caixa fechada, a caixa não muda — só o registro fica marcado como removido.)

### Opção 4: Listar caixas
Mostra todas as caixas que já fecharam (cada uma tem 10 peças), com os IDs das peças dentro. Também mostra se tem uma caixa aberta em progresso.

### Opção 5: Gerar relatório
O destaque! Gera um relatório completo com:
- Total de peças cadastradas
- Quantas passaram / quantas reprovaram
- Quantas caixas foram fechadas
- Todos os motivos de reprovação, organizados por peça

Perfeito para o gerente pedir ao final do dia: "Quanto você processou?"

### Opção 0: Sair
Encerra o programa.

---

## Como Rodar o Programa (Passo a Passo)

### Requisito
Você precisa ter **Python 3.x** instalado. Se não tiver:
👉 Vai em https://www.python.org/downloads/ e instala.

### Passo 1: Abra o Terminal
No Windows:
- Clica com direito na pasta do projeto → "Abrir PowerShell aqui"

No Mac ou Linux:
- Abre o Terminal

### Passo 2: Digite o comando
```bash
python sistema.py
```

(Se no seu PC o comando é `python3`, use `python3 sistema.py` em vez disso.)

### Passo 3: Aparece o Menu
Pronto! Agora você vê as 6 opções. Digita um número (1, 2, 3, etc) e aperta Enter para usar.

### Passo 4: Para Sair
Digita `0` e aperta Enter. Fim.

---

## Exemplos Práticos (Entrada e Saída)

### ✅ Exemplo 1: Peça Aprovada

```
────────────────────────────────────────
  ID da peça: P001
  Peso (g): 100
  Cor: azul
  Comprimento (cm): 15
────────────────────────────────────────

  ✔ Peça 'P001' APROVADA e armazenada.
```

A peça passou em todos os critérios, foi direto para a Caixa 1.

---

### ❌ Exemplo 2: Peça com Um Problema

```
────────────────────────────────────────
  ID da peça: P002
  Peso (g): 90
  Cor: azul
  Comprimento (cm): 15
────────────────────────────────────────

  ✗ Peça 'P002' REPROVADA:
     • Peso fora do intervalo (90g — esperado 95g a 105g)
```

Falhou só no peso. As outras características estão ok, mas como o peso falhou, não vai para caixa.

---

### 💥 Exemplo 3: Peça com Múltiplos Problemas

```
────────────────────────────────────────
  ID da peça: P003
  Peso (g): 80
  Cor: vermelho
  Comprimento (cm): 25
────────────────────────────────────────

  ✗ Peça 'P003' REPROVADA:
     • Peso fora do intervalo (80g — esperado 95g a 105g)
     • Cor inválida ('vermelho' — esperado: azul ou verde)
     • Comprimento fora do intervalo (25cm — esperado 10cm a 20cm)
```

Falhou em TUDO. O sistema reporta os 3 problemas de uma vez. Assim o operador vê que tem algo muito errado nessa peça (ou na máquina que produziu ela).

---

### 📦 Exemplo 4: Caixa Fechando (Automático)

Depois de cadastrar 10 peças aprovadas seguidas:

```
  📦  Caixa 1 fechada com 10 peças!
```

A 11ª peça aprovada vai para uma Caixa 2 nova, vazia. Cada caixa garante 10 peças de boa qualidade.

---

### 📊 Exemplo 5: Relatório Final

```
════════════════════════════════════════
           RELATÓRIO FINAL
════════════════════════════════════════

  Total de peças cadastradas : 25
  Total aprovadas            : 20
  Total reprovadas           : 5

  Caixas fechadas            : 2
  Caixa em aberto            : SIM (0 peças)
  Total de caixas utilizadas : 3

  ── Motivos de Reprovação ────────────
  
    Peça 'P002':
      • Peso fora do intervalo (90g — esperado 95g a 105g)
    
    Peça 'P003':
      • Peso fora do intervalo (80g — esperado 95g a 105g)
      • Cor inválida ('vermelho' — esperado: azul ou verde)
      • Comprimento fora do intervalo (25cm — esperado 10cm a 20cm)
    
    (... outras peças reprovadas ...)

════════════════════════════════════════
```

---

## Um Dia Típico de Uso

Imagina que você é o QA (quality assurance) da fábrica:

1. **Manhã:** Seu supervisor te passa uma lista com 50 peças para verificar
2. **Você faz:** Cadastra cada uma pelo menu (1. Cadastrar nova peça)
3. **14h:** Digita `2` para listar e confirmar quantas passaram
4. **16h (fim de expediente):** Digita `5` para gerar o relatório final
5. **Você faz print** do relatório e manda para o gerente

Pronto. Você processou 50 peças em uma tarde, com auditoria completa. Se fosse manual? Levaria horas.

---

## Estrutura do Código (Para Curiosos)

O arquivo `sistema.py` tem:

- **Constantes** → Peso mín/máx, cores, etc (fácil mudar se as regras mudarem)
- **Estruturas de dados** → Listas que guardampeças e caixas
- **Funções** → Cada funcionalidade isolada em uma função
- **Menu principal** → Loop que fica pedindo entrada

Nada de dependências extras, nada complexo. Só Python puro. Por isso roda em qualquer máquina.

---

## Ideias de Expansão (Se Quisesse)

Este é um protótipo. Se expandisse para indústria de verdade:

1. **Banco de dados** → Guardar tudo em PostgreSQL, não só em memória
2. **Sensores automáticos** → Em vez de digitar, um sensor de peso/cor lê automaticamente
3. **Dashboard web** → Um gráfico bonito mostrando aprovação/reprovação em tempo real
4. **API** → Integração com outros sistemas da fábrica
5. **Machine Learning** → Prever problemas antes de acontecer
6. **Rastreabilidade** → Cada caixa tem código de barras, segue até o cliente

Mas as **regras básicas** que codificamos aqui? Continuariam as mesmas.

---

## Troubleshooting (Deu Ruim?)

### "Erro: python não é reconhecido"
Você não tem Python instalado ou não está no PATH. 
→ Instala em python.org (marca a opção "Add to PATH" durante instalação)

### "TypeError: unsupported operand type(s)"
Alguém mandou um texto quando o programa esperava um número.
→ O programa pede "Peso (g):" e você digita "cento" em vez de "100"
→ Digite números, não palavras

### "Peça com ID já existe"
Você duplicou um ID.
→ Use IDs únicos: P001, P002, P003...

### "Caixa não fecha"
Você cadastrou 8 peças aprovadas, mas a caixa não fechou.
→ Normal. Ela só fecha quando chegar em 10. Cadastre mais 2 para ver ela fechar.

---

## Autor & Informações

- **Desenvolvedor:** [Seu Nome]
- **Instituição:** UniFECAF
- **Disciplina:** Algoritmos e Lógica de Programação
- **Data:** 15 de abril de 2026
- **Versão:** 1.0

---

## Como Contribuir (Se Quiser Melhorar)

Tem uma ideia? Quer adicionar features?

1. Clona o repositório
2. Faz as mudanças em uma branch nova
3. Testa bem
4. Manda um Pull Request

Qualquer melhoria é bem-vinda! 🚀

---

**Dúvidas?** Qualquer coisa que não ficou claro, é só mandar mensagem ou abrir uma issue no GitHub.
