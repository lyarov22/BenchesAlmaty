import os
import shutil

def copy_code_to_txt(input_directory, output_file):
    with open(output_file, 'w', encoding='utf-8') as output_txt:
        for root, dirs, files in os.walk(input_directory):
            for file in files:
                if file.endswith(".py"):
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r', encoding='utf-8') as input_file:
                        output_txt.write(f"{'='*20} {file_path} {'='*20}\n")
                        output_txt.write(input_file.read())
                        output_txt.write("\n\n")
                        
# Замените 'input_directory' на путь к вашей директории и 'output_file' на путь и имя файла для сохранения кода
input_directory = './'
output_file = './text.txt'

copy_code_to_txt(input_directory, output_file)
