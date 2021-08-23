import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait, expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class Baseclass:

    def getlogger(self):
        logger = logging.getLogger(__name__)

        fileHandler = logging.FileHandler('logfile.log', mode='a')
        formatter = logging.Formatter("%(asctime)s : %(levelname)s: %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)

        logger.setLevel(logging.INFO)
        return logger
        # logger.debug("debug starts")
        # logger.info("Information starts")
        # logger.warning("Some warning occured")
        # logger.error("Some error occured")
        # logger.critical("Critical issue")

    # wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//a[text()='India']")))
    def verifyTextPresence(self, in_text):
        wait = WebDriverWait(self.driver, 8)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//a[text()='{}']".format(in_text))))