__author__ = 'mdzhachvadze'

#If move this script to core there will be the error:
#Traceback (most recent call last):
#  File "C:\Users\MDzhachvadze\PycharmProjects\test\src\core\float_point_test.py", line 7, in <module>
#    from decimal import Decimal
#  File "C:\Python27\lib\decimal.py", line 3737, in <module>
#    _numbers.Number.register(Decimal)
#AttributeError: 'module' object has no attribute 'Number'


from decimal import Decimal

print "0.1 + 0.1 - 0.2=", 0.1 + 0.1 - 0.2
print "Decimal('0.1') + Decimal('0.1') - Decimal('0.2')=", Decimal('0.1') + Decimal('0.1') - Decimal('0.2')
