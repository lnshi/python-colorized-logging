import logging.config

from utils.logging.config import logging_config

logging.config.dictConfig(logging_config)
logger = logging.getLogger(__name__)

logger.debug('I am just a testing log message.')
logger.info('I am just a testing log message.')
logger.warn('I am just a testing log message.')
logger.error('I am just a testing log message.')
logger.critical('I am just a testing log message.')
