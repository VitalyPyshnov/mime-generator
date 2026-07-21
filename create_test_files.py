#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Скрипт для создания тестовых файлов для проверки MIME и расширений
"""

import os


def create_test_files():
    """Создает все необходимые тестовые файлы"""

    # Создаем папку если её нет
    os.makedirs("test_files", exist_ok=True)

    print("Начинаем создание тестовых файлов...")
    print("=" * 50)

    # ============================================
    # 1. КОРРЕКТНЫЕ ФАЙЛЫ (Правильный MIME + Расширение)
    # ============================================
    print("\n1. Создаем корректные файлы:")

    # 1.1. PDF файл
    with open("test_files/correct.pdf", "w", encoding='utf-8') as f:
        f.write("%PDF-1.4\n")
        f.write("1 0 obj<</Type/Catalog>>endobj\n")
        f.write("trailer<<>>\n")
    print("  ✓ correct.pdf")

    # 1.2. PNG файл
    with open("test_files/correct.png", "wb") as f:
        f.write(b'\x89PNG\r\n\x1a\n')
        f.write(b'\x00\x00\x00\rIHDR')
    print("  ✓ correct.png")

    # 1.3. JPG файл
    with open("test_files/correct.jpg", "wb") as f:
        f.write(b'\xFF\xD8\xFF\xE0\x00\x10JFIF\x00')
    print("  ✓ correct.jpg")

    # 1.4. TXT файл
    with open("test_files/correct.txt", "w", encoding='utf-8') as f:
        f.write("This is a simple text file for testing.\n")
        f.write("Line 2: testing content.\n")
    print("  ✓ correct.txt")

    # 1.5. GIF файл
    with open("test_files/correct.gif", "wb") as f:
        f.write(b'GIF89a')
    print("  ✓ correct.gif")

    # 1.6. ZIP файл
    with open("test_files/correct.zip", "wb") as f:
        f.write(b'PK\x03\x04')
    print("  ✓ correct.zip")

    # 1.7. XML файл
    with open("test_files/correct.xml", "w", encoding='utf-8') as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write('<root><test>content</test></root>\n')
    print("  ✓ correct.xml")

    # 1.8. JSON файл
    with open("test_files/correct.json", "w", encoding='utf-8') as f:
        f.write('{"name": "test", "value": 123}\n')
    print("  ✓ correct.json")

    # 1.9. DOCX файл (простая заглушка)
    with open("test_files/correct.docx", "wb") as f:
        f.write(b'PK\x03\x04')  # DOCX - это ZIP
    print("  ✓ correct.docx")

    # 1.10. XLSX файл
    with open("test_files/correct.xlsx", "wb") as f:
        f.write(b'PK\x03\x04')
    print("  ✓ correct.xlsx")

    # ============================================
    # 2. ФАЙЛЫ С ПОДМЕНОЙ СОДЕРЖИМОГО (fake MIME)
    # ============================================
    print("\n2. Создаем файлы с подменой содержимого:")

    html_content = """<!DOCTYPE html>
