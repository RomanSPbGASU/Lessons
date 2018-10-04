import unittest
from datetime import date as d, datetime as dt
#import L3E6

start_date = d(1,1,1)
end_date = d(9999,31,12)



#date = d(1, 1, 1)
#date.toordinal()
#print(date)
#new_date = d(date.year, date.month, date.day + 100)
#print(new_date)




class TestRegExp(unittest.TestCase):
    def test_date(self):
        # прогоним циклом все корректные даты (преобразованные в строку)
        date = date()
        date.toordinal()
        print(date)



    def test_year(self):
        # true section
        self.assertTrue(ptrn.search("11.11.1234"))
        self.assertTrue(ptrn.search("11.11.0001"))
        self.assertTrue(ptrn.search("11.11.9999"))
        # false section
        self.assertFalse(ptrn.search("11.11.0000"))
        self.assertFalse(ptrn.search("11.11.abcd"))
        self.assertFalse(ptrn.search("11.11.qwertyuiop"))
        self.assertFalse(ptrn.search("11.11."))
        self.assertFalse(ptrn.search("11.11....."))
        self.assertFalse(ptrn.search(r"11.11.\\\\"))
    def test_month(self):
        #true section
        pass
        #false section

    def test_day(self):
        #true section
        pass
        #fasle section
        self.assertFalse(ptrn.search("00.11.1111"))
        self.assertFalse(ptrn.search("30.02.1111"))
        self.assertFalse(ptrn.search("32.11.1111"))

    def test_sep(self):
        #true section
        self.assertTrue(ptrn.search("11.11.1111"))
        self.assertTrue(ptrn.search("11/11/1111"))
        #false section
        self.assertFalse(ptrn.search("11.11/1111"))
        self.assertFalse(ptrn.search("11/11.1111"))
               

if __name__ == '__main__':
    unittest.main()