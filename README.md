<h1 align="center">
  <br>
  <!-- <a href="https://github.com/UrdnotAks/RewinDir"><img src="" alt="RewinDir" width="200"></a> -->
  <br>
  RewinDir
  <br>
</h1>

<h4 align="center">Organize your photos and videos into 'year/month/day/' folder structure.</h4> 

<p align="center">
  
</p>

## How to Use

Make sure you have [git](https://git-scm.com/) and [python](https://www.python.org/) installed. Then you can run the following commands to get the scripts on your computer.

```bash
git clone https://github.com/UrdnotAks/RewinDir.git
cd RewinDir
pip install -r requirements.txt
python rewindir.py
```

If you are a python developer, consider creating a virtual environment before installing the dependent packages.

## Options
```
usage: rewindir.py [-h] [-r] -s SRC [-d DST] [--no-recursive] [-i] [-m] [-u] [-n NUM_FILES] [-w]
                   [-e [EXTRA_FILE_TYPES ...]]

options:
-h, --help            
    show this help message and exit
-r, --restore         
    If set, src argument is considered Source csv file that has the file path of images.
-s SRC, --src SRC     
    Source directory to look for images. If -r option is used, Source csv file that has the file path of images
-d DST, --dst DST     
    Destination directory to store images. Default directory is same as source directory.
--no-recursive        
    If set, the program looks for images only in the source directory and ignore all subdirectories.
-i, --interactive     
    If set, prompts the user for actions during runtime.
-m, --move_files      
    If set, moves the files instead of copying.
-u, --handle_unknown  
    If set, unknown file types are processed. This might result in processing non-image files. To specify other file types, use --extra_file_types argument.
-n NUM_FILES, --num_files NUM_FILES
    Maximum number of files to process.
-w, --treat_pil_warnings_as_error
    Treat PIL Decompression Bomb Warnings as Errors. Use when you do not know about the files present in source directory.
-e [EXTRA_FILE_TYPES ...], --extra_file_types [EXTRA_FILE_TYPES ...]
    Specify extra filetypes that needs to be processed. Use .ext to specify file extenstions and MAKE SURE they are valid file extensions. Separate multiple file extensions with spaces.
```

## License

GPL-v3

