
import os
import wfdb

# Specify the directory path where the files are located
directory = r'C:\Users\lanor\Documents\Group_project_gitrep\GroupProject\non-eeg-dataset-for-assessment-of-neurological-status-1.0.0'

# Loop through all the files with names matching the pattern "Subject*_SpO2HR.atr/dat/hea"
for i in range(1, 21):
    file_pattern = f'Subject{i}_SpO2HR'
    file_list = [f for f in os.listdir(directory) if file_pattern in f]
    print(file_list)
    if len(file_list) == 2:
        # Get the file paths for the atr, dat, and hea files
        #atr_file_path = os.path.join(directory, [f for f in file_list if f.endswith('.atr')][0])
        dat_file_path = os.path.join(directory, [f for f in file_list if f.endswith('.dat')][0])
        hea_file_path = os.path.join(directory, [f for f in file_list if f.endswith('.hea')][0])

        # Read in the heart rate signal data from the dat file using the corresponding hea file
        record = wfdb.rdrecord(dat_file_path[:-4], sampfrom=0, sampto=None, channels=[0], physical=False, \
                               with_annotations=False, pn_dir=None, mode=None, dfmt=None, return_res=64, \
                               smooth_frames=False, ignore_skew=False, return_multi_ch=False)

        # Print the heart rate signal data
        print(f'Heart rate signal data for Subject {i}: {record.d_signal}')
    else:
        print(f'Incomplete file set for Subject {i}.')



