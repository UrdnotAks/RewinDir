import copy_files as cp
import pandas as pd
import os

import config as cf

def _restore_files(df):
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


def restore():
    '''
    Point of entry for restoring files operation
    '''
    df = read_df_from_file(cf.SRC_DIR)
    if df is not None:
        _restore_files(df)
        cp.remove_empty_folders('/'.join(cf.SRC_DIR.split('/')[:-1]))
    else:
        print('Restoration Failed. File specified is not valid.')
