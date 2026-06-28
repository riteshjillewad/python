import ctypes

def ref_count(address: int) -> int:
    return ctypes.c_long.from_address(address).value

my_name = "Ritesh"
address = id(my_name)

print(ref_count(address))