# -*- coding: utf-8 -*-
"""
===========================================================
Sistema de Envio Automático de Mensagens via WhatsApp
===========================================================

📌 Descrição
Processo criado e desenvolvido para envio de mensagens automáticas via WhatsApp.

👨‍💻 Desenvolvedor
Adriano Costa

🗂️ Informações do Projeto
- Versão: 1.0
- Linguagem: Python

⚠️ Observações
Este script é destinado apenas para uso interno e não deve ser distribuído sem autorização.
"""

# Bibliotecas Utilizadas

import openpyxl
import webbrowser
import pyautogui
import os
import random
import io
import ctypes
import os
import ctypes  # popup no Windows
import win32clipboard  # function do Windows
from time import sleep
from urllib.parse import quote
from PIL import Image


# Função para copiar imagem para a área de transferência
def copy_image_to_clipboard(image_path):
    image = Image.open(image_path)
    output = io.BytesIO()
    image.convert("RGB").save(output, "BMP")
    data = output.getvalue()[14:]
    output.close()
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
    win32clipboard.CloseClipboard()

# Função para copiar texto para a área de transferência (✅ ajuste para acentos e emojis)
def copy_text_to_clipboard(texto):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32clipboard.CF_UNICODETEXT, texto)
    win32clipboard.CloseClipboard()

# Carrega a planilha
workbook = openpyxl.load_workbook('clientes.xlsx')
pagina_clientes = workbook['Sheet1']

# Caminho da imagem que você quer enviar
imagem_path = os.path.join(os.getcwd(), "imagem_teste.png")

mensagens_enviadas = []

# Lista de mensagens dinâmicas para público de supermercado
def gerar_mensagem(nome):
    mensagens = [
        f"*Olá {nome}!* 🛒\n\nSeu supermercado Modelo Smart preparou novidades fresquinhas para você hoje:\n"
        "🥬 Hortifruti direto da horta\n"
        "🥖 Pães e bolos saindo do forno\n"
        "🥛 Laticínios selecionados\n\n"
        "👉 Venha garantir qualidade e sabor para sua família!",

        f"🌞 Bom dia, {nome}! 🌞\n\nComece o dia com mais saúde:\n"
        "🍎 Frutas da estação\n"
        "🥗 Verduras e legumes frescos\n"
        "☕ Café e produtos para o seu café da manhã\n\n"
        "*Tudo pronto para você no Modelo Smart!*",

        f"✨ Oi {nome}! ✨\n\nHoje temos:\n"
        "🥩 Carnes selecionadas para sua refeição\n"
        "🍗 Frango e aves frescas\n"
        "🌽 Milho e acompanhamentos para o churrasco\n\n"
        "🛍️ Passe no supermercado e leve qualidade para casa!",

        f"💎 {nome}, cuidamos de cada detalhe para você 💎\n\n"
        "🧼 Produtos de limpeza para sua casa\n"
        "🪣 Itens de higiene pessoal\n"
        "📌 Mercearia completa\n\n"
        "*Tudo em um só lugar, com confiança e praticidade!*",

        f"☀️ Boa tarde, {nome}! ☀️\n\nVenha conferir:\n"
        "🥬 Hortifruti fresquinho\n"
        "🥛 Leite e derivados\n"
        "🥖 Padaria com pães quentinhos\n\n"
        "👉 Seu supermercado Modelo Smart está sempre pronto para te atender!"
    ]
    return random.choice(mensagens)

for linha in pagina_clientes.iter_rows(min_row=2):
    nome = linha[0].value
    telefone = linha[1].value

    try:
        # Abre o WhatsApp Web com o número
        link_mensagem_whatsapp = f'https://web.whatsapp.com/send?phone={telefone}'
        webbrowser.open(link_mensagem_whatsapp)
        sleep(15)

        # Copia a imagem para o clipboard
        copy_image_to_clipboard(imagem_path)
        sleep(5)

        # Cola a imagem
        pyautogui.hotkey('ctrl', 'v')
        sleep(5)

        # ✅ Ajuste: agora o texto é copiado para o clipboard e colado (mantém acentos e emojis)
        mensagem_texto = gerar_mensagem(nome)
        copy_text_to_clipboard(mensagem_texto)
        sleep(2)
        pyautogui.hotkey('ctrl', 'v')
        sleep(5)

        # Envia (Enter)
        pyautogui.press('enter')
        sleep(5)

        # Fecha a aba
        pyautogui.hotkey('ctrl', 'w')
        sleep(5)

        mensagens_enviadas.append(nome)

    except Exception as e:
        print(f'Não foi possível enviar mensagem para {nome}: {e}')
        with open('erros.csv', 'a', newline='', encoding='utf-8') as arquivo:
            arquivo.write(f'{nome},{telefone}{os.linesep}')

# Após concluir todos os envios
pyautogui.hotkey('ctrl', 'w')
sleep(5)

print("\n✅ Processo concluído!")
print(f"Mensagens enviadas com sucesso: {len(mensagens_enviadas)}")
for contato in mensagens_enviadas:
    print(f"- {contato}")


# ✅ Popup médio informando sucesso
mensagem_final = f"Todas as mensagens foram enviadas com sucesso!\nTotal: {len(mensagens_enviadas)} contatos."
resposta = ctypes.windll.user32.MessageBoxW(0, mensagem_final, "Processo Finalizado - Robô WhatsApp", 1)

# ✅ Se o usuário clicar em OK, fecha também o Visual Studio Code
if resposta == 1:
    try:
        # Verifica se o processo do VS Code está ativo
        retorno = os.system("tasklist /FI \"IMAGENAME eq Code.exe\" | find \"Code.exe\"")

        if retorno == 0:
            # Se encontrou o processo, encerra
            os.system("taskkill /f /im Code.exe")
            print("Visual Studio Code foi encerrado com sucesso.")
        else:
            print("Visual Studio Code não está em execução, nada a encerrar.")

    except Exception as e:
        print(f"Erro ao tentar fechar o VS Code: {e}")