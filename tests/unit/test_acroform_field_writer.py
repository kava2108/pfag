"""
Unit Test: AcroformFieldWriter
T015: フィールド埋め込み関数の単体テスト
"""
import pytest
from pfag.core.acroform_field_writer import AcroformFieldWriter
from PyPDF2 import PdfReader
import io

@pytest.fixture
def minimal_pdf_bytes():
    # 有効な1ページPDFバイナリ
    return (
        b"%PDF-1.4\n1 0 obj\n<< /Type /Catalog /Pages 2 0 R >>\nendobj\n"
        b"2 0 obj\n<< /Type /Pages /Kids [3 0 R] /Count 1 >>\nendobj\n"
        b"3 0 obj\n<< /Type /Page /Parent 2 0 R /MediaBox [0 0 300 300] >>\nendobj\n"
        b"xref\n0 4\n0000000000 65535 f \n0000000010 00000 n \n0000000060 00000 n \n0000000117 00000 n \n"
        b"trailer\n<< /Root 1 0 R /Size 4 >>\nstartxref\n178\n%%EOF\n"
    )

def test_write_fields_returns_pdf(minimal_pdf_bytes):
    fields = [
        {"name": "field1", "type": "Tx", "page": 1, "rect": [10, 10, 100, 30], "options": {"value": "abc"}}
    ]
    out_bytes = AcroformFieldWriter.write_fields(minimal_pdf_bytes, fields)
    assert out_bytes[:4] == b"%PDF"
    reader = PdfReader(io.BytesIO(out_bytes))
    assert len(reader.pages) == 1
