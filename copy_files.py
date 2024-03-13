from pathlib import Path
import os
import shutil

import config as cf


def create_directory(dest_dir):
    '''
    Creates nested directory as Year/Month/Day 
    '''
    Path(dest_dir).mkdir(parents=True, exist_ok=True)


def perform_transfer(src_dir, dest_dir):
    '''
    copies / moves a file from source directory to destination directory
    '''
    if cf.MOVE_FILES:
        shutil.move(src_dir, dest_dir)
    else:
        shutil.copy2(src_dir, dest_dir)


def transfer_files(dest_dir, df):
    '''
    Transfers files from source dir to destination dir
    Internally calls perform_transfer for each file
    '''
    for row in df.itertuples():
        if not os.path.isdir(row.new_path):
            create_directory(row.new_path)
        perform_transfer(row.filename, row.new_path)


def interactive_file_transfer(df):
    '''
    interactively transfers files. gets a confirmation from user about the
    destination paths of files before proceeding with the transfer.
    '''
    pass
