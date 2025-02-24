import pytest
import sys
import tempfile
import os
from pathlib import Path

root_dir = Path(__file__).parent.parent
sys.path.insert(0, str(root_dir))

@pytest.fixture
def temp_db_file():
    # テスト用の一時データベースファイル作成
    with tempfile.NamedTemporaryFile(delete=False) as f:
        temp_path = f.name
    yield temp_path
    # テスト後にファイル削除
    os.unlink(temp_path)

@pytest.fixture
def test_data_path():
    # テストデータ格納用のパス
    return Path(__file__).parent / "data"
