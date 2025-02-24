from enum import Enum

PAGE_SIZE = 8192
HEADER_SIZE = 16
SLOT_SIZE = 4

class PageType(enum):
    # 通常のテーブルデータを格納するページ
    PAGE_SIZE = 1
    # インデックスページ
    INDEX_PAGE = 2
    # レコードサイズがページサイズをこえる場合の追加ページ
    OVERFLOW_PAGE = 3
