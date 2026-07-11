@echo off
title Editor - Aprenda Qualquer Coisa
rem De DOIS CLIQUES neste arquivo pra abrir o editor no navegador.
rem (O editor precisa rodar em localhost -- por isso este atalho existe;
rem  abrir o ide.html direto nao funciona, e limitacao do navegador.)
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0scripts\serve-editor.ps1"
pause
