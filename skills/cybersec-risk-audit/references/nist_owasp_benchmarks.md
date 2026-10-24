# 🛡️ Benchmarks Oficiais & Fontes Primárias de Conformidade

Este guia estabelece os parâmetros técnicos exigidos pela arquitetura **SkillForge CyberSec & Intelligence** para fundamentar relatórios de segurança sem especulações.

---

## 1. NIST (National Institute of Standards and Technology)

- **NIST SP 800-52 Rev. 2:** Diretrizes para seleção e configuração de algoritmos TLS. Exige TLS 1.2+ e recomenda fortemente TLS 1.3 para proteção em trânsito.
- **NIST SP 800-53 Rev. 5:** Catálogo de controles de segurança e privacidade para sistemas de informação federais e corporativos (Famílias AC, SC, SI, CA).
- **NIST SP 800-61 Rev. 2:** Guia de gerenciamento e resposta a incidentes de segurança computacional (Ciclo: Preparação -> Detecção e Análise -> Contenção, Erradicação e Recuperação -> Pós-Incidente).
- **NIST NVD (National Vulnerability Database):** Base oficial de dados de vulnerabilidades sincronizada com os identificadores CVE e matrizes CVSS v3.1 / v4.0.

---

## 2. OWASP (Open Web Application Security Project)

- **OWASP Top 10 (Web):**
  - A01:2021 - Broken Access Control
  - A02:2021 - Cryptographic Failures
  - A03:2021 - Injection (SQLi, Command Injection, etc.)
  - A04:2021 - Insecure Design
  - A05:2021 - Security Misconfiguration
  - A06:2021 - Vulnerable and Outdated Components
  - A07:2021 - Identification and Authentication Failures
  - A08:2021 - Software and Data Integrity Failures
  - A09:2021 - Security Logging and Monitoring Failures
  - A10:2021 - Server-Side Request Forgery (SSRF)
- **OWASP ASVS (Application Security Verification Standard) v4.0.3:** Critérios de verificação em níveis L1 (básico), L2 (padrão corporativo) e L3 (crítico).

---

## 3. CIS Controls (Center for Internet Security) v8

- **Controle 01:** Inventário e Gestão de Ativos Corporativos.
- **Controle 02:** Inventário e Gestão de Ativos de Software.
- **Controle 07:** Gerenciamento Contínuo de Vulnerabilidades e Patches.
- **Controle 10:** Defesas contra Malware.

---

## 4. Legislação & Privacidade (LGPD & ISO 27001)

- **LGPD (Lei nº 13.709/2018) Art. 46:** Dever de adotar medidas de segurança, técnicas e administrativas aptas a proteger os dados pessoais de acessos não autorizados e incidentes.
- **ISO/IEC 27001:2022 (Anexo A):**
  - A.5 - Controles Organizacionais
  - A.8 - Controles Tecnológicos (A.8.8 Gestão de Vulnerabilidades Técnicas, A.8.24 Uso de Criptografia).
