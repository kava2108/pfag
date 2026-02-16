# pfag Development Guidelines

Auto-generated from all feature plans. Last updated: 2026-02-14

## Active Technologies
- Python 3.11 + OpenCV, NumPy, PyMuPDF, Pillow, FastAPI (004-checkbox-detection)
- N/A（ファイル入出力のみ） (004-checkbox-detection)
- Python 3.11 + Pillow (PIL), PyPDF2, numpy (005-coordinate-conversion)
- N/A（座標変換のみ） (005-coordinate-conversion)
- Python 3.11 + FastAPI, PyPDF2, WeasyPrint, Pillow, numpy (006-acroform-field-generation)
- ファイル一時保存（永続DBなし） (006-acroform-field-generation)

- Python 3.8+ + FastAPI, uvicorn (001-fastapi-api-server-init)

## Project Structure

```text
src/
tests/
```

## Commands

cd src [ONLY COMMANDS FOR ACTIVE TECHNOLOGIES][ONLY COMMANDS FOR ACTIVE TECHNOLOGIES] pytest [ONLY COMMANDS FOR ACTIVE TECHNOLOGIES][ONLY COMMANDS FOR ACTIVE TECHNOLOGIES] ruff check .

## Code Style

Python 3.8+: Follow standard conventions

## Recent Changes
- 006-acroform-field-generation: Added Python 3.11 + FastAPI, PyPDF2, WeasyPrint, Pillow, numpy
- 005-coordinate-conversion: Added Python 3.11 + Pillow (PIL), PyPDF2, numpy
- 004-checkbox-detection: Added Python 3.11 + OpenCV, NumPy, PyMuPDF, Pillow, FastAPI


<!-- MANUAL ADDITIONS START -->
<!-- MANUAL ADDITIONS END -->
