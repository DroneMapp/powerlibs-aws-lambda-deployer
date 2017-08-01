from prettyconf import config

BASE_TMP_DIR = config('BASE_TMP_DIR', default='/tmp/lambda_deploys')
LOG_LEVEL = config('LOG_LEVEL', default='INFO')
LOG_FILE = config('LOG_FILE', default=None)

AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID', default=None)
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY', default=None)
AWS_REGION_NAME = config('AWS_DEFAULT_REGION', default='us-east-1')

MODULE_FILE = config('MODULE_FILE')
LAMBDA_SETTINGS_FILE = config('LAMBDA_SETTINGS_FILE')
ENV_FILE = config('ENV_FILE', default=None)
REQUIREMENTS_FILE = config('REQUIREMENTS_FILE', default=None)
