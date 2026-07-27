# Сборка APK приложения Standoff2 Cheats

## Что внутри
- `main.py` — основной код Kivy-приложения
- `buildozer.spec` — настройка для сборки APK

## Как собрать APK

### 1. Установи Buildozer на Linux / Termux

Для Linux:
```bash
sudo apt update && sudo apt install -y python3-pip python3-setuptools git
pip install buildozer
```

Для Termux (если поддерживается):
```bash
pkg install python git clang make
pip install buildozer
```

### 2. Перейди в папку с проектом
```bash
cd /storage/emulated/0/Documents
```

### 3. Запусти сборку APK
```bash
buildozer android debug
```

### 4. Найди APK
APK появится в папке:
```bash
bin/
```

### 5. Установи APK на телефон
```bash
adb install -r bin/standoff2cheats-0.1-debug.apk
```

## Важно
- На Termux сборка APK может не работать на всех устройствах.
- Если не получится на телефоне, лучше собрать APK на компьютере Linux.
- Для Kivy нужен доступ к файлам и разрешения на хранилище.

## Что делать, если сборка упала
- Напиши мне ошибки из терминала.
- Я подскажу, как исправить.
