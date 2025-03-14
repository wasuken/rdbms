from rdbms.page_header import PageHeader
from rdbms.slot_array import SlotArray
from rdbms.types import PAGE_HEADER_ENTRY_SIZE, PAGE_SIZE

class Page:
    def __init__(self, page_id: int = 0, data: bytearray = [], header: PageHeader = None, slot_array: SlotArray = None):
        self.page_id: int = page_id
        self.data: bytearray = data
        self.header: PageHeader = header if header is not None else PageHeader()
        self.slot_array: SlotArray = slot_array if slot_array is not None else SlotArray()

    def get_record(self, slot_id: int) -> bytes:
        return self.data[slot_id]

    def add_record(self, record: bytes) -> int:
        self.data.append(record)

    def delete_record(self, slot_id: int) -> bytes:
        return self.data.pop(slot_id)

    def update_record(self, slot_id: int, record: bytes) -> bytes:
        old = self.data[slot_id]
        self.data[slot_id] = record
        return old

    def get_free_space(self) -> int:
        page_size = len(self.data)
        slot_array_size = self.slot_array.get_slot_array_size()
        used_size = PAGE_HEADER_ENTRY_SIZE + slot_array_size
        if self.header.free_space_offset > used_size:
            # free_space_offsetがヘッダとスロット配列の合計サイズより大きい場合、
            # その差分がデータ領域の実際のサイズ
            used_size = self.header.free_space_offset

        return PAGE_SIZE - used_size

    def calc_total_used_size(self) -> int:
        data_size = self.get_free_space() + \
            aPAGE_HEADER_ENTRY_SIZE + \
            self.slot_array.get_slot_array_size()

    def compact_page(self):
        raise NotImplementedError()

    def find_free_slot(self) -> int:
        raise NotImplementedError()

    def validate_slot_id(self, slot_id: int) -> bool:
        return self.slot_array.check_slot_id(slot_id)

    def serialise(self) -> bytes:
        raise NotImplementedError()

    @classmethod
    def deserialise(cls) -> 'Page':
        raise NotImplementedError()
