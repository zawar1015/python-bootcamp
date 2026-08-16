from pathlib import Path
import shutil

source_folder = Path(r"C:\Users\zawar\Downloads")


folders = {
    ".csv": "CSV",
    ".xlsx": "Excel",
    ".pdf": "PDF",
    ".png": "Images",
    ".jpg": "Images",
    ".txt": "Text",
    ".docx":"word_file",
    ".pptx":"power_point",
    ".xlsx": "excel",
    ".mp4" : "media",
    ".class":"class_file",
    ".java" :"java_files",
    ".ms14" :"multisim",
    ".zip"  :"zip_files",
    ".py"   :"python_files",
    ".ipynb":"jupyter_file",
    ".parquet":"parquet",
    ".sql"    : "sql_file",
    ".html"   :"html_file",
    ".css"    :"css_file",
    ".js"     :"javascript"
}



for file in source_folder.iterdir():
    if not file.is_file():
        continue


    extention = file.suffix.lower()


    if extention in folders:
        folder_name = folders[extention]
        destination_folder = source_folder/folder_name


        destination_folder.mkdir(exist_ok=True)


        destination = destination_folder/file.name

        shutil.move(file,destination)