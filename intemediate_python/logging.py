import logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s-%(name)s-%(message)s',datefmt='%Y/%m/%d %H:%M:%S')
logger = logging.getLogger(__name__)
logger.debug('this is debug')