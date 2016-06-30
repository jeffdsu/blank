




class slice ():



    def __init__(self, size, type, payload):
        pass

def sum_bytes(list_of_bytes):
    a = 0
    shifter = len(list_of_bytes) - 1
    for b in list_of_bytes:
        a |= ord(b) << shifter
        shifter-=1

    return a


def cat_bytes(list_of_bytes):
    a = ""
    for b in list_of_bytes:
        a+=b
    return a

def parse_bytes(list_of_bytes):

    begin_i = 0
    while (begin_i<len(list_of_bytes)):
        #new_slice = slice()
        size = sum_bytes(list_of_bytes[begin_i:begin_i+4])
        print(size)
        type = cat_bytes(list_of_bytes[begin_i+4:begin_i+8])
        print(type)
        #payload = sum(list_of_bytes[begin_i+8, begin_i+8+size)
        begin_i += 9 + size



def bytes_from_file(filename):
    list_of_bytes = []
    with open(filename, "r") as f:
        while True:
            chunk = f.read(1)
            if chunk:
                list_of_bytes.append(chunk)
            else:
                break

    return list_of_bytes




list_of_bytes = bytes_from_file('/Users/jeffdsu/Downloads/archive1.trpl')

print(list_of_bytes)


a = parse_bytes(list_of_bytes)