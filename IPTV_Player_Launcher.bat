@echo off
title IPTV Player Launcher
echo ========================================
echo       IPTV Player Launcher
echo ========================================
echo.
echo 1. Stalker IPTV Player
echo 2. Xtream IPTV Player
echo 3. Exit
echo.
set /p choice="Select player (1-3): "

if "%choice%"=="1" (
    start "" "dist\Stalker_IPTV_Player.exe"
) else if "%choice%"=="2" (
    start "" "dist\Xtream_IPTV_Player.exe"
) else if "%choice%"=="3" (
    exit
) else (
    echo Invalid choice. Please try again.
    pause
    goto :EOF
)
