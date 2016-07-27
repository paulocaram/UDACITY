import os
import time

def rename_files():
    file_list = os.listdir(r"C:\estudo_python\udacity\secreto")
    save_path = os.getcwd()
    os.chdir(r"C:\estudo_python\udacity\secreto")
  
    for list in file_list:
        print "Arquivo antigo...: ", list
        print "Arquivo renomeado: ", list.translate(None,"0123456789")
        time.sleep(1)
        os.rename(list,list.translate(None,"0123456789"))

    print "Terminado"
    os.chdir(save_path)


if __name__ == '__main__':
    rename_files()
