# Sistema de Gestão de Peças - Controle de Qualidade e Armazenamento
# Disciplina: Algoritmos e Lógica de Programação - UniFECAF

# ── Estruturas de dados globais ──────────────────────────────────────────────
pecas_cadastradas = []   # lista com todas as peças (aprovadas e reprovadas)
caixas_fechadas = []     # lista de caixas já fechadas
caixa_atual = []         # caixa em uso (máx. 10 peças)
CAPACIDADE_CAIXA = 10

# ── Critérios de qualidade ────────────────────────────────────────────────────
PESO_MIN = 95
PESO_MAX = 105
CORES_VALIDAS = ["azul", "verde"]
COMP_MIN = 10
COMP_MAX = 20


# ── Funções auxiliares ────────────────────────────────────────────────────────

def avaliar_peca(peso, cor, comprimento):
    """
    Avalia se a peça está aprovada ou reprovada.
    Retorna (status: str, motivos: list[str])
    """
    motivos = []

    if not (PESO_MIN <= peso <= PESO_MAX):
        motivos.append(f"Peso fora do intervalo ({peso}g — esperado {PESO_MIN}g a {PESO_MAX}g)")

    if cor.lower() not in CORES_VALIDAS:
        motivos.append(f"Cor inválida ('{cor}' — esperado: azul ou verde)")

    if not (COMP_MIN <= comprimento <= COMP_MAX):
        motivos.append(f"Comprimento fora do intervalo ({comprimento}cm — esperado {COMP_MIN}cm a {COMP_MAX}cm)")

    if motivos:
        return "reprovada", motivos
    return "aprovada", []


def armazenar_peca(peca):
    """Insere peça aprovada na caixa atual; fecha e abre nova se necessário."""
    global caixa_atual

    caixa_atual.append(peca) 

    if len(caixa_atual) >= CAPACIDADE_CAIXA:
        numero = len(caixas_fechadas) + 1
        caixas_fechadas.append({
            "numero": numero,
            "pecas": list(caixa_atual)
        })
        caixa_atual = []
        print(f"  📦  Caixa {numero} fechada com {CAPACIDADE_CAIXA} peças!")


def id_ja_existe(id_peca):
    return any(p["id"] == id_peca for p in pecas_cadastradas)


# ── Opções do menu ────────────────────────────────────────────────────────────

def cadastrar_peca():
    while True:
        print("\n── Cadastrar Nova Peça ──────────────────────")
        
        # ID
        
        id_peca = input("  ID da peça: ").strip()
        if not id_peca:
            print("  ✗ ID não pode ser vazio.")
            continue
        if id_ja_existe(id_peca):
            print(f"  ✗ Já existe uma peça com ID '{id_peca}'.")
            continue
        break
    # Peso
    while True:
        try:
            peso = float(input("  Peso (g): "))
            break
        except ValueError:
            print("  ✗ Peso inválido. Digite um número.")
            

    # Cor
    while True:
        cor = input("  Cor: ").strip()
        if not cor:
            print("  ✗ Cor não pode ser vazia.")
            continue
        break

    # Comprimento
    while True:
        try:
            comprimento = float(input("  Comprimento (cm): "))
            break
        except ValueError:
            print("  ✗ Comprimento inválido. Digite um número.")
        continue
    
    status, motivos = avaliar_peca(peso, cor, comprimento)

    peca = {
        "id": id_peca,
        "peso": peso,
        "cor": cor.lower(),
        "comprimento": comprimento,
        "status": status,
        "motivos": motivos
    }
    pecas_cadastradas.append(peca)

    if status == "aprovada":
        armazenar_peca(peca)
        print(f"  ✔ Peça '{id_peca}' APROVADA e armazenada.")
    else:
        print(f"  ✗ Peça '{id_peca}' REPROVADA:")
        for m in motivos:
            print(f"     • {m}")


def listar_pecas():
    print("\n── Listar Peças ─────────────────────────────")
    if not pecas_cadastradas:
        print("  Nenhuma peça cadastrada ainda.")
        return

    aprovadas = [p for p in pecas_cadastradas if p["status"] == "aprovada"]
    reprovadas = [p for p in pecas_cadastradas if p["status"] == "reprovada"]

    print(f"\n  APROVADAS ({len(aprovadas)}):")
    if aprovadas:
        for p in aprovadas:
            print(f"    [{p['id']}]  {p['peso']}g | {p['cor']} | {p['comprimento']}cm")
    else:
        print("    (nenhuma)")

    print(f"\n  REPROVADAS ({len(reprovadas)}):")
    if reprovadas:
        for p in reprovadas:
            motivo_str = "; ".join(p["motivos"])
            print(f"    [{p['id']}]  {p['peso']}g | {p['cor']} | {p['comprimento']}cm")
            print(f"           Motivo: {motivo_str}")
    else:
        print("    (nenhuma)")