<html>
<head><title>Fake File</title></head>
<body>
<h1>This is HTML content, not a real file!</h1>
<p>Testing MIME detection bypass.</p>
</body>
</html>"""

    # HTML с расширением PDF
    with open("test_files/fake.pdf", "w", encoding='utf-8') as f:
        f.write(html_content)
    print("  ✓ fake.pdf (HTML content)")

    # HTML с расширением PNG
    with open("test_files/fake.png", "w", encoding='utf-8') as f:
        f.write(html_content)
    print("  ✓ fake.png (HTML content)")

    # HTML с расширением JPG
    with open("test_files/fake.jpg", "w", encoding='utf-8') as f:
        f.write(html_content)
    print("  ✓ fake.jpg (HTML content)")

    # HTML с расширением GIF
    with open("test_files/fake.gif", "w", encoding='utf-8') as f:
        f.write(html_content)
    print("  ✓ fake.gif (HTML content)")

    # HTML с расширением TXT
    with open("test_files/fake.txt", "w", encoding='utf-8') as f:
        f.write(html_content)
    print("  ✓ fake.txt (HTML content)")

    # ============================================
    # 3. ОПАСНЫЕ РАСШИРЕНИЯ (для DANG_EXPANSION)
    # ============================================
    print("\n3. Создаем файлы с опасными расширениями:")

    dangerous_extensions = [
        ("malware.exe", "MZ\x90\x00\x03\x00\x00\x00\x04\x00"),
        ("script.bat", "@echo off\r\necho This is a BAT file\r\npause\r\n"),
        ("runner.sh", "#!/bin/bash\necho 'This is a shell script'\n"),
        ("payload.js", "alert('This is JavaScript');\n"),
        ("script.vbs", "MsgBox 'This is VBScript'\n"),
        ("script.ps1", "Write-Host 'This is PowerShell script'\n"),
        ("virus.com", b'\xE9\x00\x00\x00'),
        ("malware.dll", "MZ\x90\x00\x03\x00\x00\x00\x04\x00"),
        ("dangerous.scr", "MZ\x90\x00"),
        ("virus.pif", "MZ\x90\x00"),
        ("bad.cmd", "@echo off\r\necho This is a CMD file\r\n"),
        ("evil.jar", b'\x50\x4B\x03\x04'),
        ("malware.msi", b'\xD0\xCF\x11\xE0\xA1\xB1\x1A\xE1'),
        ("trojan.bat", "@echo off\r\necho Trojan test\r\n"),
    ]

    for name, content in dangerous_extensions:
        with open(f"test_files/{name}", "wb") as f:
            if isinstance(content, str):
                f.write(content.encode('utf-8'))
            else:
                f.write(content)
        print(f"  ✓ {name}")

    # ============================================
    # 4. ФАЙЛЫ С ДВОЙНЫМ РАСШИРЕНИЕМ
    # ============================================
    print("\n4. Создаем файлы с двойными расширениями:")

    double_extensions = [
        ("document.pdf.exe", "EXE file disguised as PDF"),
        ("image.png.exe", "EXE file disguised as PNG"),
        ("archive.zip.exe", "EXE file disguised as ZIP"),
        ("file.txt.pdf", "PDF disguised as TXT"),
        ("data.xml.exe", "EXE disguised as XML"),
        ("backup.tar.gz.exe", "EXE with double extension"),
        ("virus.jpg.exe", "EXE with JPG extension"),
    ]

    for name, content in double_extensions:
        with open(f"test_files/{name}", "w", encoding='utf-8') as f:
            f.write(content)
        print(f"  ✓ {name}")

    # ============================================
    # 5. ФАЙЛЫ БЕЗ РАСШИРЕНИЯ
    # ============================================
    print("\n5. Создаем файлы без расширения:")

    no_extensions = [
        ("noextension", "File without any extension"),
        (".hiddenfile", "Hidden file with leading dot"),
        ("file_without_dot", "Another file without extension"),
        ("_nodot", "File starting with underscore, no dot"),
    ]

    for name, content in no_extensions:
        with open(f"test_files/{name}", "w", encoding='utf-8') as f:
            f.write(content)
        print(f"  ✓ {name}")

    # ============================================
    # 6. ФАЙЛЫ С НЕСКОЛЬКИМИ ТОЧКАМИ
    # ============================================
    print("\n6. Создаем файлы с несколькими точками в имени:")

    multi_dot_files = [
        ("my.document.final.pdf", "%PDF-1.4\nContent with multiple dots"),
        ("image.main.background.png", "PNG content with multiple dots"),
        ("backup.2024.01.15.zip", "ZIP backup with date in name"),
        ("project.v1.2.3.tar.gz", "TAR.GZ with version"),
        ("file.name.with.many.dots.txt", "Many dots in filename"),
    ]

    for name, content in multi_dot_files:
        with open(f"test_files/{name}", "w", encoding='utf-8') as f:
            f.write(content)
        print(f"  ✓ {name}")

    # ============================================
    # 7. ФАЙЛЫ С РАЗНЫМИ РЕГИСТРАМИ
    # ============================================
    print("\n7. Создаем файлы с разными регистрами:")

    case_files = [
        ("test.PDF", "%PDF-1.4\nPDF with uppercase extension"),
        ("image.PNG", "PNG with uppercase extension"),
        ("photo.JPG", "JPG with uppercase extension"),
        ("document.PdF", "%PDF-1.4\nPDF with mixed case"),
        ("image.PnG", "PNG with mixed case"),
        ("text.TXT", "TXT with uppercase"),
        ("file.Js", "JS with mixed case"),
    ]

    for name, content in case_files:
        with open(f"test_files/{name}", "w", encoding='utf-8') as f:
            f.write(content)
        print(f"  ✓ {name}")

    # ============================================
    # 8. БИНАРНЫЕ ФАЙЛЫ
    # ============================================
    print("\n8. Создаем бинарные файлы:")

    # DOC файл (старый формат)
    with open("test_files/test.doc", "wb") as f:
        f.write(b'\xD0\xCF\x11\xE0\xA1\xB1\x1A\xE1')
    print("  ✓ test.doc")

    # XLS файл
    with open("test_files/test.xls", "wb") as f:
        f.write(b'\xD0\xCF\x11\xE0\xA1\xB1\x1A\xE1')
    print("  ✓ test.xls")

    # PPT файл
    with open("test_files/test.ppt", "wb") as f:
        f.write(b'\xD0\xCF\x11\xE0\xA1\xB1\x1A\xE1')
    print("  ✓ test.ppt")

    # RTF файл
    with open("test_files/test.rtf", "w", encoding='utf-8') as f:
        f.write(r'{\rtf1\ansi\deff0 {\fonttbl {\f0 Times New Roman;}} \f0\fs20 Hello!}')
    print("  ✓ test.rtf")

    # ============================================
    # 9. СПЕЦИАЛЬНЫЕ ФАЙЛЫ ДЛЯ ГРАНИЧНЫХ СЛУЧАЕВ
    # ============================================
    print("\n9. Создаем файлы для граничных случаев:")

    # Пустой файл
    with open("test_files/empty.pdf", "wb") as f:
        pass
    print("  ✓ empty.pdf (0 bytes)")

    # Очень маленький файл
    with open("test_files/small.pdf", "w") as f:
        f.write("%PDF")
    print("  ✓ small.pdf (4 bytes)")

    # Файл с очень длинным именем
    long_name = "this_is_a_very_long_filename_with_extension_" + "x" * 100 + ".pdf"
    with open(f"test_files/{long_name}", "w") as f:
        f.write("%PDF-1.4\nLong filename test")
    print(f"  ✓ {long_name[:50]}... (long filename)")

    # Файл с пробелами в имени
    with open("test_files/my test file with spaces.pdf", "w") as f:
        f.write("%PDF-1.4\nSpaces in filename")
    print("  ✓ my test file with spaces.pdf")

    # Файл с кириллицей в имени
    try:
        with open("test_files/тестовый_файл.pdf", "w", encoding='utf-8') as f:
            f.write("%PDF-1.4\nCyrillic filename")
        print("  ✓ тестовый_файл.pdf")
    except:
        print("  ⚠ тестовый_файл.pdf (пропущен - возможно проблемы с кодировкой)")

    # Файл с кириллицей в содержимом
    with open("test_files/cyrillic_content.txt", "w", encoding='utf-8') as f:
        f.write("Привет мир! Это текст на кириллице.\n")
        f.write("Hello world! This is text in Cyrillic.\n")
    print("  ✓ cyrillic_content.txt")

    # ============================================
    # ИТОГО
    # ============================================
    print("\n" + "=" * 50)
    total_files = len(os.listdir("test_files"))
    print(f"✅ Всего создано файлов: {total_files}")
    print(f"📁 Папка: {os.path.abspath('test_files')}")

    # Выводим список всех файлов по категориям
    print("\n📋 Категории созданных файлов:")
    print("-" * 50)

    # Группируем файлы
    categories = {
        "📄 Корректные": ["correct", "test.doc", "test.xls", "test.ppt", "test.rtf", "cyrillic_content"],
        "⚠️ Fake MIME": ["fake"],
        "🔴 Опасные": ["malware", "script", "runner", "payload", "virus", "dangerous", "bad", "evil", "trojan"],
        "🔄 Двойные расширения": [".exe", ".pdf.exe", ".png.exe", ".zip.exe", ".txt.pdf", ".xml.exe"],
        "🔍 Без расширения": ["noextension", "hiddenfile", "file_without_dot", "_nodot"],
        "📝 Много точек": ["my.document", "image.main", "backup.2024", "project.v1"],
        "🔤 Регистры": [".PDF", ".PNG", ".JPG", ".PdF", ".PnG", ".TXT", ".Js"],
        "⚡ Граничные": ["empty", "small", "with spaces", "long_filename"],
    }

    for category, patterns in categories.items():
        files = []
        for pattern in patterns:
            for file in os.listdir("test_files"):
                if pattern.lower() in file.lower():
                    files.append(file)
        if files:
            print(f"\n{category}:")
            for file in sorted(files)[:5]:  # Показываем первые 5
                size = os.path.getsize(f"test_files/{file}")
                print(f"    • {file:<40} ({size} байт)")
            if len(files) > 5:
                print(f"    ... и еще {len(files) - 5} файлов")

    print("\n" + "=" * 50)
    print("✅ Готово! Файлы созданы для тестирования.")
    print("\n💡 Рекомендуемые тестовые сценарии:")
    print("  1. Проверить correct.pdf при MIME=application/pdf и WHITE=pdf")
    print("  2. Проверить fake.pdf при MIME=image/png (должен быть отклонен)")
    print("  3. Проверить malware.exe при DANG_EXPANSION=exe (должен быть отклонен)")
    print("  4. Проверить noextension (должен быть отклонен при проверке расширения)")
    print("  5. Проверить test.PDF (регистронезависимость)")
    print("  6. Проверить document.pdf.exe (извлечение по последней точке)")

# Запускаем функцию
if __name__ == "__main__":
    create_test_files()