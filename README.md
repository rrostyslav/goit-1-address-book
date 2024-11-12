# Address Book CLI

**Address Book** — це Python CLI-інструмент, який допомагає вам додавати контакти в адресну книгу та управляти цією книгою з командного рядку

# Установка

- Завантажте встановлювальний пакет whl. [Завантажити](https://github.com/rrostyslav/goit-1-address-book/blob/main/dist/addrbook.whl)
- Встановіть застосунок

```bash 
pip install ./addr-book.whl
```

- Запустіть пакет увівши
```bash
addrbook
```

# Для розробки
## Вимоги

- Python 3.x
- `setuptools`

## Встановлення

### 1. Клонування репозиторію

Клонуйте репозиторій і перейдіть у папку проєкту:

```bash
git clone https://github.com/rrostyslav/goit-1-address-book
cd goit-1-address-book
```

### 2. Активація віртуального середовища
```bash
python -m venv venv
source venv/bin/activate  # для Linux/MacOS
venv\Scripts\activate  # для Windows
```

### 3. Установка залежностей
```bash
pip install setuptools
```

### 4. Побудова пакету
```bash
pip install -e .
```

### 5. Запуск пакету
```bash
addrbook
```