def remover_peca():
    print("\n── Remover Peça ─────────────────────────────")
    id_peca = input("  ID da peça a remover: ").strip()

    alvo = next((p for p in pecas_cadastradas if p["id"] == id_peca), None)
    if not alvo:
        print(f"  ✗ Peça '{id_peca}' não encontrada.")
        return

    confirmacao = input(f"  Confirmar remoção de '{id_peca}'? (s/n): ").strip().lower()
    if confirmacao != "s":
        print("  Remoção cancelada.")
        return

    pecas_cadastradas.remove(alvo)

    # Remove da caixa atual se estiver lá
    if alvo in caixa_atual:
        caixa_atual.remove(alvo)

    print(f"  ✔ Peça '{id_peca}' removida com sucesso.")
    print("  ⚠  Nota: caixas já fechadas não são alteradas.")


def listar_caixas():
    print("\n── Caixas Fechadas ──────────────────────────")

    if not caixas_fechadas:
        print("  Nenhuma caixa fechada ainda.")
    else:
        for cx in caixas_fechadas:
            ids = ", ".join(p["id"] for p in cx["pecas"])
            print(f"  Caixa {cx['numero']:02d} — {len(cx['pecas'])} peças: {ids}")

    if caixa_atual:
        ids = ", ".join(p["id"] for p in caixa_atual)
        print(f"\n  Caixa em aberto — {len(caixa_atual)}/{CAPACIDADE_CAIXA} peças: {ids}")
    else:
        print("\n  Caixa em aberto — vazia (0 peças)")


def gerar_relatorio():
    print("\n════════════════════════════════════════════")
    print("           RELATÓRIO FINAL")
    print("════════════════════════════════════════════")

    total = len(pecas_cadastradas)
    aprovadas = [p for p in pecas_cadastradas if p["status"] == "aprovada"]
    reprovadas = [p for p in pecas_cadastradas if p["status"] == "reprovada"]

    print(f"\n  Total de peças cadastradas : {total}")
    print(f"  Total aprovadas            : {len(aprovadas)}")
    print(f"  Total reprovadas           : {len(reprovadas)}")

    total_caixas = len(caixas_fechadas) + (1 if caixa_atual else 0)
    print(f"\n  Caixas fechadas            : {len(caixas_fechadas)}")
    print(f"  Caixa em aberto            : {'sim' if caixa_atual else 'não'}")
    print(f"  Total de caixas utilizadas : {total_caixas}")

    if reprovadas:
        print("\n  ── Motivos de Reprovação ────────────────")
        for p in reprovadas:
            print(f"\n    Peça '{p['id']}':")
            for m in p["motivos"]:
                print(f"      • {m}")

    print("\n════════════════════════════════════════════\n")


# ── Menu principal ────────────────────────────────────────────────────────────

def menu():
    opcoes = {
        "1": ("Cadastrar nova peça",          cadastrar_peca),
        "2": ("Listar peças aprovadas/reprovadas", listar_pecas),
        "3": ("Remover peça cadastrada",       remover_peca),
        "4": ("Listar caixas fechadas",        listar_caixas),
        "5": ("Gerar relatório final",         gerar_relatorio),
        "0": ("Sair",                          None),
    }

    while True:
        print("\n╔══════════════════════════════════════════╗")
        print("║   SISTEMA DE GESTÃO DE PEÇAS             ║")
        print("╠══════════════════════════════════════════╣")
        for chave, (desc, _) in opcoes.items():
            print(f"║  {chave}. {desc:<38}║")
        print("╚══════════════════════════════════════════╝")

        escolha = input("  Escolha uma opção: ").strip()

        if escolha == "0":
            print("\n  Encerrando o sistema. Até logo!\n")
            break
        elif escolha in opcoes:
            opcoes[escolha][1]()
        else:
            print("  ✗ Opção inválida. Tente novamente.")


# ── Ponto de entrada ──────────────────────────────────────────────────────────

if __name__ == "__main__":
    menu()