# 📁 Генератор тестовых файлов для MIME-проверки

Скрипт для создания набора тестовых файлов для проверки модуля `cust-ibank-check-files`.

---

## 📌 Назначение

Скрипт генерирует файлы для проверки корректности работы валидатора файлов, включая:

- Проверку MIME-типов через Tika
- Проверку расширений (WHITE_EXPANSION / DANG_EXPANSION)
- Проверку подмены Content-Type
- Проверку регистронезависимости
- Проверку извлечения расширения по последней точке
- Проверку граничных случаев

---

## 🚀 Быстрый старт

### 1. Убедитесь, что Python установлен

```bash
python --version
# или
py --version
```

### 2. Скачайте скрипт

**Способ 1 — через Git:**
```bash
git clone https://github.com/iSimpleLab/mime-generator.git
cd mime-generator
```

**Способ 2 — скачать ZIP:**
- Перейдите по ссылке: https://github.com/iSimpleLab/mime-generator
- Нажмите **"Code"** → **"Download ZIP"**
- Распакуйте архив

**Способ 3 — скачать только файл:**
- Прямая ссылка: https://raw.githubusercontent.com/iSimpleLab/mime-generator/main/create_test_files.py

### 3. Запустите скрипт

```bash
python create_test_files.py
```

### 4. Результат

Все файлы появятся в папке `test_files/`

---

## 📂 Структура генерируемых файлов

### 1. 📄 Корректные файлы (правильный MIME + расширение)

| Файл | MIME-тип | Описание |
|------|----------|----------|
| `correct.pdf` | `application/pdf` | Корректный PDF-файл |
| `correct.png` | `image/png` | Корректный PNG-файл |
| `correct.jpg` | `image/jpeg` | Корректный JPG-файл |
| `correct.txt` | `text/plain` | Текстовый файл |
| `correct.gif` | `image/gif` | GIF-файл |
| `correct.zip` | `application/zip` | ZIP-архив |
| `correct.xml` | `application/xml` | XML-файл |
| `correct.json` | `application/json` | JSON-файл |
| `correct.docx` | `application/vnd.openxmlformats-officedocument.wordprocessingml.document` | DOCX-файл |
| `correct.xlsx` | `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet` | XLSX-файл |

---

### 2. ⚠️ Файлы с подменой содержимого (fake MIME)

| Файл | Расширение | Реальный MIME | Описание |
|------|------------|---------------|----------|
| `fake.pdf` | `.pdf` | `text/html` | HTML внутри, расширение PDF |
| `fake.png` | `.png` | `text/html` | HTML внутри, расширение PNG |
| `fake.jpg` | `.jpg` | `text/html` | HTML внутри, расширение JPG |
| `fake.gif` | `.gif` | `text/html` | HTML внутри, расширение GIF |
| `fake.txt` | `.txt` | `text/html` | HTML внутри, расширение TXT |

**Назначение:** Проверка, что валидатор определяет реальный MIME через Tika, а не доверяет расширению.

---

### 3. 🔴 Опасные расширения (для DANG_EXPANSION)

| Файл | Расширение | Описание |
|------|------------|----------|
| `malware.exe` | `.exe` | Исполняемый файл |
| `script.bat` | `.bat` | Batch-скрипт |
| `runner.sh` | `.sh` | Shell-скрипт |
| `payload.js` | `.js` | JavaScript-файл |
| `script.vbs` | `.vbs` | VBScript-файл |
| `script.ps1` | `.ps1` | PowerShell-скрипт |
| `virus.com` | `.com` | COM-файл |
| `malware.dll` | `.dll` | DLL-библиотека |
| `dangerous.scr` | `.scr` | Screensaver |
| `virus.pif` | `.pif` | Program Information File |
| `bad.cmd` | `.cmd` | Command-файл |
| `evil.jar` | `.jar` | Java-архив |
| `malware.msi` | `.msi` | MSI-установщик |
| `trojan.bat` | `.bat` | Batch-файл (троян) |

**Назначение:** Проверка, что файлы с опасными расширениями отклоняются.

---

### 4. 🔄 Файлы с двойными расширениями

| Файл | Извлеченное расширение | Описание |
|------|------------------------|----------|
| `document.pdf.exe` | `exe` | EXE под видом PDF |
| `image.png.exe` | `exe` | EXE под видом PNG |
| `archive.zip.exe` | `exe` | EXE под видом ZIP |
| `file.txt.pdf` | `pdf` | PDF под видом TXT |
| `data.xml.exe` | `exe` | EXE под видом XML |
| `backup.tar.gz.exe` | `exe` | EXE с двойным расширением |
| `virus.jpg.exe` | `exe` | EXE под видом JPG |

**Назначение:** Проверка, что расширение извлекается ПО ПОСЛЕДНЕЙ ТОЧКЕ.

---

### 5. 🔍 Файлы без расширения

| Файл | Описание |
|------|----------|
| `noextension` | Файл без расширения |
| `.hiddenfile` | Скрытый файл (точка в начале) |
| `file_without_dot` | Файл без точки в имени |
| `_nodot` | Файл без точки (начинается с подчеркивания) |

**Назначение:** Проверка обработки файлов без расширения.

---

### 6. 📝 Файлы с несколькими точками в имени

