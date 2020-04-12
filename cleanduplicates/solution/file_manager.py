import os
from cleanduplicates.solution.file_finder import FileFinder


class FileManager:
    def __init__(self, folder):
        self.folder = folder
        self.file_finder = FileFinder()
        self.duplicates_filename_path_list = []

    def find_duplicated_files(self):
        self.duplicates_details_dict_by_filename = self.file_finder.find_duplicated_files(self.folder)
        return self.calculate_duplicated_list()

    def calculate_duplicated_list(self):
        list_duplicated = []
        for filename in self.duplicates_details_dict_by_filename:
            list_given_file = self.duplicates_details_dict_by_filename[filename]
            if (len(list_given_file)>1):
                for index  in range(1,len(list_given_file)):
                    if(list_given_file[0].sha1hash ==list_given_file[index].sha1hash):
                        list_duplicated.append(list_given_file[index].location)
        self.duplicates_filename_path_list = list_duplicated
        return self.duplicates_filename_path_list

    def get_duplicates_list(self):
        return self.duplicates_filename_path_list

    def calculate_total_memory(self):
        dict = self.file_finder.g
        return

    def remove_duplicates(self):
        for item in self.duplicates_filename_path_list:
            os.remove(item)