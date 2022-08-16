import unittest

def duplicateelement(lista):
    vacia = []
    for x in lista: 
        vacia.append(x)
        vacia.append(x)

    return  vacia 



class TestStringMethods(unittest.TestCase):

    def test_listoutput(self):
        self.assertEqual(duplicateelement([1,2, 3]), [1,1,2,2,3,3]) 

    

if __name__ == '__main__':
    unittest.main()