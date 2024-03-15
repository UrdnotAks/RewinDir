from argument_parser import parse_cmd_line_arguments
import config as cf
import read_files as rf
import copy_files as cp

def _organize_files():
    '''
    This function drives the operations from listing the files in source directory to
    transfering them to year/month/day directory structure.
    '''
    df = rf.generate_file_path_df(cf.SRC_DIR)
    df = rf.add_new_path_to_df(df, cf.DST_DIR)

    if cf.INTERACTIVE:
        cp.interactive_file_transfer(df)
    else:
        cp.transfer_files(df)

    if cf.MOVE_FILES:
        cp.remove_empty_folders(cf.SRC_DIR)

    cp.save_df(df)

def organize():
    '''
    Point of entry for organizing files operation.
    '''
    if cf.TREAT_DECOMPRESSION_BOMB_WARNING_AS_ERROR:
        rf.toggle_pil_decompression_bomb_warning('error')
    else:
        rf.toggle_pil_decompression_bomb_warning('ignore')
    
    _organize_files()
