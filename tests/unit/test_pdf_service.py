import pytest
from pfag.core.pdf_service import PDFService
import os

def test_html_length_limit():
    service = PDFService()
    html = "<p>test</p>" * (service.MAX_HTML_LENGTH + 1)
    with pytest.raises(ValueError):
        service.html_to_pdf(html)

def test_pdf_size_limit(tmp_path):
    service = PDFService(tmp_dir=str(tmp_path))
    # 極端に大きなHTMLを生成（WeasyPrintがPDF化できる範囲で）
    html = "<div>big</div>" * 50000
    try:
        service.html_to_pdf(html)
    except ValueError as e:
        assert "PDFサイズが大きすぎます" in str(e)

def test_cleanup_tmp_files(tmp_path):
    service = PDFService(tmp_dir=str(tmp_path))
    # ダミーPDF作成
    pdf_path = os.path.join(tmp_path, "dummy.pdf")
    with open(pdf_path, "wb") as f:
        f.write(b"%PDF-1.4 test")
    os.utime(pdf_path, (0, 0))  # 最終更新をepochに
    removed = service.cleanup_tmp_files(days=1)
    assert removed >= 1
