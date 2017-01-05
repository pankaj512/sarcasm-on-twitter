import tkinter as tk
import pygubu
from application import svm, naive_bayes

import os


class Application:
    def __init__(self, master):
        os.chdir('../application/')
        self.master = master
        # 1: Create a builder
        self.builder = builder = pygubu.Builder()

        # 2: Load an ui file
        builder.add_from_file('gui.ui')

        # 3: Create the widget using a master as parent
        self.mainwindow = builder.get_object('main_window', master)

        builder.connect_callbacks(self)

    def on_classify_click(self):
        selected_classifier = self.builder.get_variable('selected_classifer').get()
        selected_size = self.builder.get_variable('size_of_train').get()
        # print(selected_classifier, selected_size)

        if selected_classifier!='' and selected_size!='':

            error_label = self.builder.get_variable('error_label')
            error_label.set('')

            if selected_classifier == 'Support_Vector_Machine(SVM)':
                normal_size, sarcastic_size, accuracy = svm.svm_classifier(float(selected_size))
            elif selected_classifier == 'Naive_Bayes':
                normal_size, sarcastic_size, accuracy = naive_bayes.naive_classifier(float(selected_size))

            out_classifier_label = self.builder.get_variable('out_front_print')
            out_classifier_label.set(selected_classifier)

            out_normal_size_label = self.builder.get_variable('out_normal_data_print')
            out_normal_size_label.set(normal_size)

            out_sarcastic_size_label = self.builder.get_variable('out_sarcastic_data_print')
            out_sarcastic_size_label.set(sarcastic_size)

            out_accuracy_label = self.builder.get_variable('out_accuracy_print')
            out_accuracy_label.set(accuracy)
        elif selected_classifier =='':
            error_label = self.builder.get_variable('error_label')
            error_label.set('Please select Classifier !!')
        elif selected_size=='':
            error_label = self.builder.get_variable('error_label')
            error_label.set('Please select training Size !!')
        else:
            print("Please Select valid input")


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Sarcasm Classifier')
    app = Application(root)
    root.mainloop()