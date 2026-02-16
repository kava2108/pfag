"""
Integration Test: 一時ファイル削除API/自動削除
T019: 削除API/自動削除の統合テスト
"""
import pytest
from fastapi.testclient import TestClient
from src.pfag.api.main import app
import shutil
import os
import time

client = TestClient(app)

def setup_module(module):
    # テスト用一時ディレクトリに古いPDFを作成
    tmp_dir = "/tmp/pfag_pdf"
    os.makedirs(tmp_dir, exist_ok=True)
    old_file = os.path.join(tmp_dir, "old.pdf")
    with open(old_file, "wb") as f:
        f.write(b"dummy")
    old_time = time.time() - 2 * 86400
    os.utime(old_file, (old_time, old_time))
    # 新しいファイル
    new_file = os.path.join(tmp_dir, "new.pdf")
    with open(new_file, "wb") as f:
        f.write(b"dummy")

def test_cleanup_tmp_files_api():
    # API経由で一時ファイル削除を呼び出す（仮: /pdf/cleanup）
    response = client.post("/pdf/cleanup")
    assert response.status_code == 200
    # old.pdfは削除され、new.pdfは残る
    tmp_dir = "/tmp/pfag_pdf"
    assert not os.path.exists(os.path.join(tmp_dir, "old.pdf"))
    assert os.path.exists(os.path.join(tmp_dir, "new.pdf"))
