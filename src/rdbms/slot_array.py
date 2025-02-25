import struct
from rdbms.slot import Slot

class SlotArray:
    def __init__(self, slots: list['Slot'] = []):
        self.slots = slots


    def get_slot(self, slot_id: int) -> 'Slot':
        if slot_id < 0 >= len(self.slots):
            raise ValueError('Invalid slot_id: {slot_id}')
        return self.slots[slot_id]


    def add_slot(self, slot: 'Slot') -> int:
        self.slots.append(slot)
        slot_id = len(self.slots)
        return slot_id

    def delete_list(self, slot_id: int):
        if slot_id < 0 >= len(self.slots):
            raise ValueError('Invalid slot_id: {slot_id}')

        return self.slots[slot_id]

    def update_slot(self, slot_id: int, offset: int, length, is_active: bool):
        if slot_id < 0 >= len(self.slots):
            raise ValueError('Invalid slot_id: {slot_id}')

        t_slot = self.slots[slot_id]
        t_slot.offset = offset
        t_slot.length = length
        t_slot.is_active = is_active

    def serialize(self):
        header = struct.pack('>i', len(self.slots))
        serial = b''
        for slot in self.slots:
            serial += slot.serialize()

        return header + serial

    @classmethod
    def deserialize(cls, data: bytes) -> list['Slot']:
        slot_count = struct.unpack('>i', data[:4])[0]
        slot_array = cls()
        slot_size = 5

        for i in range(slot_count):
            start = 4 + (i * slot_size)
            end = start + slot_size
            slot_array.add_slot(Slot.deserialize(data[start:end]))

        return slot_array

