from pathlib import Path
import os
import shutil

import config as cf


def create_directory(dst_dir):
    '''
    Creates nested directory as Year/Month/Day 
    '''
    Path(dst_dir).mkdir(parents=True, exist_ok=True)


def perform_transfer(src_dir, dst_dir):
    '''
    copies / moves a file from source directory to destination directory
    '''
    if cf.MOVE_FILES:
        shutil.move(src_dir, dst_dir)
    else:
        shutil.copy2(src_dir, dst_dir)


def transfer_files(df):
    '''
    Transfers files from source dir to destination dir
    Internally calls perform_transfer for each file
    '''
    for row in df.itertuples():
        if not os.path.isdir('/'.join(row.new_path.split('/')[:-1])):
            create_directory('/'.join(row.new_path.split('/')[:-1]))
        perform_transfer(row.filename, row.new_path)


def interactive_file_transfer(df):
    '''
    interactively transfers files. gets a confirmation from user about the
    destination paths of files before proceeding with the transfer.
    '''
    print(df[['filename', 'new_path']].to_markdown())
    inp = input('Do you want to proceed with transfering files to the new path?(Y or N) ')
    if inp != 'y' and inp != 'Y':
        return
    else:
        transfer_files(df)

def save_df(df):
    '''
    saves the new file paths for helping with the reversal of operations
    '''
    inp = input('Do you want to save the file paths to help with reverting the file operations?(Y or N) ')
    if inp != 'y' and inp != 'Y':
        return
    else:
        df.to_csv(cf.SRC_DIR + 'ymd_file_paths.csv', index=False)
    
    
