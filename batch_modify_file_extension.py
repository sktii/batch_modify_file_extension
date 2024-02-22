import os

def process_files_in_folder(folder_path):
    if not os.path.exists(folder_path):
        print(f"指定的文件夾 '{folder_path}' 不存在。")
        return

    for filename in os.listdir(folder_path):
        if '.' in filename:
            # 取得檔案的副檔名
            old_extension = filename.split('.')[-1]

            # 如果副檔名是SPE，就將其修改為txt
            if old_extension == 'docx':
                new_filename = filename.rsplit('.', 1)[0] + '.txt'
                old_path = os.path.join(folder_path, filename)  
                new_path = os.path.join(folder_path, new_filename) 
                os.rename(old_path, new_path)
                print(f"已將 '{filename}' 修改為 '{new_filename}'")

if __name__ == "__main__":
    folder_path = r"C:\Users\ASUS\Desktop\test"
    process_files_in_folder(folder_path)
