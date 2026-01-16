@echo off
REM Define a página de código para UTF-8
chcp 65001 >nul

REM Define o título com acentos
title Sistema de Envio Automático de Mensagens via WhatsApp

REM Vai para a pasta onde está o script
cd /d "C:\Users\Adriano\Desktop\envio_zap"

REM Executa o script Python
python app8.py

pause