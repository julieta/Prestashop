import unittest
from unittest import TestLoader, TestSuite, TextTestRunner

import Test
#acá abajo van el nombre de todos los test que tengo
#from Test.test_Verify_Login_Success import TestLoginSuccess
#from Test.test_Verify_FooterComponent import TestFooterComponent
#from Test.test_Verify_HoverColor_One_Product import TestHoverColorOneProduct
from Test.test_example import TestExample

if __name__ == '__main__':
    loader = TestLoader()
    suite = TestSuite((
        loader.loadTestsFromTestCase(TestExample)
        #loader.loadTestsFromTestCase(TestFooterComponent),
        #loader.loadTestsFromTestCase(TestHoverColorOneProduct)
    ))
    runner = TextTestRunner(verbosity=3)
    runner.run(suite)

#(ver)para ejecutar esta suite lo que se hace es correr el comando py.test Test/test_Runner_Sanity_Chrome.py --browser chrome
