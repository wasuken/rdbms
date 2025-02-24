import  struct
from rdbms.types import PageType

class PageHeader:
    self.page_id: int = 0
    self.free_space_offset: int = 0
    self.record_count: int = 0
    self.page_type = PageType.PAGE_SIZE
    self.next_free_page = 0

    def serialize():
        return struct.pack('>iiiii', self.page_id, self.free_space_offset, self.record_count, self.page_type, self.next_free_page)


    def deserialize():
        return struct.unpack('>i', value)[0]


    def update_free_space(data: bytes):
        raise NotImplementedError()

    def increment_record_count():
        raise NotImplementedError()

    def decrement_record_count():
        raise NotImplementedError()
