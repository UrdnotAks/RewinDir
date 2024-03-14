from shutil import move
import copy_files as cp
import pandas as pd
import os

import argparse

def parse_cmd_line_arguments():
    '''
    parses commandline arguments
    '''
    parser = argparse.ArgumentParser()
    
    parser.add_argument('-s', '--src', 
                        action='store', 
                        required=True, 
                        help='Source csv file that has the file path of images.')

    args = parser.parse_args()
    return args

def restore_files(df):
    '''
    restore files to its previous location if files paths were saved while
    transfering files
    '''
    for row in df.itertuples():
        if not os.path.isdir('/'.join(row.filename.split('/')[:-1])):
            cp.create_directory('/'.join(row.filename.split('/')[:-1]))
        cp.perform_transfer(row.new_path, row.filename, move_files=True)


def read_df_from_file(src):
    '''
    reads old file path dataframe from file and validates it.
    '''
    try:
        df = pd.read_csv(src)

        if 'filename' in df.columns and 'new_path' in df.columns and len(df) > 0:
            return df
        else:
            return None
    except Exception:
        return None


if __name__ == '__main__':
    args = parse_cmd_line_arguments()
    df = read_df_from_file(args.src)
    if df is not None:
        restore_files(df)
        cp.remove_empty_folders('/'.join(args.src.split('/')[:-1]))
    else:
        print('Restoration Failed. File specified is not valid.')
