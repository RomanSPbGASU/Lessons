import unittest
import sys
from datetime import date as d, datetime as dt, timedelta
import time
from L3E6 import ptrn

#start_date = d(1,1,1)
#end_date = d(9999,12,31)
#file1 = open(r"D:\Desktop\Python\Lessons Python\L4\dates1.txt", 'w')
#file2 = open(r"D:\Desktop\Python\Lessons Python\L4\dates2.txt", 'w')
#start = dt.now()
#for single_date in (start_date + timedelta(n) for n in range(int((end_date - start_date).days))):
#    file1.write(single_date.strftime("%d/%m/%Y\n"))
#    file2.write(single_date.strftime("%d.%m.%Y\n"))
#duration = dt.now() - start
#print(duration.seconds, ".%06d" % duration.microseconds, sep = "")


#dates = [[single_date.strftime("%d/%m/%Y"), single_date.strftime("%d.%m.%Y")] for single_date in (start_date + timedelta(day)) for day in range(int((end_date - start_date).days))]
#print(dates)

#date = d(1, 1, 1)
#date.toordinal()
#print(date)
#new_date = d(date.year, date.month, date.day + 100)
#print(new_date)




class TestRegExp(unittest.TestCase):
    file1 = open(r"D:\Desktop\Python\Lessons Python\L4\dates1.txt")
    file2 = open(r"D:\Desktop\Python\Lessons Python\L4\dates2.txt")
    for i in range(10):
        print(file1.read())
        print(file2.read())

    def test_date(self):
        # прогоним циклом все корректные даты (преобразованные в строку)
        file1 = open(r"D:\Desktop\Python\Lessons Python\L4\dates1.txt")
        file2 = open(r"D:\Desktop\Python\Lessons Python\L4\dates2.txt")
        for line in range(file1):
            self.assertTrue(ptrn.search(line.read()))

        for line in range(file2):
            self.assertTrue(ptrn.search(line.read()))

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
        self.assertTrue(ptrn.search("11.01.1111"))
        self.assertTrue(ptrn.search("11.12.1111"))
        self.assertTrue(ptrn.search("11.10.1111"))
        self.assertTrue(ptrn.search("11.09.1111"))
        #false section
        self.assertFalse(ptrn.search("11.13.1111"))
        self.assertFalse(ptrn.search("11.00.1111"))
        self.assertFalse(ptrn.search("11.0.1111"))
        self.assertFalse(ptrn.search("11..1111"))
        self.assertFalse(ptrn.search("11.ab.1111"))
        self.assertFalse(ptrn.search("11./.1111"))
        self.assertFalse(ptrn.search("11...1111"))


    def test_day(self):
        #true section
        self.assertTrue(ptrn.search("01.11.1111"))
        self.assertTrue(ptrn.search("30.11.1111"))
        self.assertTrue(ptrn.search("29.02.2020"))

        #fasle section
        self.assertFalse(ptrn.search("00.11.1111"))
        self.assertFalse(ptrn.search("0.11.1111"))
        self.assertFalse(ptrn.search("30.02.1111"))
        self.assertFalse(ptrn.search("32.11.1111"))
        self.assertFalse(ptrn.search("29.02.2100"))
        self.assertFalse(ptrn.search("29.02.2018"))
        self.assertFalse(ptrn.search(".11.1111"))
        self.assertFalse(ptrn.search("ab.02.2018"))
        self.assertFalse(ptrn.search(".......02.2018"))


    def test_sep(self):
        #true section
        self.assertTrue(ptrn.search("11.11.1111"))
        self.assertTrue(ptrn.search("11/11/1111"))
        #false section
        self.assertFalse(ptrn.search("11.11/1111"))
        self.assertFalse(ptrn.search("11/11.1111"))
               

if __name__ == '__main__':
    unittest.main()