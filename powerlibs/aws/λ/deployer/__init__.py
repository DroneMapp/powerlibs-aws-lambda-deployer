import os
import shutil

from powerlibs.aws.λ.deployer import aws
from powerlibs.aws.λ.deployer import helpers
from powerlibs.aws.λ.deployer import settings
from powerlibs.aws.λ.deployer.log import logger


def main(lambda_settings):
    logger.info('Making package for %s...', lambda_settings['FunctionName'])
    tmp_dir_path = os.path.join(settings.BASE_TMP_DIR, lambda_settings['FunctionName'])
    with helpers.TempDir(tmp_dir_path) as tmp_dir:
        logger.info('Copying module file...')
        shutil.copyfile(settings.MODULE_FILE, os.path.join(tmp_dir, os.path.basename(settings.MODULE_FILE)))
        if settings.REQUIREMENTS_FILE:
            logger.info('Installing dependencies..')
            helpers.install_requirements(tmp_dir)
        logger.info('Creating .zip...')
        zip_file = helpers.zip_package(tmp_dir)
        logger.info('Pushing lambda...')
    aws.push_lambda(zip_file, lambda_settings)
    logger.info('Done.')
