import pytest
from rdbms.slot_array import SlotArray
from rdbms.slot import Slot

def test_slot_array_init():
    slot_array = SlotArray([])
    assert len(slot_array.slots) == 0

    slot_array = SlotArray([Slot(100, 200, False)])
    assert len(slot_array.slots) == 1

@pytest.mark.xfail(reason="未実装")
def test_add_slot():
    assert False

@pytest.mark.xfail(reason="未実装")
def test_delete_slot():
    assert False

@pytest.mark.xfail(reason="未実装")
def test_update_slot():
    assert False

@pytest.mark.xfail(reason="未実装")
def test_get_slot():
    assert False

@pytest.mark.xfail(reason="未実装")
def test_serialize():
    assert False

@pytest.mark.xfail(reason="未実装")
def test_deserialize():
    assert False
