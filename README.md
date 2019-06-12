
# watermarker
A small python script to generate rotated text watermarks to cover an image.

## Installation
To get this project up and running, you'll need to set up a few things:

(These instructions are for Windows, if you're using Mac, you're on your own. I've never used a Mac)

1. Download Python 3.7 or higher, and MAKE SURE TO CHOOSE 'ADD TO PATH' DURING INSTALL

2. Download the ffmpeg binary from [here](https://ffmpeg.zeranoe.com/builds/). Be sure to choose the 'stable' version (currently 4.1.3), 
   your OS, and 'Static' under Linking, then click Download Build.

3. Download ImageMagick from [here](https://imagemagick.org/script/download.php). That page isn't loading as of when I'm writing this, 
   but the mirrors at [SourceForge](https://sourceforge.net/projects/imagemagick/files/) should work fine.

4. Clone this repo to somewhere easy to get to.

5. Open a PowerShell or CMD window as Administrator and redirect it to the watermarker folder using the 'cd' command

6. Type in 'python' and ensure something along the lines of    `Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32` appears

7. Type `exit()` to exit the python console, then enter `python -m pip install --upgrade pip`
   to ensure the pip package manager is up to date.

8. Type in `pip install -r requirements.txt` to the PowerShell/CMD window and press ENTER. 
   It should start installing the necessary packages.

9. Type in `pip show moviepy`, highlight the directory next to 'Location', copy it and paste it in a Windows Explorer window to get to it.

10. Find the 'moviepy' folder in there, and inside that folder, find the 'config_defaults.py' file. 
    Open this in a text editor THAT ISN'T NOTEPAD. N++ is fine.

11. Scroll to the bottom and find FFMPEG_BINARY and IMAGEMAGICK_BINARY. Replace what's after the = with a path to your 
    ffmpeg.exe and magick.exe that you downloaded earlier. Save the file after making these changes
	For example:	
```
		FFMPEG_BINARY = r"D:\Downloads\ffmpeg-4.1-win64-static\bin\ffmpeg.exe"
		IMAGEMAGICK_BINARY = r"C:\Program Files\ImageMagick-7.0.8-Q16\magick.exe"
```

(The r in front of the quotations allows you to use single backslashes as a path separator. If you don't use this, 
	you need to make every backslash a \\ so that Python doesn't think you're trying to use special characters)

12. Now you can open a PowerShell/CMD Prompt, redirect it to the project folder containing 'watermarker.py', and type in `python watermarker.py`
    to run the script.

Enjoy :)