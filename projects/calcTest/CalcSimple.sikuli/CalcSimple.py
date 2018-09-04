from sikuli import *
import unittest

class BaseActionsTests(unittest.TestCase):
    """Tests for base calc actions (add, sub, mul, div)"""
        
    @classmethod
    def setUpClass(cls):
        """setUpClass: start calc if it was not started"""
        print("")
        print("=> Start base actions test")
        try:
            if not exists("1534765309922.png"):                
                print("=> Start calc")
                App.open("calc")            
        except:
            App.open("calc") 
        
        wait("1534765309922.png")        
        type("1", KEY_ALT)
    
    @classmethod
    def tearDownClass(cls):
        """tearDownClass: pass"""        
        pass
    
    def setUp(self):        
        """setUp: pass"""
        pass

    def tearDown(self):
        """tearDown: clear calc value"""
        type(Key.ESC)

        
    def test_add(self):
        #"""Test action: add"""
        click("1534765352123.png")
        click("1534765427453.png")
        click("1534765482107.png")
        click("1534765492363.png")
        if exists("1534766358843.png"):
            self.assertTrue(True)
        else:
            self.assertTrue(False, "1 + 7 = 8 : ERROR!")
    
    def test_sub(self):
        #"""Test action: sub"""
        click("1534765482107.png")
        click("1534765514962.png")
        click("1534765352123.png")
        click("1534765492363.png")
        if exists("1534765540803.png"):
            self.assertTrue(True)
        else:
            self.assertTrue(False, "7 - 1 = 6 : ERROR!")

    def test_mul(self):
        #"""Test action: mul"""
        click("1534765482107.png")
        click("1534765577675.png")
        click("1534765540803.png")
        click("1534765492363.png")
        if exists("1534765605275.png"):
            self.assertTrue(True)
        else:
            self.assertTrue(False, "7 * 6 = 42 : ERROR!")

    def test_div(self):
        #"""Test action: div"""
        click("1534765472122.png")
        click("1534765625202.png")
        click("1534765633438.png")
        click("1534765492363.png")
        if exists("1534765656914.png"):
            self.assertTrue(True)
        else:
            self.assertTrue(False, "8 / 2 = 4 : ERROR!")
              

class ExtendsActionsTests(unittest.TestCase):
    """Tests for extends calc actions (1/x, sqrt)"""
    
    @classmethod
    def setUpClass(cls):
        """setUpClass: start calc if it was not started"""
        print("")
        print("=> Start extends actions test")
        try:
            if not exists("1534765309922.png"):                
                print("=> Start calc")
                App.open("calc")            
        except:
            App.open("calc") 
        
        wait("1534765309922.png")        
        type("1", KEY_ALT)
    
    @classmethod
    def tearDownClass(cls):
        """tearDownClass: pass"""        
        pass
        
    def setUp(self):        
        """setUp: pass"""
        pass

    def tearDown(self):
        """tearDown: clear calc value"""
        type(Key.ESC)
        
    def test_sqrt(self):
        #"""Test action: sqrt"""
        click("1534765352123.png")
        click("1534765540803.png")
        click("1534765702272.png")
        if exists("1534765656914.png"):
            self.assertTrue(True)
        else:
            self.assertTrue(False, "sqrt(16) = 4 : ERROR!")
    
    def test_one_div_x(self):
        #"""Test action: 1/x"""
        click("1534765739481.png")
        click("1534765751339.png")
        if exists("1534765770629.png"):
            self.assertTrue(True)
        else:
            self.assertTrue(False, "1 / 5 = 0.2 : ERROR!") 