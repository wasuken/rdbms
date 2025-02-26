import pytest
from rdbms.slot_array import SlotArray
from rdbms.slot import Slot

def test_slot_array_init():
    slot_array = SlotArray([])
    assert len(slot_array.slots) == 0

    slot_array = SlotArray([Slot(100, 200, False)])
    assert len(slot_array.slots) == 1

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

@pytest.mark.xfail(reason="未実装")
def test_update_slot():
    assert False

@pytest.mark.xfail(reason="未実装")
def test_serialize():
    assert False

@pytest.mark.xfail(reason="未実装")
def test_deserialize():
    assert False
