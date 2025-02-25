import pytest
from rdbms.slot_array import SlotArray
from rdbms.slot import Slot

def test_slot_array_init():
    slot_array = SlotArray([])
    assert len(slot_array.slots) == 0

    slot_array = SlotArray([Slot(100, 200, False)])
    assert len(slot_array.slots) == 1

def test_add_slot():
    pass

def test_delete_slot():
    pass

def test_update_slot():
    pass

def test_get_slot():
    pass

def test_serialize():
    pass


def test_deserialize():
    pass
