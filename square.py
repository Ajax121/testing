'''
jbj
'''
import warnings

def squ(num):
    '''
    hgj
    '''
    if isinstance(num,float):  # dont do  type(num) == float
        warnings.warn('inp of type float will be converted to int')
        num = int(num)
    return num ** 2
