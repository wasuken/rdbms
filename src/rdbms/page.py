PAGE_SIZE = 8192  # 8KB
HEADER_SIZE = 16
SLOT_SIZE = 4

class Page:
    page_id = 0
    data = []
    free_space_offset = 0
    record_count = 0
    page_type = 0

    def get_record():
        raise NotImplementedError()

    def insert_record():
        raise NotImplementedError()

    def delete_record():
        raise NotImplementedError()

    def update_record():
        raise NotImplementedError()

    def check_free_space():
        raise NotImplementedError()

    def set_deploypoint():
        raise NotImplementedError()

    def update_slot():
        raise NotImplementedError()

    def write_record():
        raise NotImplementedError()

    def update_header():
        raise NotImplementedError()
