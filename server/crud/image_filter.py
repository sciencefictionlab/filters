import time
import uuid
from pathlib import Path
from typing import Union
import boto3
import magic

from server.utils.functions import create_output_path

mime = magic.Magic(mime=True)
from server.singletons.config import AppConfig
import shutil, os
from pixellib.tune_bg import alter_bg
config = AppConfig.get_config()


s3 = boto3.client(
    service_name='s3',
    region_name='eu-central-1',
    aws_access_key_id=config.AWS_KEY_ID,
    aws_secret_access_key=config.AWS_KEY_SECRET
)


def save_upload_file(file, path):
    with path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)


async def make_background_gray(image):
    temp_path = config.UPLOAD_PATH
    filename = uuid.uuid4().hex
    extension = image.filename.split('.')[-1]

    filename = filename + '.' + extension if extension else print('No file extension')

    save_upload_file(image, Path(temp_path + filename))

    shutil.move(Path(temp_path + filename), Path(config.UPLOAD_PATH + os.sep + filename))

    current_file = temp_path + filename


    change_bg = alter_bg()
    change_bg.load_pascalvoc_model(config.MODEL_PATH+"deeplabv3_xception_tf_dim_ordering_tf_kernels.h5")
    outfile = create_output_path() + os.sep + str(time.time()) + '.jpg'

    file = os.path.basename(outfile)

    try:
        change_bg.gray_bg(current_file, output_image_name=outfile)
        s3_url = await upload_single_file(outfile, file , 'sciencefictionlab-public', True)
        return {'url': s3_url}
    except Exception as e:
        print(e)


async def make_background_white_color(image):
    temp_path = config.UPLOAD_PATH
    filename = uuid.uuid4().hex
    extension = image.filename.split('.')[-1]

    filename = filename + '.' + extension if extension else print('No file extension')

    save_upload_file(image, Path(temp_path + filename))

    shutil.move(Path(temp_path + filename), Path(config.UPLOAD_PATH + os.sep + filename))

    current_file = temp_path + filename

    change_bg = alter_bg()
    change_bg.load_pascalvoc_model(config.MODEL_PATH + "deeplabv3_xception_tf_dim_ordering_tf_kernels.h5")
    outfile = create_output_path() + os.sep + str(time.time()) + '.jpg'

    file = os.path.basename(outfile)

    try:

        change_bg.color_bg(current_file, colors=(255, 255, 255), output_image_name=outfile)
        s3_url = await upload_single_file(outfile, file, 'sciencefictionlab-public', True)
        return {'url': s3_url}
    except Exception as e:
        print(e)


async def upload_single_file(path_to_file, file, bucket_name, make_public: bool = False) -> Union[str, bool]:

    file_location_in_s3 = 'converted_images'+'/'+ file

    try:
        with open(path_to_file, 'rb') as data:
            s3.upload_fileobj(data, Bucket=bucket_name, Key=file_location_in_s3,
                              ExtraArgs={'ACL': 'public-read'} if make_public else {})
        print("Upload Successful")
        os.remove(path_to_file)
        return 'https://' + bucket_name + '.s3.eu-central-1.amazonaws.com/' + file_location_in_s3
    except FileNotFoundError:
        print("The file was not found")
        return False







