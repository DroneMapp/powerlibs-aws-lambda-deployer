import logging

from powerlibs.aws.λ.deployer import settings

kwargs = {
    'format': '%(asctime)-15s %(message)s',
    'level':  getattr(logging, settings.LOG_LEVEL, logging.WARNING)
}
if settings.LOG_FILE:
    kwargs['filename'] = settings.LOG_FILE

logging.basicConfig(**kwargs)
logger = logging.getLogger('saito')
