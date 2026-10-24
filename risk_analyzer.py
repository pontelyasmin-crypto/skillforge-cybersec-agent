"""
===============================================================================
AGENT PERSONA & ARCHITECTURE: SkillForge CyberSec & Intelligence
===============================================================================
[IDENTIDADE]
- Nome: SkillForge Security & Data Intelligence Agent (@skillforge/cyber-core)
- Missão: Criar automações e ferramentas visuais em Python unindo alta performance
  técnica, rigor científico e desmistificação de fake news em cibersegurança.
- Público-Alvo: Tech Leads, Recrutadores de Tech e desenvolvedores focados em prática.

[DIRETRIZES DE CONFIABILIDADE & FONTES OFICIAIS]
- Proibido achismo: Exigir dados reais e cruzamento de fontes primárias.
- Fontes Obrigatórias: NIST NVD, OWASP, GitHub Security Advisories e PyPI.
- Anti-Fake News: Desconstruir alarmismos da mídia leiga explicando a causa raiz 
  técnica de vulnerabilidades (ex: corrupção de memória Use-After-Free no PHP).

[MÓDULO DE ANÁLISE DE RISCO & VISUALIZAÇÃO]
- Classificação: Geração de tabelas tabulares separando Green Flags e Red Flags.
- Gráficos: Plotagem automática em Python (Matplotlib/Seaborn) de métricas de ameaça.
- Alerta Crítico: Disparar aviso visual de segurança caso o score médio ultrapasse 
  o limite de tolerância estipulado (Score >= 4.0).
===============================================================================
"""

import matplotlib.pyplot as plt
import pandas as pd


def run_security_audit(save_path: str = "security_risk_matrix.png") -> pd.DataFrame:
    # 1. Dados estruturados com base em auditoria de fontes seguras (NIST/OWASP)
    dados = {
        "Métrica de Avaliação": [
            "Criptografia de Dados (Rest & Transit)",
            "Política de Patch Management",
            "Conformidade LGPD / ISO 27001",
            "Tempo Médio de Resposta a Incidentes",
            "Uso de Runtimes Sem Atualização",
        ],
        "Status": ["OK", "OK", "OK", "Crítico", "Vulnerável"],
        "Score de Risco (0-10)": [1.0, 2.0, 1.0, 8.5, 9.0],
        "Classificação": [
            "Green Flag",
            "Green Flag",
            "Green Flag",
            "Red Flag",
            "Red Flag",
        ],
        "Fonte de Verificação": [
            "NIST SP 800-52 / TLS 1.3",
            "CIS Controls v8 (Asset Mgt)",
            "Auditoria LGPD Art. 46",
            "NIST SP 800-61 Rev. 2",
            "NVD NIST / CVE Advisories",
        ],
    }

    df = pd.DataFrame(dados)

    print("\n" + "=" * 80)
    print(" ⚡ [SKILLFORGE CORE] RELATÓRIO DE RISCO TÉCNICO & SEGURANÇA CIBERNÉTICA")
    print("=" * 80)
    print(df.to_string(index=False))
    print("-" * 80)

    # 2. Avaliação Algorítmica e Emissão de Alerta Crítico
    score_medio = df["Score de Risco (0-10)"].mean()

    if score_medio >= 4.0:
        print("\n" + "🚨 " * 20)
        print(" ⚠️  [ALERTA VERMELHO DE RISCO CRÍTICO IDENTIFICADO]")
        print(f" 📊  Score Médio de Exposição: {score_medio:.2f} / 10.0")
        print(" 🛡️  AÇÃO RECOMENDADA:")
        print("     - Bloqueio imediato de esteira ou assinatura contratual.")
        print("     - Mitigação obrigatória de runtimes desatualizados com base em patch oficial.")
        print("     - Revisão do SLA de Incident Response sob diretrizes NIST SP 800-61.")
        print("🚨 " * 20 + "\n")
    else:
        print(f"\n✅ Score Médio de Risco: {score_medio:.2f} / 10.0 — Nível Seguro.\n")

    # 3. Gráfico Visual com Estilo Cyberpunk / Dark Mode
    plt.style.use("dark_background")
    fig, ax = plt.subplots(figsize=(11, 5.5), facecolor="#0b0f19")
    ax.set_facecolor("#111726")

    # Paleta Neon Cyberpunk
    cores = [
        "#00ff9d" if flag == "Green Flag" else "#ff3366"
        for flag in df["Classificação"]
    ]

    bars = ax.barh(
        df["Métrica de Avaliação"],
        df["Score de Risco (0-10)"],
        color=cores,
        edgecolor="#ffffff",
        linewidth=0.6,
        height=0.55,
    )

    # Limite Crítico de Tolerância
    ax.axvline(
        x=5.0,
        color="#ffcc00",
        linestyle="--",
        linewidth=1.8,
        label="Limite de Tolerância (Score 5.0)",
    )

    # Rótulos de valor nas barras
    for bar in bars:
        width = bar.get_width()
        ax.text(
            width + 0.2,
            bar.get_y() + bar.get_height() / 2,
            f"{width:.1f}",
            va="center",
            ha="left",
            color="#ffffff",
            fontweight="bold",
            fontsize=10,
        )

    # Customizações Estéticas
    ax.set_xlim(0, 10.5)
    ax.set_title(
        "⚡ SKILLFORGE | Matriz Visual de Risco & Vulnerabilidade",
        fontsize=14,
        fontweight="bold",
        color="#00ffff",
        pad=15,
    )
    ax.set_xlabel(
        "Grau de Severidade (0.0 = Seguro | 10.0 = Risco Extremo)",
        fontsize=11,
        color="#8ea2c6",
        labelpad=10,
    )
    ax.tick_params(colors="#cbd5e1", labelsize=10)
    ax.grid(color="#1f293d", linestyle=":", linewidth=0.8, alpha=0.7)

    # Legenda
    ax.legend(
        facecolor="#161f30",
        edgecolor="#334155",
        fontsize=9,
        loc="lower right",
        labelcolor="#e2e8f0",
    )

    plt.tight_layout()
    plt.savefig(save_path, dpi=300, facecolor=fig.get_facecolor())
    print(f"📊 Gráfico renderizado com sucesso salvo em: {save_path}")
    return df


if __name__ == "__main__":
    run_security_audit()

