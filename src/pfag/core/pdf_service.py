
import os
import json
from tempfile import gettempdir
from typing import Optional, List, Dict
from datetime import datetime


class PDFService:
    MAX_HTML_LENGTH = 100_000  # 例: 10万文字まで
    MAX_PDF_SIZE = 10 * 1024 * 1024  # 例: 10MB
    """
    PDF生成・管理サービス
    - HTML→PDF変換
    - 一時保存ディレクトリ管理
    - 履歴管理
    - PDFファイル取得
    """
    HISTORY_FILE = "pdf_history.json"

    def __init__(self, tmp_dir: Optional[str] = None) -> None:
        self.tmp_dir: str = tmp_dir or os.path.join(gettempdir(), "pfag_pdf")
        os.makedirs(self.tmp_dir, exist_ok=True)

    def get_tmp_dir(self) -> str:
        """一時保存ディレクトリのパスを返す"""
        return self.tmp_dir

    def html_to_pdf(self, html: str, out_filename: Optional[str] = None) -> str:
        """
        HTML文字列をPDFに変換し、一時ディレクトリに保存する。
        :param html: HTMLデータ
        :param out_filename: 保存ファイル名（省略時は自動生成）
        :return: 保存先ファイルパス
        """
        from weasyprint import HTML
        import uuid
        if not html or not html.strip():
            raise ValueError("HTMLデータが空です")
        if len(html) > self.MAX_HTML_LENGTH:
            raise ValueError(f"HTMLデータが長すぎます（最大{self.MAX_HTML_LENGTH}文字）")
        if out_filename is None:
            out_filename = f"pdf_{uuid.uuid4().hex}.pdf"
        out_path = os.path.join(self.tmp_dir, out_filename)
        HTML(string=html).write_pdf(out_path)
        # PDFサイズ制限
        if os.path.getsize(out_path) > self.MAX_PDF_SIZE:
            os.remove(out_path)
            raise ValueError(f"PDFサイズが大きすぎます（最大{self.MAX_PDF_SIZE // (1024*1024)}MB）")
        # 履歴保存
        self._save_history_entry(out_filename)
        return out_path

    def cleanup_tmp_files(self, days: int = 7) -> int:
        """
        一時ディレクトリ内の古いPDF/履歴ファイルを削除（デフォルト7日より前のもの）
        :param days: 削除対象日数
        :return: 削除したファイル数
        """
        import time
        now = time.time()
        removed = 0
        for fname in os.listdir(self.tmp_dir):
            if fname.endswith('.pdf') or fname == self.HISTORY_FILE:
                fpath = os.path.join(self.tmp_dir, fname)
                try:
                    if now - os.path.getmtime(fpath) > days * 86400:
                        os.remove(fpath)
                        removed += 1
                except Exception:
                    pass
        return removed

    def _save_history_entry(self, filename: str) -> None:
        """履歴ファイルにエントリを追加"""
        history_path = os.path.join(self.tmp_dir, self.HISTORY_FILE)
        entry = {
            "id": filename,
            "created_at": datetime.now().isoformat(),
            "filename": filename
        }
        try:
            if os.path.exists(history_path):
                with open(history_path, "r", encoding="utf-8") as f:
                    history = json.load(f)
            else:
                history = []
        except Exception:
            history = []
        history.append(entry)
        with open(history_path, "w", encoding="utf-8") as f:
            json.dump(history, f, ensure_ascii=False, indent=2)

    def get_history(self) -> List[Dict]:
        """PDF生成履歴一覧を返す"""
        history_path = os.path.join(self.tmp_dir, self.HISTORY_FILE)
        try:
            if os.path.exists(history_path):
                with open(history_path, "r", encoding="utf-8") as f:
                    return json.load(f)
            else:
                return []
        except Exception:
            return []

    def get_pdf_file(self, pdf_id: str) -> str:
        """
        指定IDのPDFファイルパスを返す。存在しない場合はFileNotFoundError。
        :param pdf_id: PDFファイル名 or ID
        :return: ファイルパス
        """
        if not pdf_id or not isinstance(pdf_id, str):
            raise ValueError("PDF IDが不正です")
        pdf_path = os.path.join(self.tmp_dir, pdf_id)
        if not os.path.isfile(pdf_path):
            raise FileNotFoundError(f"PDFファイルが見つかりません: {pdf_id}")
        return pdf_path
