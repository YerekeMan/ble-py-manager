# Interactive BLE Manager

A Python-based CLI utility to scan, discover, and interact with Bluetooth Low Energy (BLE) devices. It automatically resolves GATT characteristic names to human-readable descriptions.

## Features
- **Device Discovery:** Scans for all nearby BLE devices.
- **Auto-Resolution:** Displays human-readable names for standard GATT characteristics (e.g., "Manufacturer Name" instead of `0x2A29`).
- **Interactive Mode:** Read from or write to specific characteristics using a simple index-based menu.
- **Error Handling:** Validates characteristic properties (read/write permissions) before execution.

---

# Интерактивный BLE Менеджер

Консольная утилита на Python для сканирования и взаимодействия с устройствами Bluetooth Low Energy (BLE). Автоматически преобразует UUID характеристик в понятные человеку названия.

## Возможности
- **Поиск устройств:** Сканирует все доступные BLE устройства поблизости.
- **Дешифровка названий:** Показывает названия стандартных GATT характеристик (например, "Model Number" вместо `0x2A24`).
- **Интерактивное меню:** Чтение данных (Read) и запись команд (Write) через выбор порядкового номера.
- **Обработка прав:** Проверяет права доступа к характеристике перед отправкой запроса.

## Setup / Установка
1. `pip install bleak`
2. `python main.py`