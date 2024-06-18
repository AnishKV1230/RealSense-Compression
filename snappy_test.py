import numpy as np
import snappy as sp

def compress_numpy_array(arr):
    arr_bytes = arr.tobytes()
    compressed_data = sp.compress(arr_bytes)
    return compressed_data

def decompress_numpy_array(compressed_data, dtype, shape):
    decompressed_data = sp.decompress(compressed_data)
    arr = np.frombuffer(decompressed_data, dtype=dtype).reshape(shape)
    return arr

if __name__ == "__main__":
    large_array = np.random.randint(0, 1000, size=(10000, 10000), dtype=np.int32)
    
    # Compress the numpy array
    compressed_array = compress_numpy_array(large_array)
    print(f"Compressed size: {len(compressed_array)} bytes")

    # Decompress the numpy array
    decompressed_array = decompress_numpy_array(compressed_array, dtype=large_array.dtype, shape=large_array.shape)
    
    # Verify that the decompressed array is the same as the original
    assert np.array_equal(decompressed_array, large_array)
    print("Decompression successful and data is intact.")
