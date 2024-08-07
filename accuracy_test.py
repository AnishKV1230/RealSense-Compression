import numpy as np

file_path1 = r'./Frame_000184.npy'

data1 = np.load(file_path1)

clean1 = data1[~np.isnan(data1)]

file_path2 = r'./Frame_000506.npy'

data2 = np.load(file_path2)

clean2 = data2[~np.isnan(data2)]

file_path3 = r'./Frame_000760.npy'

data3 = np.load(file_path3)

clean3 = data3[~np.isnan(data3)]

# Print the loaded data to verify
print(clean1.max())
print(clean2.max())
print(clean3.max())


