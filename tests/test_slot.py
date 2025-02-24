import pytest
from rdbms.slot import Slot

def test_slot_init():
    # デフォルト値でのインスタンス化テスト
    slot = Slot()
    assert slot.offset == 0
    assert slot.length == 0
    assert slot.is_active == True

    # 値を指定してのインスタンス化テスト
    slot = Slot(100, 200, False)
    assert slot.offset == 100
    assert slot.length == 200
    assert slot.is_active == False

def test_slot_serialize():
    # シリアライズのテスト
    slot = Slot(100, 200, True)
    data = slot.serialize()
    # バイナリデータの長さチェック (short+short+bool)
    assert len(data) == 5

    # 正しい値が含まれているか確認
    import struct
    offset, length, is_active = struct.unpack('>hh?', data)
    assert offset == 100
    assert length == 200
    assert is_active == True

def test_slot_deserialize():
    # デシリアライズのテスト
    import struct
    # テスト用データの作成
    data = struct.pack('>hh?', 150, 250, False)

    # デシリアライズして新しいインスタンスを取得
    slot = Slot.deserialize(data)

    # 値のチェック
    assert slot.offset == 150
    assert slot.length == 250
    assert slot.is_active == False

def test_slot_roundtrip():
    # シリアライズ→デシリアライズの一貫性テスト
    original = Slot(300, 400, True)
    data = original.serialize()
    restored = Slot.deserialize(data)

    assert restored.offset == original.offset
    assert restored.length == original.length
    assert restored.is_active == original.is_active
