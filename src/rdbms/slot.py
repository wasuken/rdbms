import struct
class Slot:

    def __init__(self, offset: int = 0, length: int = 0, is_active: bool = True):
        self.offset = offset
        self.length = length
        self.is_active = is_active

    def serialize(self):
        return struct.pack('>hh?', self.offset, self.length, self.is_active)

    @classmethod
    def deserialize(self, data: bytes) -> 'Slot':
        offset, length, is_active = struct.unpack('>hh?', data)
        return self(offset, length, is_active)
