import time


start = time.time()

total_bytes = 1024
bin_file = open("test.bin", "wb") # Create file and open in byte write mode
print(f'Writing to {bin_file}')

# Write bytes 0x00 to 0xFF for 1KB...
for i in range(0, total_bytes):
    bin_file.write(bytes([i % 256])) # Write in byte notation (needed for 'wb')
    bin_file.flush() # Internal buffer is cleared
        
bin_file.close()

end = time.time()
elapsed_time = end - start

print(f'Done writing! Elapsed time took {elapsed_time} seconds...')