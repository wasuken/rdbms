import pytest
from rdbms.page import Page
from rdbms.slot_array import SlotArray
from rdbms.slot import Slot
from rdbms.page_header import PageHeader
from rdbms.types import PageType, PAGE_SIZE, SLOT_ARRAY_HEADER_SIZE, PAGE_HEADER_ENTRY_SIZE

def test_page_header_init():
    ph = PageHeader()
    sl = SlotArray()
    sl2 = SlotArray()

    p = Page()
    assert p.page_id == 0
    assert p.data == []
    assert p.header.serialize() == ph.serialize()
    assert p.slot_array.serialize() == sl.serialize()

    ph = PageHeader()
    sl = SlotArray()
    p = Page(10, [], ph, sl)
    assert p.page_id == 10
    assert p.data == []
    assert p.header.serialize() == ph.serialize()
    assert p.slot_array.serialize() == sl.serialize()

def test_get_free_space():
    p = Page()
    assert p.get_free_space() == (PAGE_SIZE - PAGE_HEADER_ENTRY_SIZE - SLOT_ARRAY_HEADER_SIZE)
