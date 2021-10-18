import os
import datetime

from server.singletons import AppConfig

config = AppConfig.get_config()
def create_output_path():

    datepath = datetime.datetime.now().strftime('%Y/%m/%d_%H-%M-%S')
    outdir = os.path.join(config.OUTPUT_PATH, datepath)
    if not os.path.exists(outdir):
        os.makedirs(outdir)
    return outdir
