import os
from pathlib import Path
from dotenv import load_dotenv


class AppConfig:
    __instance__ = None

    def __init__(self):
        """ Constructor.
       """
        if AppConfig.__instance__ is None:
            AppConfig.__instance__ = self

            env_path = Path('.') / '.env'
            load_dotenv(dotenv_path=env_path)

            self.APP_ENV = os.getenv('APP_ENV')
            self.APP_NAME = os.getenv('APP_NAME')
            self.API_URL = os.getenv('API_URL')
            self.APP_FRONTEND_URL = os.getenv('APP_FRONTEND_URL')
            self.UPLOAD_PATH = os.getenv('UPLOAD_PATH')

            self.MONGO_DB_CONNECTION_URI = os.getenv('MONGO_DB_CONNECTION_URI')
            self.DATABASE_NAME = os.getenv('DATABASE_NAME')
            self.LOGS_DATABASE_NAME = os.getenv('LOGS_DATABASE_NAME')

            self.TOKEN_SECRET = os.getenv('TOKEN_SECRET')
            self.TOKEN_ALGORITHM = os.getenv('TOKEN_ALGORITHM')
            self.TOKEN_EXPIRY_IN_MINUTES = int(os.getenv('TOKEN_EXPIRY_IN_MINUTES'))

            self.RABBITMQ_HOST = os.getenv('RABBITMQ_HOST')
            self.RABBITMQ_PORT = int(os.getenv('RABBITMQ_PORT'))
            self.RABBITMQ_CONNECTION_URI = os.getenv('RABBITMQ_CONNECTION_URI')

            self.DEFAULT_QUEUE_NAME = os.getenv('DEFAULT_QUEUE_NAME')
            self.SEND_EMAIL_QUEUE = os.getenv('SEND_EMAIL_QUEUE')

            self.AWS_KEY_ID = os.getenv('AWS_KEY_ID')
            self.AWS_KEY_SECRET = os.getenv('AWS_KEY_SECRET')
            self.FILE_UPLOAD_BUCKET = os.getenv('FILE_UPLOAD_BUCKET')

            self.SMTP_HOST = os.getenv('SMTP_HOST')
            self.SMTP_PORT = int(os.getenv('SMTP_PORT'))
            self.SMTP_ID = os.getenv('SMTP_ID')
            self.SMTP_PASSWORD = os.getenv('SMTP_PASSWORD')
            self.MAIL_TEMPLATES_DIR = os.getenv('MAIL_TEMPLATES_DIR')
            self.DEFAULT_SENDER_EMAIL = os.getenv('DEFAULT_SENDER_EMAIL')
            self.DEFAULT_SENDER_NAME = os.getenv('DEFAULT_SENDER_NAME')

            self.REDIS_CONNECTION_URI = os.getenv('REDIS_CONNECTION_URI')

            self.XL_TEMPLATES_DIR = os.getenv('XL_TEMPLATES_DIR')
            self.PDF_TEMPLATES_DIR = os.getenv('PDF_TEMPLATES_DIR')

            self.IAM_POLICY_TEMPLATE_PATH = os.getenv('IAM_POLICY_TEMPLATE_PATH')


            self.MAILGUN_BASE_URL = os.getenv('MAILGUN_BASE_URL')
            self.MAILGUN_DOMAIN_NAME = os.getenv('MAILGUN_DOMAIN_NAME')
            self.MAILGUN_ACCESS_KEY = os.getenv('MAILGUN_ACCESS_KEY')

            self.MODEL_PATH = os.getenv('MODEL_PATH')
            self.OUTPUT_PATH = os.getenv('OUTPUT_PATH')

            # errbit error tracker

            self.ERRBIT_PROJECT_KEY = os.getenv('ERRBIT_PROJECT_KEY')
            self.ERRBIT_HOST = os.getenv('ERRBIT_HOST')
        else:
            raise Exception("You cannot create another AppConfig class")

    @staticmethod
    def get_config() -> 'AppConfig':
        """ Static method to fetch the current instance.
       """
        if not AppConfig.__instance__:
            AppConfig()
        return AppConfig.__instance__
