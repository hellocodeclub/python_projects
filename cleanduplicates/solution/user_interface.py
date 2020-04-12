import tkinter as tk
import pygubu
from cleanduplicates.solution.file_manager import FileManager


class Application(pygubu.TkApplication):

    def _create_ui(self):

        self.builder = pygubu.Builder()

        self.builder.add_from_file('test_ui.ui')

        self.main_window = self.builder.get_object('Frame_1', self.master)

        self.builder.connect_callbacks(self)

        self.file_manager = None


    def on_find_duplicates_click(self):
        folder_selected = self.builder.get_object('folder_entry').get()

        self.file_manager = FileManager(folder_selected)
        self.duplicates_list = self.file_manager.find_duplicated_files()

        treeview = self.builder.get_object('list_duplicates_treeview')
        if(len(self.duplicates_list) == 0):
            treeview.insert('','end', text= 'No duplicated files')
        else:
            for filename in self.duplicates_list:
                treeview.insert('','end', text= filename)

    def on_clean_button_click(self):
        self.file_manager =self.file_manager.remove_files()
        treeview =self.builder.get_object('list_duplicates_treeview')
        for i in treeview.get_children():
            treeview.delete(i)


if __name__=='__main__':
    root = tk.Tk()
    app = Application(root)
    app.run()