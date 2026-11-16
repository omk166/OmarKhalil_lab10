import runpy
import unittest

from app import greet, main


class TestApp(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("World"), "Hello, World from Omar Khalil!")

    def test_student_name(self):
        self.assertEqual(greet("Omar"), "Hello, Omar from Omar Khalil!")


def test_main(capsys):
    main()
    assert capsys.readouterr().out == "Hello, World from Omar Khalil!\n"


def test_script_entry_point(capsys):
    runpy.run_module("app", run_name="__main__")
    assert capsys.readouterr().out == "Hello, World from Omar Khalil!\n"
