import struct
from rdbms.slot import Slot
from rdbms.types import SLOT_ENTRY_SIZE, SLOT_ARRAY_HEADER_SIZE

class SlotArray:
    def __init__(self, slots: list[Slot] = []):
        self.slots = slots

    def find_free_slot(self) -> int:
        for i, slot in enumerate(self.slots):
            if not slot.is_active:
                return i

        self.add_slot(Slot())

    def check_slot_id(self, slot_id: int):
        if slot_id < 0 or slot_id >= len(self.slots):
            raise ValueError('Invalid slot_id: {slot_id}')

    def get_slot(self, slot_id: int) -> Slot | None:
        self.check_slot_id(slot_id)

        return self.slots[slot_id]

    def add_slot(self, slot: Slot) -> int:
        slot_id = len(self.slots)
        self.slots.append(slot)
        return slot_id

    def delete_slot(self, slot_id: int):
        self.check_slot_id(slot_id)

        return self.slots.pop(slot_id)

    def update_slot(self, slot_id: int, offset: int, length: int, is_active: bool):
        self.check_slot_id(slot_id)

        t_slot = self.slots[slot_id]
        t_slot.offset = offset
        t_slot.length = length
        t_slot.is_active = is_active


    def get_slot_array_size(self):
        return SLOT_ARRAY_HEADER_SIZE + (len(self.slots) * SLOT_ENTRY_SIZE)

    def serialize(self):
        header = struct.pack('>i', len(self.slots))
        serial = b''
        for slot in self.slots:
            serial += slot.serialize()

        return header + serial

    @classmethod
    def deserialize(cls, data: bytes) -> 'SlotArray':
        slot_count = struct.unpack('>i', data[:4])[0]
        slot_size = 5
        slots = []

        for i in range(slot_count):
            start = 4 + (i * slot_size)
            end = start + slot_size
            slots.append(Slot.deserialize(data[start:end]))

        return cls(slots)

