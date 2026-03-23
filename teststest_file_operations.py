import os
import tempfile
import unittest
import shutil
from file_operations import copy_file, delete_path

class TestFileOperations(unittest.TestCase):

    def setUp(self):
    
        self.test_dir = tempfile.mkdtemp()
        self.source_file = os.path.join(self.test_dir, "source.txt")
        with open(self.source_file, "w") as f:
            f.write("test content")

    def tearDown(self):
    
        shutil.rmtree(self.test_dir, ignore_errors=True)

    def test_copy_file_to_file(self):
        dest = os.path.join(self.test_dir, "dest.txt")
        copy_file(self.source_file, dest)
        self.assertTrue(os.path.exists(dest))
        with open(dest) as f:
            self.assertEqual(f.read(), "test content")

    def test_copy_file_to_dir(self):
        subdir = os.path.join(self.test_dir, "subdir")
        os.mkdir(subdir)
        copy_file(self.source_file, subdir)
        expected = os.path.join(subdir, "source.txt")
        self.assertTrue(os.path.exists(expected))

    def test_copy_nonexistent_source(self):
        with self.assertRaises(FileNotFoundError):
            copy_file("nonexistent.txt", "dest.txt")

    def test_copy_directory_as_source(self):
        with self.assertRaises(IsADirectoryError):
            copy_file(self.test_dir, "dest.txt")

    def test_delete_file(self):
        file_path = os.path.join(self.test_dir, "to_delete.txt")
        with open(file_path, "w"):
            pass
        delete_path(file_path)
        self.assertFalse(os.path.exists(file_path))

    def test_delete_directory(self):
        dir_path = os.path.join(self.test_dir, "to_delete_dir")
        os.mkdir(dir_path)
        delete_path(dir_path)
        self.assertFalse(os.path.exists(dir_path))

    def test_delete_nonexistent(self):
        with self.assertRaises(FileNotFoundError):
            delete_path("nonexistent")

if __name__ == "__main__":
    unittest.main()


    