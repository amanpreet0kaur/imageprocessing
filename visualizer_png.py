from vedo import load, show, Volume
import nibabel as nib
import os
import numpy as np
import nrrd
from vedo import load, show

def visualize_nifti(path_to_file, output_path, bg=(1,1,1), mesh_color=(1,0,0)):
    # Load NIfTI file
    # vol = Volume(input_path)

    # Show the volume
    
    if path_to_file.lower().endswith(('.nrrd', '.nii')):
        # Load a volume file (NIfTI or NRRD)
        vol = load(path_to_file)
        
        data, header = nrrd.read(path_to_file)

        # Print the size of the NRRD data
        print(f"{path_to_file} Size: {data.shape}")
        # Load the NRRD file
        #data, header = nrrd.read(path_to_file)

        # Print the size of the NRRD data
        #print(f" Size: {data.shape}")
    elif path_to_file.lower().endswith('.npy'):
        # Load a NumPy array
        array = np.load(path_to_file)
        # Convert the array to a Volume object
        vol = load(array, spacing=(1, 1, 1), c='gray')
    else:
        raise ValueError(f"Unsupported file format for file: {path_to_file}")

    # Show the volume
    vp=show(vol, bg=bg,interactive=False,offscreen=True)

    output_filename = os.path.join(output_path, os.path.basename(input_path) + '_visualization.png')
    vp.screenshot(output_filename) 
    vp.close()

#input_folder = "/media/computer/a454b81a-4532-48c4-a200-7aad03b060e2/skull Reconstruction/Pre Processing Final Outputs/filtered_nrrd"
input_folder = "/media/computer/a454b81a-4532-48c4-a200-7aad03b060e2/skull Reconstruction/Pre Processing Final Outputs/filtered_nrrd"
output_folder = "/media/computer/ff1e3558-7505-4148-bcb3-5af20a2d1dd9/skull_images"
# Iterate through NIfTI files in the input folder
# Iterate through NIfTI files in the input folder
for file_name in os.listdir(input_folder):
    if file_name.endswith(".nrrd") or file_name.endswith(".nii.gz"):
        # Construct the full path to the input NIfTI file
        input_path = os.path.join(input_folder, file_name)

        # Visualize and save the output to the output folder
        visualize_nifti(input_path, output_folder)