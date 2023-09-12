import scipy.io
import scipy.signal
import matplotlib.pyplot as plt
import numpy as np

mat_ME = scipy.io.loadmat('ME.mat')
mat_MI = scipy.io.loadmat("MI.mat")


data_ME = np.array(mat_ME['data'][4])
epoch_start_ME = mat_ME['Epoch_start']
fs_ME = mat_ME['fs']

a,b = scipy.signal.iirfilter(4,[2*np.pi*0.05,2*np.pi*1],ftype="butter",btype='bandpass',fs = 500)
filtered_data_ME= scipy.signal.filtfilt(a,b,data_ME)

data_MI = np.array(mat_MI['data'][4])
epoch_start_MI = mat_MI['Epoch_start']
fs_MI = mat_MI['fs']

a,b = scipy.signal.iirfilter(4,[2*np.pi*0.05,2*np.pi*1],ftype="butter",btype='bandpass',fs = 500)
filtered_data_MI= scipy.signal.filtfilt(a,b,data_MI)




epochs_ME = []
for num in epoch_start_ME[0]:
    epochs_ME.append(filtered_data_ME[num:num+3000])
#print(epochs)
avg_vals_ME = np.average(epochs_ME,0)



epochs_MI = []
for num in epoch_start_MI[0]:
    epochs_MI.append(filtered_data_MI[num:num+3000])
#print(epochs)
avg_vals_MI = np.average(epochs_MI,0)

plt.plot(avg_vals_ME)
plt.plot(avg_vals_MI)
plt.show()