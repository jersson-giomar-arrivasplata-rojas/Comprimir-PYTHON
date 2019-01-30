import zipfile
import os

def do_POST():
    print('archivo')
        
def comprimirFile(file):
    print('archivo')

    archivo= file.args
    ubicacionZip='comprimido'
    file_name = os.path.basename(archivo)
    jungle_zip = zipfile.ZipFile(ubicacionZip+'/'+file_name+'.zip', 'w')
    jungle_zip.write(file, compress_type=zipfile.ZIP_DEFLATED)
    jungle_zip.close()


#comprimir()
#extraer()
#extraerTipoArchivo()
#informacionArchivo()