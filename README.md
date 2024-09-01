# VIDEO TRIMMING AND FRAME EXTRACTION SCRIPT
## OVERVIEW
This Python script processes video files within a specified directory structure. It trims each video to a specified duration, replaces the original video with the trimmed version, and extracts the first and last frames of the trimmed video.
## Dependencies
The script requires the following Python libraries:
1.	`os`: For file and directory operations.
2.	`subprocess`: For executing external commands.
3.	`cv2` (OpenCV): For video processing and frame extraction.

Additionally, FFmpeg must be installed on your system for video trimming. Ensure that FFmpeg is accessible via the provided path in the script.
## Setup
1. Install Required Libraries:
   Make sure you have OpenCV installed. You can install it using pip:
   ```bash
   pip install opencv-python
   ```


2. FFmpeg Installation:
   Download FFmpeg from [FFmpeg's official website](https://ffmpeg.org/download.html) and extract it. Update the `ffmpeg_path` variable in the script to point to the `ffmpeg.exe` executable.
## Script Details
Script Path
The path to the root directory containing subfolders with videos:
```python
companies_folder = 'C:\\Path_to_main_dir\\companies'
```
## Trim Duration
The duration to trim each video to, in seconds:
```python
trim_duration = 5.96
```
## Script Functionality
1. Traversal of Subdirectories:
The script iterates over each subdirectory within the specified root directory, skipping the root itself.



2. Video Processing:
   - Finding MP4 Files:
     The script searches for `.mp4` files in each subfolder. If none are found, it prints a message and moves to the next subfolder.
   - Trimming the Video:
     The script uses FFmpeg to trim the video to the specified duration. The output is saved as `trimmed_video.mp4`.
   - Replacing the Original Video:
     After trimming, the original video is removed and replaced by the trimmed video.
3. Frame Extraction:
   - First Frame:
     The script extracts the first frame from the trimmed video and saves it as `first_frame.jpg`.
   - Last Frame:
     The script extracts the last frame and saves it as `last_frame.jpg`.

4. Error Handling:
   - If trimming fails, an error message is printed.
   - If replacing the video or extracting frames encounters an issue, it logs the error.


## Example Output
The console output includes messages such as:
- `"Video in <subdir> trimmed successfully to <duration> seconds."`
- `"Replaced original video with trimmed video in <subdir>."`
- `"Error opening trimmed video file <path>"`
## Running the Script
1. Ensure that Python is installed and your environment is set up.
2. Update the `companies_folder` and `ffmpeg_path` variables as needed.
3. Execute the script in your terminal or command prompt:
   ```bash
   python main.py
   ```
## Notes*
- Ensure FFmpeg is correctly installed and the path is accurately specified.
- Verify that the OpenCV library is correctly installed and accessible.
- The script assumes there is only one `.mp4` file per subfolder. 