| Файл | Извлеченное расширение | Описание |
|------|------------------------|----------|
| `my.document.final.pdf` | `pdf` | PDF с точками в имени |
| `image.main.background.png` | `png` | PNG с точками в имени |
| `backup.2024.01.15.zip` | `zip` | ZIP с датой в имени |
| `project.v1.2.3.tar.gz` | `gz` | TAR.GZ с версией |
| `file.name.with.many.dots.txt` | `txt` | Много точек в имени |

**Назначение:** Проверка извлечения расширения по последней точке.

---

### 7. 🔤 Файлы с разными регистрами

| Файл | Нормализованное расширение | Описание |
|------|---------------------------|----------|
| `test.PDF` | `pdf` | PDF в верхнем регистре |
| `image.PNG` | `png` | PNG в верхнем регистре |
| `photo.JPG` | `jpg` | JPG в верхнем регистре |
| `document.PdF` | `pdf` | PDF в смешанном регистре |
| `image.PnG` | `png` | PNG в смешанном регистре |
| `text.TXT` | `txt` | TXT в верхнем регистре |
| `file.Js` | `js` | JS в смешанном регистре |

**Назначение:** Проверка регистронезависимости.

---

### 8. 📄 Бинарные файлы

| Файл | MIME-тип | Описание |
|------|----------|----------|
| `test.doc` | `application/msword` | Старый DOC-формат |
| `test.xls` | `application/vnd.ms-excel` | Старый XLS-формат |
| `test.ppt` | `application/vnd.ms-powerpoint` | Старый PPT-формат |
| `test.rtf` | `text/rtf` | RTF-документ |

**Назначение:** Проверка определения MIME для бинарных форматов.

---

### 9. ⚡ Специальные файлы для граничных случаев

| Файл | Описание |
|------|----------|
| `empty.pdf` | Пустой файл (0 байт) |
| `small.pdf` | Файл размером 4 байта |
| `this_is_a_very_long_filename_...pdf` | Файл с очень длинным именем |
| `my test file with spaces.pdf` | Файл с пробелами в имени |
| `тестовый_файл.pdf` | Файл с кириллицей в имени |
| `cyrillic_content.txt` | Файл с кириллицей в содержимом |

**Назначение:** Проверка обработки граничных случаев.

---

## 🧪 Рекомендуемые тестовые сценарии

После генерации файлов выполните проверку:

### 1. Проверка корректного PDF
- **Настройки:** `MIME_TYPE_FILE_LIST` содержит `application/pdf`, `WHITE_EXPANSION` содержит `pdf`
- **Файл:** `correct.pdf`
- **Ожидаемый результат:** ✅ Успех

### 2. Проверка подмены Content-Type
- **Настройки:** `MIME_TYPE_FILE_LIST` содержит `image/png`
- **Файл:** `fake.png` (HTML внутри)
- **Ожидаемый результат:** ❌ Ошибка "declaredMime не соответствует detectedMime"

### 3. Проверка опасного расширения
- **Настройки:** `DANG_EXPANSION` содержит `exe`
- **Файл:** `malware.exe`
- **Ожидаемый результат:** ❌ Ошибка "расширение в DANG_EXPANSION"

### 4. Проверка файла без расширения
- **Настройки:** `WHITE_EXPANSION` содержит `pdf,png`
- **Файл:** `noextension`
- **Ожидаемый результат:** ❌ Ошибка "расширение отсутствует"

### 5. Проверка регистронезависимости
- **Настройки:** `WHITE_EXPANSION` содержит `pdf`
- **Файл:** `test.PDF`
- **Ожидаемый результат:** ✅ Успех

### 6. Проверка извлечения по последней точке
- **Настройки:** `WHITE_EXPANSION` содержит `exe`
- **Файл:** `document.pdf.exe`
- **Ожидаемый результат:** ❌ Ошибка "расширение exe в DANG_EXPANSION" (извлечено как `exe`)

### 7. Проверка MIME вне списка
- **Настройки:** `MIME_TYPE_FILE_LIST` содержит `image/png`
- **Файл:** `correct.pdf`
- **Ожидаемый результат:** ❌ Ошибка "detectedMime не в списке"

---

## 📋 Полный список генерируемых файлов

После запуска скрипта будут созданы файлы следующих категорий:

| Категория | Количество файлов | Примеры |
|-----------|-------------------|---------|
| 📄 Корректные | ~15 | `correct.pdf`, `correct.png`, `test.doc` |
| ⚠️ Fake MIME | 5 | `fake.pdf`, `fake.png`, `fake.jpg` |
| 🔴 Опасные | 14 | `malware.exe`, `script.bat`, `payload.js` |
| 🔄 Двойные расширения | 7 | `document.pdf.exe`, `image.png.exe` |
| 🔍 Без расширения | 4 | `noextension`, `.hiddenfile` |
| 📝 Много точек | 5 | `my.document.final.pdf` |
| 🔤 Регистры | 7 | `test.PDF`, `image.PNG` |
| ⚡ Граничные | ~6 | `empty.pdf`, `small.pdf` |

**Всего:** ~60+ файлов

---

## 📝 Примечания

1. Скрипт создает папку `test_files/` в текущей директории
2. Если папка уже существует, файлы будут перезаписаны
3. Для работы не требуется установка дополнительных библиотек
4. Скрипт работает на Windows, Linux и macOS

---

## 🤝 Контакты
**Репозиторий:** https://github.com/VitalyPyshnov/mime-generator  
**Назначение:** Тестирование модуля `cust-ibank-check-files`

---

## 📄 Лицензия

Свободное использование в рамках тестирования.
