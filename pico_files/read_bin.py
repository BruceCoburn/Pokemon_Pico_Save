import time

start_time = time.time()

bin_file = open('test.bin', 'rb')

binArray = bytearray(bin_file.read(1024))

bin_file.close

end_time = time.time()

elapsed_time = end_time - start_time

print(f'elapsed_time: {elapsed_time}')

print(binArray)