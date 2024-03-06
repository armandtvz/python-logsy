import logging

import logsy


config = {
    'loggers': {
        '': {
            'handlers': ['console', 'fluent', 'file'],
            'level': logging.INFO,
            'propagate': True,
        },
        'app': {
            'handlers': ['console', 'fluent', 'file'],
            'level': logging.WARNING,
            # Changing propagate to True here will likely duplicate log records.
            'propagate': False,
        },
    },
}
logsy.init(
    config,
    tag='apps.mytag',
    fluent_host='localhost',
    fluent_port='24225',
    environment=None,
    release='1.0.0'
)




logger = logging.getLogger(__name__)
logger.debug('debug')
logger.info('info')
logger.warning('warning')
logger.error('error')
try:
    raise ValueError('This is a ValueError')
except ValueError as exc:
    logger.exception(exc)

try:
    raise TypeError('This is a TypeError')
except TypeError as exc:
    logger.critical(exc, exc_info=True)




app_logger = logging.getLogger('app')
app_logger.info('No log record will be created for the "INFO" log level.')
app_logger.warning('But this warning will be logged.')
