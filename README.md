This project organizes local photos into `year/month/day/` folder structure. 

## Usage
```
usage: rewindir.py [-h] [-r] -s SRC [-d DST] [--no-recursive] [-i] [-m] [-u] [-n NUM_FILES] [-w]
                   [-e [EXTRA_FILE_TYPES ...]]

options:
  -h, --help            show this help message and exit
  -r, --restore         If set, src argument is considered Source csv file that has the file path of images.
  -s SRC, --src SRC     Source directory to look for images. If -r option is used, Source csv file that has the file
                        path of images
  -d DST, --dst DST     Destination directory to store images. Default directory is same as source directory.
  --no-recursive        If set, the program looks for images only in the source directory and ignores all
                        subdirectories.
  -i, --interactive     If set, prompts the user for actions during runtime.
  -m, --move_files      If set, moves the files instead of copying.
  -u, --handle_unknown  If set, unknown file types are processed. This might result in processing non-image files. To
                        specify custom files, use --extra_file_types argument.
  -n NUM_FILES, --num_files NUM_FILES
                        Maximum number of files to process.
  -w, --treat_pil_warnings_as_error
                        Treat PIL Decompression Bomb Warnings as Errors. Use when you don't know about the files present
                        in source directory.
  -e [EXTRA_FILE_TYPES ...], --extra_file_types [EXTRA_FILE_TYPES ...]
                        Specify extra filetypes that needs to be processed. Use .ext to specify file extenstions and
                        MAKE SURE they are valid file extensions. Separate multiple file extensions with spaces.
```