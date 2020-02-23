import unittest
from binding import network_automation

class TestYangModels(unittest.TestCase):

    def setUp(self):
        self.na = network_automation()
        self.projects = self.na.network_automation_projects.network_automation_project
        self.engineers = self.na.network_automation_engineers.network_automation_engineer
    
    def set_project_type(self, name):
        self.projects.add("Network AI")
        self.projects["Network AI"].project_type = name
    
    def set_engineer_first_name(self, name):
        self.engineers.add("sjn")
        self.engineers["sjn"].first_name = name


    def test_adding_a_project(self):
        self.projects.add("Network AI")
        self.assertTrue(self.projects["Network AI"])
    
    def test_project_type_fail(self):
        with self.assertRaises(Exception):
            self.set_project_type("Bad Project Type")

    def test_project_type_pass(self):
        try:
            self.set_project_type("internal")
        except:
            self.fail("Exception raised")

    def test_engineer_fname_fail(self):
        try:
            self.set_engineer_first_name("sam")
        except:
            pass
        else:
            self.fail("Exception should have been raised but was not")

    def test_engineer_fname_pass(self):
        try:
            self.set_engineer_first_name("Sam")
        except:
            self.fail("Exception raised")

if __name__ == '__main__':
    unittest.main()