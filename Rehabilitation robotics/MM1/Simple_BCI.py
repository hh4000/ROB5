import scipy.io
import scipy.signal
import matplotlib.pyplot as plt
import numpy as np

mat = scipy.io.loadmat('ME.mat')

data = np.array(mat['data'][4])
epoch_start = mat['Epoch_start']
fs = mat['fs']

a,b = scipy.signal.iirfilter(4,[2*np.pi*0.05,2*np.pi*5],ftype="butter",btype='bandpass',fs = 500)
filtered_data= scipy.signal.filtfilt(a,b,data)

epochs = []
for num in epoch_start:
    epochs = 
fig,ax = plt.subplots(2)
ax[0].plot(filtered_data[6610:6610+3000])
ax[1].plot(data[6610:6610+3000])
plt.show()