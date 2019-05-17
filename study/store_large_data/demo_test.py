import unittest, h5py
import numpy as np

class people():
    name = 'yang'
    age = 19,
    gender = 'man'


class MyTestCase(unittest.TestCase):
    def test_HDF5(self):
        arr = np.random.randn(10)

        p1 = people()
        p2 = people()
        p3 = people()
        p4 = people()
        p5 = people()

        all_people = [p1,p2,p3,p4,p5]
        with h5py.File('random.hdf5', 'w') as f:
            dset = f.create_dataset("default", data=all_people)
        with h5py.File('random.hdf5', 'r') as f:
            data = f['default']
            # print(min(data))
            # print(max(data))
            # print(data[:10])
            for key in f.keys():
                print(key)

if __name__ == '__main__':
    unittest.main()
