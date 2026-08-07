# 📲 Projeto_WhatsApp – Sistema de Envio Automático de Mensagens via WhatsApp

## 📌 Descrição
Projeto desenvolvido em Python para automatizar o envio de mensagens via **WhatsApp Web**, incluindo textos personalizados e imagens, utilizando uma planilha de clientes como base.

## 👨‍💻 Desenvolvedor
- **Nome:** Adriano Costa
- **Versão:** 1.0
- **Linguagem:** Python

## 🗂️ Estrutura do Repositório
- `.github/workflows/ci_python_tests.yml` — pipeline de CI (GitHub Actions) que instala as dependências e executa os testes com pytest a cada push/pull request.
- `Projeto_Whatzap/app8.py` — script principal do sistema de envio automático de mensagens.
- `Projeto_Whatzap/arquivo.bat` — script batch auxiliar para execução do processo.
- `Projeto_Whatzap/clientes.xlsx` — planilha com os contatos (nome e telefone).
- `Projeto_Whatzap/imagem_teste.png` e `icons8-whatsapp-logo-94.ico` — recursos de imagem/ícone utilizados no processo.
- `Contexto_Projeto` — documentação detalhada do projeto (descrição, bibliotecas, funcionalidades e instruções de uso).
- `requirements.txt` — dependências utilizadas nos testes (pytest).
- `test_exemple.py` — teste automatizado de exemplo.

## ⚙️ Funcionalidades
- Envio automático de mensagens via WhatsApp Web.
- Envio de imagem junto com o texto da mensagem.
- Geração de mensagens dinâmicas e personalizadas com o nome do cliente (modelo voltado a supermercados).
- Leitura da lista de contatos a partir de planilha Excel (`clientes.xlsx`).
- Cópia de texto e imagem para a área de transferência do Windows, com colagem automática via `pyautogui` e `win32clipboard`.
- Pipeline de Integração Contínua (GitHub Actions) executando testes automaticamente a cada push ou pull request.

## 📚 Tecnologias e Bibliotecas
- Python 3.10
- openpyxl
- webbrowser
- pyautogui
- pywin32 (win32clipboard)
- Pillow (PIL)
- pytest (testes)

## 🚀 Como Usar
1. Clone o repositório.
2. Instale as dependências:
```bash
pip install openpyxl pyautogui pillow pywin32 pytest
```
3. Preencha a planilha `clientes.xlsx` com nome e telefone dos contatos.
4. Execute o script `app8.py` (ou `arquivo.bat`) com o WhatsApp Web logado no navegador padrão.

## ✅ Testes
O repositório possui integração contínua configurada (GitHub Actions), executando os testes com `pytest` automaticamente a cada push ou pull request.

## ⚠️ Observações
Este script é destinado a uso interno/estudo e não deve ser distribuído sem autorização do desenvolvedor.
