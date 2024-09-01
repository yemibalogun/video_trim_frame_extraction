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
    
    # Look for an mp4 or mov file in the current subfolder
    video_files = [f for f in files if f.endswith(('.mp4', '.mov'))]
    
    if not video_files:
        print(f"No video file found in {subdir}")
        continue
    
    # Assume there's only one video file per subfolder
    original_video_path = os.path.join(subdir, video_files[0])
    
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
    
    # Convert the video to H.264 - MPEG-4 AVC codec
    converted_video_path = os.path.join(subdir, 'converted_video.mp4')
    try:
        subprocess.run([
            'C:\\ffmpeg-2024-08-28-git-b730defd52-essentials_build\\bin\\ffmpeg.exe', '-i', original_video_path,
            '-vcodec', 'libx264', '-acodec', 'aac', converted_video_path
        ], check=True)
        print(f"Video in {subdir} converted to H.264 - MPEG-4 AVC codec successfully.")
        
        # Replace the original video with the converted video
        os.remove(original_video_path)
        os.rename(converted_video_path, original_video_path)
        print(f"Replaced original video with H.264 - MPEG-4 AVC codec video in {subdir}.")
    except subprocess.CalledProcessError:
        print(f"Failed to convert video in {subdir} to H.264 - MPEG-4 AVC codec.")
        continue
    
    # Extract first and last frames of the converted video
    cap = cv2.VideoCapture(original_video_path)
    
    if not cap.isOpened():
        print(f"Error opening converted video file {original_video_path}")
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
    
    # Look for a png file in the current subfolder
    png_files = [f for f in files if f.endswith('.png')]
    
    if png_files:
        png_path = os.path.join(subdir, png_files[0])
        
        # Load the PNG image
        png_image = cv2.imread(png_path)
        
        # Resize the PNG image to 1920 x 1080
        resized_png = cv2.resize(png_image, (1920, 1080))
        
        # Save the resized image, overwriting the original file
        cv2.imwrite(png_path, resized_png)
        
        print(f"Resized PNG image in {subdir} to 1920x1080.")

print("Processing complete.")
