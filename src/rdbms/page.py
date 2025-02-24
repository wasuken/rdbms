from enum import Enum

class Page:
    self.page_id: int = 0
    self.data: bytearray = []
    self.header: PageHeader = None
    self.slot_array: SlotArray = None

    def get_record(slot_id: int) -> bytes:
        raise NotImplementedError()

    def insert_record(record: bytes) -> int:
        raise NotImplementedError()

    def delete_record(slot_id: int) -> bytes:
        raise NotImplementedError()

    def update_record(slot_id: int, record: bytes) -> bytes:
        raise NotImplementedError()

    def get_free_space() -> int:
        raise NotImplementedError()

    def serialise() -> bytes:
        raise NotImplementedError()

    def deserialise() -> bytes:
        raise NotImplementedError()

    def compact_page():
        raise NotImplementedError()

    def find_free_slot() -> int:
        raise NotImplementedError()

    def validate_slot_id(slot_id: int) -> boolean:
        raise NotImplementedError()
