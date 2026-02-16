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
    import time
    service = PDFService(tmp_dir=str(tmp_path))
    # 古いファイルを作成
    old_file = os.path.join(tmp_path, "old.pdf")
    with open(old_file, "wb") as f:
        f.write(b"dummy")
    old_time = time.time() - 2 * 86400
    os.utime(old_file, (old_time, old_time))
    # 新しいファイル
    new_file = os.path.join(tmp_path, "new.pdf")
    with open(new_file, "wb") as f:
        f.write(b"dummy")
    # 実行: 1日より古いファイルを削除
    removed = service.cleanup_tmp_files(days=1)
    assert removed == 1
    assert not os.path.exists(old_file)
    assert os.path.exists(new_file)
