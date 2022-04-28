import time
import pytest
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
import json
from colorama import Fore, Back, Style
import HtmlTestRunner
from Utils import utils as utils
from Utils.BaseClass import BaseClass

@pytest.mark.usefixtures("test_setup")
class TestExample(BaseClass):

    def test_example(self):
        log = self.get_Logger()
        driver = self.driver
        log.info("paso 1")
        log.info("paso 2")
        log.info("paso 3")
