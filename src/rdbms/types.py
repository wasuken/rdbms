from enum import Enum

PAGE_SIZE = 8192
HEADER_SIZE = 16
SLOT_SIZE = 4

PAGE_HEADER_ENTRY_SIZE = 16
SLOT_ARRAY_HEADER_SIZE = 4
SLOT_ENTRY_SIZE = 5

class PageType(Enum):
    # 通常のテーブルデータを格納するページ
    DATA_PAGE = 1
    # インデックスページ
    INDEX_PAGE = 2
    # レコードサイズがページサイズをこえる場合の追加ページ
    OVERFLOW_PAGE = 3
