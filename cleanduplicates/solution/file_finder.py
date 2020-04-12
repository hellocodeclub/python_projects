import os
from cleanduplicates.solution.utils import  get_hash, merge_two_dicts

class FileFinder:
    def __init__(self):
        self.tracking_files_dict = {}

    def find_duplicated_files(self, folder):
        tracking_files = {}

        try:
            with os.scandir(folder) as current_folder:
                for filename in current_folder:
                    if filename.is_dir():
                        tracking_files = merge_two_dicts(tracking_files, self.find_duplicated_files(filename.path))
                    else:
                        if(filename.name[0]=='.'):
                            continue;
                        current_file_name = filename.name
                        current_file_hash = get_hash(filename)
                        current_file_location = filename.path
                        current_memory_in_bytes = os.stat(filename.path).st_size

                        file_details = FileDetails(current_file_name,current_file_location, current_file_hash, current_memory_in_bytes)

                        if filename.name not in tracking_files:
                            tracking_files[filename.name] = [ file_details ]
                        else:
                            tracking_files[filename.name].append(file_details)
                            tracking_files[filename.name].sort(key=order_by_path_lenght)

            self.tracking_files_dict =tracking_files
        except PermissionError:
            return {}
        return tracking_files

    def get_tracking_files_dict(self):
        return self.tracking_files_dict

    def get_total_memory(self):

        return 0

def order_by_path_lenght(filedetails):
    return len(filedetails.location)

class FileDetails:
    def __init__(self,filename, location, sha1hash, memory):
        self.filename = filename
        self.location = location
        self.sha1hash = sha1hash
        self.memory_in_bytes = memory
