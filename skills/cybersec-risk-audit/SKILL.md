---
name: cybersec-risk-audit
description: >-
  Audita a postura de segurança cibernética, analisa métricas de risco contra
  fontes primárias (NIST, OWASP, CIS, LGPD/ISO 27001), desmistifica boatos técnicos
  e gera matrizes visuais de ameaça em tema Cyberpunk/Dark Mode com emissão de alertas críticos.
  Use esta skill quando o usuário solicitar auditoria de risco, validação de conformidade,
  análise técnica de vulnerabilidades/CVEs ou geração de gráficos de severidade em Python.
---

# ⚡ CyberSec Risk Audit & Data Intelligence Skill

Esta skill capacita o agente a conduzir auditorias de segurança cibernética baseadas estritamente em evidências, eliminando o achismo e o sensacionalismo midiático (*anti-fake news*), calculando scores ponderados de severidade e renderizando relatórios visuais de alto impacto para Tech Leads e Recrutadores.

---

## 📋 Fluxo Operacional Passo a Passo

### Passo 1: Coleta e Estruturação das Métricas
Colete ou solicite ao usuário as métricas operacionais a serem auditadas. Cada métrica deve conter:
- **Nome da Métrica / Vetor de Análise** (ex: Criptografia em Trânsito, Política de Patches).
- **Status Operacional** (`OK`, `Atenção`, `Crítico`, `Vulnerável`).
- **Score de Risco (0.0 a 10.0)** ponderado pela severidade e probabilidade.
- **Classificação**: `Green Flag` (Score < 4.0) ou `Red Flag` (Score >= 4.0).
- **Norma / Fonte Primária de Verificação** (ex: NIST SP 800-52, OWASP Top 10, CIS Controls).

Consulte o arquivo de referências:
- [Benchmarks Oficiais NIST & OWASP](./references/nist_owasp_benchmarks.md)

---

### Passo 2: Verificação Anti-Fake News (Rigor Técnico)
Antes de emitir parecer sobre qualquer CVE ou incidente noticiado pela mídia:
1. Consulte as fontes primárias obrigatórias: **NIST NVD**, **OWASP**, **GitHub Advisory Database**, **PyPI Advisories** e notas oficiais de patch.
2. Identifique a causa-raiz no nível de código (ex: *Use-After-Free*, *Buffer Overflow*, *Race Condition*, *Broken Object Level Authorization*).
3. Separe o que a mídia leiga reportou do escopo real da vulnerabilidade e apresente a mitigação exata.

Consulte o guia de desmistificação:
- [Protocolo Anti-Fake News](./references/anti_fake_news_protocol.md)

---

### Passo 3: Execução do Script de Auditoria Visual
Execute o script em Python para processar os dados e gerar a matriz visual em Dark Mode / Cyberpunk:

```powershell
python .agents/skills/cybersec-risk-audit/scripts/run_audit.py --input .agents/skills/cybersec-risk-audit/examples/sample_audit_input.json --output audit_result.png
```

Ou invoque diretamente via código Python embutido no workspace.

---

### Passo 4: Avaliação do Alerta Crítico
Calcule a média ponderada do Score de Risco da avaliação:
- Se **Score Médio >= 4.0** ou qualquer métrica crítica com **Score >= 8.0**:
  - Emita obrigatoriamente o bloco **`🚨 [ALERTA VERMELHO DE RISCO CRÍTICO] 🚨`**.
  - Liste ações imediatas de contenção e mitigação antes de qualquer aprovação contratual ou deploy.

---

### Passo 5: Entrega do Relatório Executivo
Apresente a resposta final contendo:
1. **Tabela Classificada**: Linhas organizadas com distinção clara entre `Green Flags` e `Red Flags`.
2. **Citação de Fontes Primárias**: Referências aos frameworks e boletins oficiais.
3. **Link para o Gráfico Gerado**: Caminho absoluto ou relativo para a imagem PNG gerada.
4. **Plano de Ação Técnico**: Passos práticos de remediação recomendados para a engenharia.
