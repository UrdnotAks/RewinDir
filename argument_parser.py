import argparse

def parse_cmd_line_arguments():
    '''
    parses the cmd line arguments
    '''
    parser = argparse.ArgumentParser()
    
    parser.add_argument('-s', '--src', 
                        action='store', 
                        required=True, 
                        help='Source directory to look for images.')

    parser.add_argument('-d', '--dst', 
                        action='store', 
                        help='Destination directory to store images.\
                              Default directory: \'ymd_photos/\' ')
    
    parser.add_argument('-i', '--interactive',
                        action='store_true',
                        help='If set, prompts the user for actions during runtime.')

    parser.add_argument('-m', '--move_files',
                        action='store_true',
                        help='If set, moves the files instead of copying.')

    parser.add_argument('-u', '--handle_unknown',
                        action='store_true',
                        help='If set, unknown file types are processed. This might result \
                              in processing non-image files. To specify custom files, \
                              use --extra_file_types argument.')
    
    parser.add_argument('-e', '--extra_file_types', 
                        action='store',
                        nargs='*',
                        help='Specify extra filetypes that needs to be processed. \
                              Use .ext to specify file extenstions and MAKE SURE \
                              they are valid file extensions. Separate multiple \
                              file extensions with spaces.')

    args = parser.parse_args()
    return args
