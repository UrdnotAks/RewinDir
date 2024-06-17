from organize_files import organize
from restore_files import restore
from argument_parser import parse_cmd_line_arguments
import config as cf


def set_config(args):
    '''
    sets the config variables
    '''
    if args.restore:
        cf.SRC_DIR = args.src
    else:
        cf.SRC_DIR = args.src if args.src.endswith('/') else args.src + '/'

    cf.DST_DIR = args.dst if args.dst is not None else cf.SRC_DIR
    cf.DST_DIR = cf.DST_DIR if cf.DST_DIR.endswith('/') else cf.DST_DIR + '/'
    
    cf.INTERACTIVE = args.interactive
    cf.MOVE_FILES = args.move_files
    cf.HANDLE_UNKNOWN_FILES = args.handle_unknown
    if args.extra_file_types:
        cf.ADDITIONAL_FILE_TYPES_TO_PROCESS += tuple([i for i in args.extra_file_types])
    cf.TREAT_DECOMPRESSION_BOMB_WARNING_AS_ERROR = args.treat_pil_warnings_as_error
    cf.NUM_FILES = args.num_files
    cf.RECURSIVE = args.recursive


if __name__ == '__main__':
    args = parse_cmd_line_arguments()
    set_config(args)
    if args.restore:
        restore()
    else:
        organize()
