import numpy as np
from vedo import load, show , Volume

def visualize_volume(path_to_file, bg=(1, 1, 1), mesh_color=(1, 0, 0)):
    # Check the file extension to determine the type of file
    if path_to_file.lower().endswith(('.nrrd', '.nii')):
        # Load a volume file (NIfTI or NRRD)
        vol = load(path_to_file)
        print(f'{vol.shape}')
    elif path_to_file.lower().endswith('.npy'):
        # Load a NumPy array
        array = np.load(path_to_file)
        # Convert the array to a Volume object without specifying color ('c')
        vol = Volume(array)
    else:
        raise ValueError(f"Unsupported file format for file: {path_to_file}")

    # Show the volume
    show(vol, bg=bg)

# Example usage:
def main():
    # Input the path of the volume file
    path_to_file = input("Enter the path of the volume file: ")
    visualize_volume(path_to_file)

if __name__ == "__main__":
    main()
