import os
import shutil

# set the path to the directory containing the images
path = "Test"

# set the path to the directory where you want to save the new folders
output_path = "Test data split"

# set the percentages of files to be allocated to each part
percentages = [5, 10, 15, 17, 7, 13, 11, 9, 4, 12]

# get a list of all the files in the directory
files = os.listdir(path)
total_files = len(files)

# determine the number of files to put in each part based on the percentages
num_parts = len(percentages)
part_sizes = [int(total_files * p / 100) for p in percentages]
remaining_files = total_files - sum(part_sizes)
for i in range(remaining_files):
    part_sizes[i] += 1

# divide the files into parts
parts = []
start = 0
for size in part_sizes:
    part = files[start:start+size]
    parts.append(part)
    start += size

# create the new folders and copy the files
for i, part in enumerate(parts):
    # create a new folder for this part
    folder_name = f"Test_{i+1}" #Modify this according to the requirements
    folder_path = os.path.join(output_path, folder_name)
    os.makedirs(folder_path)

    # copy the files into the new folder
    for file in part:
        src = os.path.join(path, file)
        dst = os.path.join(folder_path, file)
        shutil.copyfile(src, dst)

    # print the size of this part
    print(f"Part {i+1}: {len(part)} files")
