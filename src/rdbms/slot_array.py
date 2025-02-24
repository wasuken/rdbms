import struct

class SlotArray:
    def __init__(self, slots: list<Slot>):
        self.slots = slots

    def add_slot(self, slot: Slot) -> int:
        self.slots.append(slot)
        slot_id = len(self.slots)
        return slot_id

    def delete_list(self, slot_id: int):
        if slot_id < 0 or >= len(self.slots):
            raise ValueError('Invalid slot_id: {slot_id}')

        return self.slots[slot_id]

    def update_slot(self, slot_id: int, offset: int, length, is_active: boolean):
        if slot_id < 0 or >= len(self.slots):
            raise ValueError('Invalid slot_id: {slot_id}')

        t_slot = self.slots[slot_id]
        t_slot.offset = offset
        t_slot.length = length
        t_slot.is_active = is_active
