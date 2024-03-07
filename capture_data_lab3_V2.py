import ugradio
import matplotlib.pyplot as plt
import numpy as np
import snap_spec
import coord

ifm = ugradio.interf.Interferometer()

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

#while True:
for i in range(1):
    jd_corrected = astropy.time.Time(jd,format='jd')
    sun_ra, sun_dec = coord.sunpos(jd=jd_corrected)
    alt, az = coord.get_altaz(ra=sun_ra, dec=sun_dec, jd=jd_corrected)
    
    if alt <= 0:
        break
    
    ifm.point(alt, az)
    
    try:
        data = snap.read_data(prev_cnt=data['acc_cnt'])
        buf.append(data)
    except(AssertionError):
        print(f'Error: {data["acc_cnt"] + 1}')

    

np.savez('noise_data.npz', data=[data.keys for data in buf])

'''
npz = np.load('noise_data.npz')['data']

d = npz['corr0
freqs = np.linspace(0, 250, 1024, endpoint=False)

plt.plot(freqs, d.real)
plt.plot(freqs, d.imag)

plt.show()
'''
#d.shape -> (1024,)
