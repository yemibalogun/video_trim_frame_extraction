import os
import subprocess
import cv2

# Define the path to the 'companies' folder
companies_folder = 'C:\\Users\\OMEN 15 Pro\\Videos\\companies'

# Specify the trim duration in seconds (e.g., 5.96 seconds)
trim_duration = 5.96

# Iterate over each subfolder in the 'companies' folder
for subdir, _, files in os.walk(companies_folder):
    # Skip the root directory itself and only process subdirectories
    if subdir == companies_folder:
        continue
    
    # Look for an mp4 file in the current subfolder
    mp4_files = [f for f in files if f.endswith('.mp4')]
    
    if not mp4_files:
        print(f"No mp4 file found in {subdir}")
        continue
    
    # Assume there's only one mp4 file per subfolder
    original_video_path = os.path.join(subdir, mp4_files[0])
    
    # Define the output path for the trimmed video
    trimmed_video_path = os.path.join(subdir, 'trimmed_video.mp4')
    
    # Trim the video using FFmpeg
    try:
        subprocess.run([
            'C:\\ffmpeg-2024-08-28-git-b730defd52-essentials_build\\bin\\ffmpeg.exe', '-i', original_video_path, '-t', str(trim_duration),
            '-c', 'copy', trimmed_video_path
        ], check=True)
        print(f"Video in {subdir} trimmed successfully to {trim_duration} seconds.")
    except subprocess.CalledProcessError:
        print(f"Failed to trim video in {subdir}.")
        continue
    
    # Replace the original video with the trimmed video
    try:
        os.remove(original_video_path)
        os.rename(trimmed_video_path, original_video_path)
        print(f"Replaced original video with trimmed video in {subdir}.")
    except Exception as e:
        print(f"Error replacing video in {subdir}: {e}")
        continue
    
    # Extract first and last frames of the trimmed video
    cap = cv2.VideoCapture(original_video_path)
    
    if not cap.isOpened():
        print(f"Error opening trimmed video file {original_video_path}")
        continue
    
    # Read the first frame
    ret, first_frame = cap.read()
    if ret:
        cv2.imwrite(os.path.join(subdir, 'first_frame.jpg'), first_frame)
    
    # Seek to the last frame
    cap.set(cv2.CAP_PROP_POS_FRAMES, cap.get(cv2.CAP_PROP_FRAME_COUNT) - 1)
    ret, last_frame = cap.read()
    if ret:
        cv2.imwrite(os.path.join(subdir, 'last_frame.jpg'), last_frame)
    
    cap.release()

print("Processing complete.")
