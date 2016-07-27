import os


def rename_files():
    file_list = os.listdir(r"C:\estudo_python\udacity\prank")
    save_path = os.getcwd()
    print "Diretorio corrente: ", save_path
    os.chdir(r"C:\estudo_python\udacity\prank")
    
    for file_name in file_list:
        print "Arquivo antigo: ", file_name
        print "Arquivo Novo: ", file_name.translate(None,"0123456789")
        os.rename(file_name,file_name.translate(None,"0123456789"))

    print "Renomeados...."
    os.chdir(save_path)
        
        
if __name__ == '__main__':
    rename_files()
