import struct
import pytest
from rdbms.slot_array import SlotArray
from rdbms.slot import Slot

def test_slot_array_init():
    slot_array = SlotArray([])
    assert len(slot_array.slots) == 0

    slot_array = SlotArray([Slot(100, 200, False)])
    assert len(slot_array.slots) == 1


def test_find_free_slot():
    slot_array = SlotArray([Slot(100, 200, True), Slot(500, 200, False), Slot(100, 200, False)])
    assert(slot_array.find_free_slot() != None)

def test_get_slot():
    slot_array = SlotArray([Slot(100, 200, False)])
    assert(slot_array.get_slot(0) != None)

    slot_array = SlotArray([])
    with pytest.raises(ValueError) as e:
        slot_array.get_slot(0)
        assert str(e.value) == "Invalid slot_id: 0"

def test_add_slot():
    slot_array = SlotArray([])
    slot_id = slot_array.add_slot(Slot(100, 200, False))
    assert(slot_id == 0)

def test_delete_slot():
    slot_array = SlotArray([Slot(100, 200, False), Slot(100, 300, False)])
    slot_array.delete_slot(0)
    target = slot_array.get_slot(0)
    assert(target.serialize() == Slot(100, 300, False).serialize())

def test_get_slot_array_size():
    slot_array = SlotArray([Slot(100, 200, False), Slot(100, 300, False)])
    assert slot_array.get_slot_array_size() == 14

def test_update_slot():
    slot_array = SlotArray([Slot(100, 200, False), Slot(100, 300, False)])
    slot_array.update_slot(0, 300, 400, True)
    target = slot_array.get_slot(0)
    assert(target.serialize() == Slot(300, 400, True).serialize())

def test_serialize():
    target = SlotArray([Slot(100, 200, False), Slot(100, 300, True)])
    expected = b'' + struct.pack('>i', 2) \
        + Slot(100, 200, False).serialize() \
        + Slot(100, 300, True).serialize()
    assert(target.serialize() == expected)

def test_deserialize():
    origin = SlotArray([Slot(100, 200, False), Slot(100, 300, True)])
    assert(origin.serialize() == SlotArray.deserialize(origin.serialize()).serialize())
    assert(origin.serialize() == SlotArray.deserialize(SlotArray.deserialize(origin.serialize()).serialize()).serialize())

