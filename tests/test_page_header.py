import pytest
from rdbms.page_header import PageHeader
from rdbms.types import PageType

def test_page_header_init():
    ph = PageHeader()
    assert ph.page_id == 0
    assert ph.free_space_offset == -1
    assert ph.record_count == 0
    assert ph.page_type == PageType.DATA_PAGE
    assert ph.next_free_page == 0

    ph = PageHeader(1, 1, 1, PageType.INDEX_PAGE, 1)
    assert ph.page_id == 1
    assert ph.free_space_offset == 1
    assert ph.record_count == 1
    assert ph.page_type == PageType.INDEX_PAGE
    assert ph.next_free_page == 1

def test_slot_roundtrip():
    # シリアライズ→デシリアライズの一貫性テスト
    ph = PageHeader()
    phb = PageHeader.deserialize(ph.serialize())
    assert ph.page_id == phb.page_id
    assert ph.free_space_offset == phb.free_space_offset
    assert ph.record_count == phb.record_count
    assert ph.page_type == phb.page_type
    assert ph.next_free_page == phb.next_free_page

def test_update_free_space():
    ph = PageHeader()
    ph.update_free_space(10)
    assert ph.free_space_offset == 10
    ph.update_free_space(8193)
    assert ph.free_space_offset != 8193

def test_increment_record_count():
    ph = PageHeader()
    ph.increment_record_count()
    assert ph.record_count == 1

def test_decrement_record_count():
    ph = PageHeader()
    ph.decrement_record_count()
    assert ph.record_count == -1
