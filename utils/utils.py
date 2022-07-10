import softest
import logging


class utilities(softest.TestCase):

    def soft_Assert(self, List, value):
        for i in List:
            self.soft_assert(self.assertIn, value, i.text)
            print('Pass', end=' ')

    def _loggers(self):
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)
        ch = logging.StreamHandler()
        fh = logging.FileHandler(filename='demologger.log')
        formatter = logging.Formatter('%(asctime)s - %(levelname)s : %(message)s')
        ch.setFormatter(formatter)
        fh.setFormatter(formatter)
        logger.addHandler(ch)
        logger.addHandler(fh)
        return logger
