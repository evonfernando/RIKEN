import os
from importing import mat
from avalanchetoolbox import preprocessing as preproc

#path = '/work/imaging8/jja34/ECoG_Study/ECoG_Data/data'
path = '/data/alstottj/RIKEN/Original/'
output_path = '/data/alstottj/RIKEN/Data/'

dirList=os.listdir(path)

#bands = ('delta', 'theta', 'alpha', 'beta', 'raw', 'gamma', 'high-gamma', 'broad')
bands = ('raw',)
window='hamming'
#taps=25
taps = 512
#downsample=100.0
downsample=False
sampling_rate = 1000.0

tasks = {'FTT': 'food_tracking', 'EMT': 'emotional_movie', 'VGT': 'visual_grating', \
        'SCT': 'social_competition', 'ST': 'sleep_task'}

A_counter = 0
K1_counter = 0
K2_counter = 0
for dirname in dirList:
    print dirname
    filename = path+dirname+'/'
    components = dirname.split('_')
    name = components[2]
    output_file = output_path+'Monkey_'+name

    date = components[0][0:7]
    if components[1] not in tasks:
        continue
    task = tasks[components[1]]
    if name=='A' and task=='food_tracking':
        task = task+str(A_counter)
        A_counter = A_counter+1
    if name=='K1' and task=='food_tracking':
        task = task+str(K1_counter)
        K1_counter = K1_counter+1
    if name=='K2' and task=='visual_grating':
        task = task+str(K2_counter)
        K2_counter = K2_counter+1
    if name=='K2' and task=='sleep_task':
        data = mat(filename)

        preproc.write_to_HDF5(data,output_file, task, sampling_rate=sampling_rate, bands=bands,\
                window=window, taps=taps,\
                downsample=downsample,
                group_name='RIKEN', species='monkey', location='RIKEN',\
                        number_in_group=name, name=name, date=date)
        preproc.write_to_HDF5(data[:,:600000],output_file, 'rest', sampling_rate=sampling_rate, bands=bands,\
                window=window, taps=taps,\
                downsample=downsample,
                group_name='RIKEN', species='monkey', location='RIKEN',\
                        number_in_group=name, name=name, date=date)
        preproc.write_to_HDF5(data[:,-600000:],output_file, 'anesthetized', sampling_rate=sampling_rate, bands=bands,\
                window=window, taps=taps,\
                downsample=downsample,
                group_name='RIKEN', species='monkey', location='RIKEN',\
                        number_in_group=name, name=name, date=date)
        preproc.write_to_HDF5(data[:,600001:-600001],output_file, 'sleep_wake_transition', sampling_rate=sampling_rate, bands=bands,\
                window=window, taps=taps,\
                downsample=downsample,
                group_name='RIKEN', species='monkey', location='RIKEN',\
                        number_in_group=name, name=name, date=date)

    data = mat(filename)

    preproc.write_to_HDF5(data,output_file, task, sampling_rate=sampling_rate, bands=bands,\
            window=window, taps=taps,\
            downsample=downsample,
            group_name='RIKEN', species='monkey', location='RIKEN',\
                    number_in_group=name, name=name, date=date)
