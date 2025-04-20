from PIL import Image, UnidentifiedImageError
from datetime import datetime
from dateutil import parser as date_parser
import warnings
import glob
import os

import pandas as pd
from pillow_heif import register_heif_opener, register_avif_opener

import config as cf

register_heif_opener()
register_avif_opener()

def toggle_pil_decompression_bomb_warning(warning_level):
    '''
    This method sets the warning level of the PIL Decompression Bomb Warning
    '''
    warnings.simplefilter(warning_level, Image.DecompressionBombWarning)

def list_files(src_dir):
    '''
    Lists the files in the specified directory recursively
    '''

    return iter([src_dir+i for i in glob.glob('**', root_dir=src_dir, recursive=cf.RECURSIVE) 
                                    if os.path.isfile(src_dir+i)])


def get_file_attrib(attrib):
    '''
    returns which file attribute to use for organising the files
    '''
    attrib_dict = {
        'creation_date' : os.path.getctime,                                     # getctime does not return creation time 
        'modified_date' : os.path.getmtime                                      # in UNIX systems, refer docs for more
    }                                                                           # https://docs.python.org/3/library/os.path.html#os.path.getctime
    return attrib_dict[attrib]


def generate_file_path_df(src_dir, use_creation_date=False):
    '''
    Opens files to access EXIF data of images, if unable to access the basedir  
    '''

    attrib_func = get_file_attrib('creation_date') \
                if use_creation_date \
                else get_file_attrib('modified_date')

    df = pd.DataFrame(columns=['filename', 'timestamp', 'source'])

    files = list_files(src_dir)
    file = next(files, '')
    while file:
        if len(df) > cf.NUM_FILES:
            break
        try:
            img = Image.open(file)
            img_exif = img.getexif()

            if img_exif is not None and 306 in img_exif.keys():                 # 306 - EXIF TAG for DateTime
                try:
                    df.loc[len(df)] = [file, 
                                    datetime.strptime(img_exif[306], 
                                                        '%Y:%m:%d %H:%M:%S'),  
                                    'exif']
                except ValueError:
                    df.loc[len(df)] = [file,
                                       date_parser.parse(img_exif[306]), 
                                       'exif']
            else:
                df.loc[len(df)] = [file, 
                                   datetime.fromtimestamp(attrib_func(file)), 
                                   'file_attribute']
            file = next(files, '')

        except UnidentifiedImageError:
            if not file.lower().endswith(cf.ADDITIONAL_FILE_TYPES_TO_PROCESS):
                print('Encountered unknown filetype {}'.format(file))

                if cf.INTERACTIVE:
                    inp = input('Do you want to process this file? (Y or N)')
                    if inp not in ['y', 'Y']:
                        file = next(files, '')
                        continue
                else:
                    if not cf.HANDLE_UNKNOWN_FILES:
                        print('Skipping the file with unknown file format')
                        file = next(files, '')
                        continue

            df.loc[len(df)] = [file, 
                                datetime.fromtimestamp(attrib_func(file)), 
                                'file_attribute']
            file = next(files, '')

        except OSError:
            print('Failed to open file {}. Skipping it.'.format(file))
            file = next(files, '')
        
        except Image.DecompressionBombError:
            print('Encountered Decompression Error while accessing {}'.format(file))
            print('Skipping the file as it could be malicious')
            file = next(files, '')
    
    df = split_date(df)
    return df


def split_date(df):
    '''
    splits date time into year, month and day
    '''
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['year'] = df.timestamp.dt.year
    df['month'] = df.timestamp.dt.month
    df['day'] = df.timestamp.dt.day

    return df


def add_new_path_to_df(df, dst_dir):
    '''
    adds new path where the file will be copied to the dataframe
    '''
    for row in df.itertuples():
        full_path = dst_dir+'{}/{}/{}/'.format(row.year, row.month, row.day)
        df.loc[row.Index, 'new_path'] = full_path
    df['new_path'] = df['new_path'] + df['filename'].str.rsplit('/', n=1).str[-1]
    return df
