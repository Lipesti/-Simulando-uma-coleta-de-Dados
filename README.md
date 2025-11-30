# 🚀 Desafio de Segurança Cibernética: Simulação de Malware (Ransomware e Keylogger)

Olá! Este projeto foi desenvolvido como parte de um desafio prático de **Segurança Cibernética** para fins **puramente educacionais**. O objetivo é simular o comportamento de dois tipos principais de *malware* – **Ransomware** e **Keylogger** – em um ambiente controlado, a fim de entender seus mecanismos e, mais importante, desenvolver estratégias de **defesa e mitigação**.

> ⚠️ **AVISO LEGAL:** O código aqui contido é estritamente conceitual e deve ser executado **apenas** em ambientes isolados (sandboxes ou máquinas virtuais) e sob total controle. Qualquer uso indevido ou malicioso é de responsabilidade exclusiva do usuário.

---

## 📋 Conteúdo do Projeto

O projeto é dividido em três áreas principais, conforme a estrutura do diretório:

### 1. ⌨️ Keylogger Simulado (`captura_tecla.py`)
* **Mecanismo:** Utiliza a biblioteca `pynput` do Python para registrar as teclas pressionadas pelo usuário em um arquivo de *log* local.
* **Foco Didático:** Demonstra como ocorre a **captura de dados de entrada**, o vetor de ataque primário para roubo de credenciais.

### 2. 🔐 Ransomware Simulado (`criptografia.py`)
* **Mecanismo:** Usa a biblioteca `cryptography` (módulo `Fernet`) para criptografar arquivos de teste em um diretório (`arquivos_teste/`) usando criptografia simétrica.
* **Resultado:** Gera uma chave secreta e uma "Nota de Resgate", que contém a chave para simular o processo de descriptografia após o "pagamento".
* **Foco Didático:** Entender a **estrutura de criptografia** e a **ameaça de indisponibilidade de dados**.

### 3. 🛡️ Documentação de Defesa
* Análise detalhada das medidas de **prevenção, detecção e resposta** para proteger sistemas contra esses tipos de ataque.

---

## ⚙️ Configuração e Execução

Para rodar as simulações, você precisa ter o **Python 3** instalado.

### 1. Clonar o Repositório

`bash
    git clone [https://github.com/Lipesti/-Simulando-uma-coleta-de-Dados](https://github.com/Lipesti/-Simulando-uma-coleta-de-Dados)
    cd -Simulando-uma-coleta-de-Dados`

### 2. Instalar Dependências
As simulações dependem das bibliotecas **pynput** e **cryptography**.

`bash
    pip install pynput cryptography`
  
### 3. Execução do Ransomware Simulado
⚠️ Cuidado: Execute apenas o código do Ransomware em um diretório com arquivos de teste que você não se importa em criptografar.
`bash
    python criptografia.py`

### 4. Execução do Keylogger Simulado
`bash
    python captura_tecla.py`


🛡️ Medidas de Defesa e Mitigação (O Foco Principal)
A. Prevenção e Backup
- Princípio 3-2-1 de Backup:
Mantenha 3 cópias dos seus dados, em 2 mídias diferentes, com 1 cópia off-site (desconectada).
➝ Esta é a única defesa que anula completamente a ameaça do Ransomware.
- Mínimo Privilégio:
Limite as permissões dos usuários e aplicativos.
➝ Um malware só pode danificar o que o usuário que o executou pode acessar.

### B. Defesa Comportamental

| **Medida**            | **Ransomware**                                                                 | **Keylogger**                                                                 |
|------------------------|--------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| **Antivírus / EDR**    | Detecta padrões de criptografia incomuns e bloqueia o processo.                | Identifica *hooks* de teclado e processos que monitoram entradas de usuário.  |
| **Sandboxing / VM**    | Executar apps suspeitos em ambientes isolados impede acesso aos arquivos reais.| O keylogger captura apenas as teclas do ambiente isolado (VM).                 |
| **MFA (Autenticação)** | Mesmo se a senha for roubada, o invasor não terá acesso sem o segundo fator.   | Reduz drasticamente o impacto do roubo de credenciais.                         |



