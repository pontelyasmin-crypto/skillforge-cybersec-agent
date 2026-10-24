#!/usr/bin/env python3
"""
SkillForge Security & Data Intelligence (@skillforge/cyber-core)
Skill Script: run_audit.py
Executes structured security audits, risk evaluations, and Dark Mode visual charts.
"""

import argparse
import json
import sys
from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="SkillForge CyberSec Risk Visual Auditor"
    )
    parser.add_argument(
        "--input",
        "-i",
        type=str,
        default=None,
        help="Path to JSON file with audit metrics",
    )
    parser.add_argument(
        "--output",
        "-o",
        type=str,
        default="audit_risk_matrix.png",
        help="Output PNG image path for the visual risk matrix",
    )
    return parser.parse_args()


def load_audit_data(input_path: str | None) -> tuple[str, float, pd.DataFrame]:
    if input_path and Path(input_path).exists():
        with open(input_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        title = data.get("audit_title", "Auditoria de Risco & Segurança Cibernética")
        threshold = float(data.get("tolerance_threshold", 5.0))
        rows = []
        for item in data.get("metrics", []):
            rows.append({
                "Métrica de Avaliação": item.get("metric"),
                "Status": item.get("status"),
                "Score de Risco (0-10)": float(item.get("risk_score", 0.0)),
                "Classificação": item.get("classification"),
                "Fonte de Verificação": item.get("benchmark"),
            })
        return title, threshold, pd.DataFrame(rows)

    # Dados padrão caso nenhum arquivo seja informado
    title = "⚡ SKILLFORGE | Matriz Visual de Risco & Vulnerabilidade"
    threshold = 5.0
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
    return title, threshold, pd.DataFrame(dados)


def generate_audit_report(title: str, threshold: float, df: pd.DataFrame, output_path: str):
    print("\n" + "=" * 80)
    print(f" ⚡ [SKILLFORGE AUDIT CORE] {title.upper()}")
    print("=" * 80)
    print(df.to_string(index=False))
    print("-" * 80)

    score_medio = df["Score de Risco (0-10)"].mean()
    tem_critico = any(df["Score de Risco (0-10)"] >= 8.0)

    if score_medio >= 4.0 or tem_critico:
        print("\n" + "🚨 " * 20)
        print(" ⚠️  [ALERTA VERMELHO DE RISCO CRÍTICO IDENTIFICADO]")
        print(f" 📊  Score Médio Geral: {score_medio:.2f} / 10.0")
        print(" 🛡️  AÇÕES OBRIGATÓRIAS DE REMEDIAÇÃO:")
        print("     1. Bloquear novas publicações em esteiras afetadas até correção de patch.")
        print("     2. Atualizar imediatamente runtimes e bibliotecas com advisories ativos.")
        print("     3. Revisar planos de contenção conforme diretrizes NIST SP 800-61 Rev. 2.")
        print("🚨 " * 20 + "\n")
    else:
        print(f"\n✅ Score Médio de Risco: {score_medio:.2f} / 10.0 — Ambiente Seguro.\n")

    # Gráfico Visual Dark Mode / Cyberpunk
    plt.style.use("dark_background")
    fig, ax = plt.subplots(figsize=(11, 5.5), facecolor="#0b0f19")
    ax.set_facecolor("#111726")

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

    ax.axvline(
        x=threshold,
        color="#ffcc00",
        linestyle="--",
        linewidth=1.8,
        label=f"Limite de Tolerância ({threshold:.1f})",
    )

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

    ax.set_xlim(0, 10.5)
    ax.set_title(
        f"⚡ {title}",
        fontsize=13,
        fontweight="bold",
        color="#00ffff",
        pad=15,
    )
    ax.set_xlabel(
        "Grau de Severidade (0.0 = Seguro | 10.0 = Risco Extremo)",
        fontsize=10,
        color="#8ea2c6",
        labelpad=10,
    )
    ax.tick_params(colors="#cbd5e1", labelsize=9.5)
    ax.grid(color="#1f293d", linestyle=":", linewidth=0.8, alpha=0.7)
    ax.legend(
        facecolor="#161f30",
        edgecolor="#334155",
        fontsize=9,
        loc="lower right",
        labelcolor="#e2e8f0",
    )

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, facecolor=fig.get_facecolor())
    print(f"📊 Gráfico salvo com sucesso em: {output_path}")


def main():
    args = parse_arguments()
    title, threshold, df = load_audit_data(args.input)
    generate_audit_report(title, threshold, df, args.output)


if __name__ == "__main__":
    main()
