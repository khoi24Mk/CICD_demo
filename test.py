import unittest;
# import calc;
import cffi;
import importlib;
print("TESTING")

def load(filename):
	source = open(filename+'.c').read()
	includes = open(filename+'.h').read()
	
	ffibuilder = cffi.FFI()
	ffibuilder.cdef(includes)
	ffibuilder.set_source(filename+'_',source)
	ffibuilder.compile()
	
	module = importlib.import_module(filename+'_')
	return module.lib
 
    

class TestCalc(unittest.TestCase):
    def test_add(self):
        print("OK")
        module = load('sum')
        self.assertEqual(module.sum(1,2),1+2)