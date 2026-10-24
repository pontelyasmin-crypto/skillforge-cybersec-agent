# ⚡ SkillForge CyberSec & Intelligence Agent (`@skillforge/cyber-core`)

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](#)
[![Security Standards](https://img.shields.io/badge/Standards-NIST%20%7C%20OWASP%20%7C%20CIS-00ff9d.svg)](#)
[![Theme](https://img.shields.io/badge/Visual-Cyberpunk%20Dark%20Mode-ff007f.svg)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> **Engenharia de dados, automações defensivas e desmistificação de fake news em cibersegurança.**

---

## 🎯 Propósito e Missão

O **SkillForge Security & Data Intelligence Agent** é uma iniciativa técnica focada em entregar análises rigorosas, ferramentas de auditoria e dashboards visuais com rigor científico, eliminando o alarmismo e a desinformação (*fake news*) na área de tecnologia e segurança da informação.

### 🛡️ Princípios Operacionais Inegociáveis
1. **Tolerância Zero ao Achismo:** Todas as análises cruzam fontes primárias oficiais (**NIST NVD**, **OWASP**, **GitHub Advisories**, **PyPI**, notas oficiais de lançamento).
2. **Anti-Fake News Ativo:** Desconstrução de boatos midiáticos explicando a causa-raiz técnica de falhas (ex: análise real de vulnerabilidades de corrupção de memória e CVEs oficiais vs pânico generalizado).
3. **Hands-On & Data-Driven:** Código funcional, testes automatizados e visualizações em alta resolução com estética Cyberpunk / Dark Mode.

---

## 📊 Matriz Visual de Risco

O módulo [`risk_analyzer.py`](risk_analyzer.py) realiza auditorias de métricas corporativas, categoriza Green Flags vs. Red Flags e aciona alertas críticos com base em limites de tolerância estipulados:

![Matriz Visual de Risco](security_risk_matrix.png)

---

## 🚀 Instalação e Execução

### Pré-requisitos
- Python 3.10 ou superior
- Git

### 1. Clonar o repositório
```bash
git clone https://github.com/pontelyasmin-crypto/skillforge-cybersec-agent.git
cd skillforge-cybersec-agent
```

### 2. Configurar o ambiente virtual e dependências
```bash
python -m venv venv

# Windows
.\venv\Scripts\activate

# Linux / macOS
source venv/bin/activate

pip install -r requirements.txt
```

### 3. Executar o analisador de risco
```bash
python risk_analyzer.py
```

---

## 📂 Estrutura do Repositório

```text
├── .gitignore               # Exclusões padrão para Python, SO e ambientes
├── AGENTS.md                # Diretrizes de arquitetura e persona do agente
├── README.md                # Documentação oficial do projeto
├── requirements.txt         # Dependências do projeto (pandas, matplotlib)
├── risk_analyzer.py         # Módulo central de auditoria e plotagem Dark Mode
└── security_risk_matrix.png # Visualização gerada pela esteira de auditoria
```

---

## 📜 Licença
Distribuído sob a licença MIT. Consulte `LICENSE` para mais informações.
