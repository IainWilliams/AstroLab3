import ugradio
import matplotlib.pyplot as plt
import numpy as np
import snap_spec

snap = snap_spec.snap.UGRadioSnap()

snap.initialize(mode='corr')

'''
data = snap.read_data()

buf = []

for i in range(100):
    data = snap.read_data()
    buf.append(data)

buf = []

for i in range(10):
    try:
        data = snap.read_data(prev_cnt=data['acc_cnt'])
    except(AssertionError):
        print('Error')
    buf.append(data)
'''

buf = []

data = {'acc_cnt': None}

for i in range(10):
    try:
        data = snap.read_data(prev_cnt=data['acc_cnt'])
    except(AssertionError):
        print('Error')
    buf.append(data)

np.savez('noise_data.npz', **data)

#npz = np.load('noise_data.npz')

npz = **data #maybe?

d = npz['corr01']
freqs = np.linspace(0, 250, 1024, endpoint=False)

plt.plot(freqs, d.real)
plt.plot(freqs, d.imag)

plt.show()

#d.shape -> (1024,)