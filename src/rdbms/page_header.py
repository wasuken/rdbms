import  struct
from rdbms.types import PageType, PAGE_SIZE, PAGE_HEADER_ENTRY_SIZE

class PageHeader:
    def __init__(self, page_id: int = 0, free_space_offset: int = -1, record_count: int = 0, page_type: PageType = PageType.DATA_PAGE, next_free_page: int = 0):
        self.page_id: int = page_id
        self.free_space_offset: int = free_space_offset
        self.record_count: int = record_count
        self.page_type: PageType = page_type
        self.next_free_page: int = next_free_page

    def serialize(self):
        return struct.pack('>ihhii', self.page_id, self.free_space_offset, self.record_count, self.page_type.value, self.next_free_page)

    @classmethod
    def deserialize(cls, data: bytes):
        page_id, free_space_offset, record_count, page_type, next_free_page = struct.unpack('>ihhii', data)
        return cls(page_id,
                   free_space_offset,
                   record_count,
                   PageType(page_type),
                   next_free_page)

    def update_free_space(self, offset: int):
        if 0 <= offset < PAGE_SIZE:
            self.free_space_offset = offset

    def increment_record_count(self):
        self.record_count += 1

    def decrement_record_count(self):
        self.record_count -= 1
