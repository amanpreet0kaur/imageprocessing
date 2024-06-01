import numpy as np
from vedo import load, show, Volume

def visualize_volume(path_to_file, bg=(1, 1, 1), mesh_color=(1, 0, 0)):
    if path_to_file.lower().endswith(('.nrrd', '.nii')):
        vol = load(path_to_file)
    elif path_to_file.lower().endswith('.npy'):
        array = np.load(path_to_file)
        if array.shape[-1] == 1:
            array = array.squeeze()
        array = np.nan_to_num(array)
        print("Array shape:", array.shape)
        vol = Volume(array)
    else:
        raise ValueError(f"Unsupported file format for file: {path_to_file}")

    show(vol, bg=bg)

def main():
    path_to_file = input("Enter the path of the volume file: ")
    visualize_volume(path_to_file)

if __name__ == "__main__":
    main()
