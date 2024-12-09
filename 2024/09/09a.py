import fileinput

diskspec = [int(c) for c in next(fileinput.input()).strip()]

if len(diskspec) < 50:
    print(f"{diskspec=}")

cksum = 0
chunk = 0
block = 0
while chunk < len(diskspec):
    if chunk % 2:
        empty_size = diskspec[chunk]
        while empty_size:
            if not diskspec[-1]:
                del diskspec[-2:]

            file_size = diskspec[-1]
            file_id = len(diskspec) // 2
            do_size = min(empty_size, file_size)
            cksum += sum(file_id * b for b in range(block, block + do_size))
            block += do_size
            diskspec[-1] -= do_size
            empty_size -= do_size
    else:
        file_size = diskspec[chunk]
        file_id = chunk // 2
        cksum += sum(file_id * b for b in range(block, block + file_size))
        block += file_size

    chunk += 1


print(f"{cksum=}")
# cksum=6344673854800 0.093s
