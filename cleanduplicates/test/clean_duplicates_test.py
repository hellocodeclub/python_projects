import unittest
import os
from cleanduplicates.solution.clean_duplicates import find_duplicates,list_duplicated_file


class CleanDuplicateTest(unittest.TestCase):
    def test1(self):
        create_duplicates_folder()
        dict = find_duplicates('.')
        list = list_duplicated_file(dict)
        self.assertEqual(2,len(list))
        list.sort()
        self.assertTrue('duplicate_test/subfolder/file1' in list[0])
        self.assertTrue('duplicate_test/subfolder/file2' in list[1])
        delete_duplicates_folder()
        return

def create_duplicates_folder():
    os.mkdir('duplicate_test')
    os.mkdir('duplicate_test/subfolder')
    create_file('duplicate_test/file1','Hello there')
    create_file('duplicate_test/subfolder/file1','Hello there')
    create_file('duplicate_test/file2','Hello there')
    create_file('duplicate_test/subfolder/file2','Hello there')

def delete_duplicates_folder():
    os.remove('duplicate_test/file1')
    os.remove('duplicate_test/subfolder/file1')
    os.remove('duplicate_test/file2')
    os.remove('duplicate_test/subfolder/file2')
    os.rmdir('duplicate_test/subfolder')
    os.rmdir('duplicate_test')

def create_file(filename,content):
    f = open(filename, "w")
    f.write(content)
    f.close()

if __name__ =='__main__':
    unittest.main()