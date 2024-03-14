

from argument_parser import parse_cmd_line_arguments
import config as cf
import read_files as rf

def set_config(args):
    '''
    sets the config variables
    '''
    cf.SRC_DIR = args.src
    cf.DST_DIR = args.dst
    cf.INTERACTIVE = args.interactive
    cf.MOVE_FILES = args.move_files
    cf.HANDLE_UNKNOWN_FILES = args.handle_unknown
    cf.ADDITIONAL_FILE_TYPES_TO_PROCESS += tuple([i for i in args.extra_file_types])
    cf.TREAT_DECOMPRESSION_BOMB_WARNING_AS_ERROR = args.treat_pil_warnings_as_error
    cf.NUM_FILES = args.num_files

def main():
    print(args)


if __name__ == '__main__':
    args = parse_cmd_line_arguments()
    set_config(args)

    if cf.SUPPRESS_DECOMPRESSION_BOMB_WARNING:
        rf.toggle_pil_decompression_bomb_warning('ignore')
    else:
        rf.toggle_pil_decompression_bomb_warning('error')
    
    main()
