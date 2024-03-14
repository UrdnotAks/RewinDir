from argument_parser import parse_cmd_line_arguments
import config as cf
import read_files as rf
import copy_files as cp

def set_config(args):
    '''
    sets the config variables
    '''
    cf.SRC_DIR = args.src
    cf.DST_DIR = args.dst if args.dst is not None else args.src
    cf.INTERACTIVE = args.interactive
    cf.MOVE_FILES = args.move_files
    cf.HANDLE_UNKNOWN_FILES = args.handle_unknown
    if args.extra_file_types:
        cf.ADDITIONAL_FILE_TYPES_TO_PROCESS += tuple([i for i in args.extra_file_types])
    cf.TREAT_DECOMPRESSION_BOMB_WARNING_AS_ERROR = args.treat_pil_warnings_as_error
    cf.NUM_FILES = args.num_files

def main():
    df = rf.generate_file_path_df(cf.SRC_DIR)
    df = rf.add_new_path_to_df(df, cf.DST_DIR)
    cp.transfer_files(df)

if __name__ == '__main__':
    args = parse_cmd_line_arguments()
    set_config(args)

    if cf.TREAT_DECOMPRESSION_BOMB_WARNING_AS_ERROR:
        rf.toggle_pil_decompression_bomb_warning('error')
    else:
        rf.toggle_pil_decompression_bomb_warning('ignore')
    
    main()
