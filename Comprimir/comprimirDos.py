import zipfile
import os
from zipfile import *

def comprimir():
    nombreZip='Ejemplo'
    ubicacionZip='comprimido'
    ubicacionArchivo='archivos'
    nombreArchivo='texto'
    extensionArchivo='txt'
    jungle_zip = zipfile.ZipFile(ubicacionZip+'/'+nombreZip+'.zip', 'w')
    jungle_zip.write(ubicacionArchivo+'/'+nombreArchivo+'.'+extensionArchivo, compress_type=zipfile.ZIP_DEFLATED)
    jungle_zip.close()

def extraer():
    nombreZip='Ejemplo'
    ubicacionZip='comprimido'
    carpetaExtraer='extraido'#carpeta extraida
    ubicacionExtraer='archivos'
    archivoExtraer='texto'
    extensionExtraer='txt'
    archivo_zip = zipfile.ZipFile(ubicacionZip+'/'+nombreZip+'.zip')
    archivo_zip.extract(ubicacionExtraer+'/'+archivoExtraer+'.'+extensionExtraer, carpetaExtraer)
    archivo_zip.close()

def extraerTipoArchivo():
    nombreZip='Ejemplo'
    ubicacionZip='comprimido'
    carpetaExtraer='extraerTipoArchivo'
    archivo_zip = zipfile.ZipFile(ubicacionZip+'/'+nombreZip+'.zip')

    for file in archivo_zip.namelist():
        if archivo_zip.getinfo(file).file_size < 1024*1024:
            archivo_zip.extract(file, carpetaExtraer)

    archivo_zip.close()

def informacionArchivo():
    nombreZip='Ejemplo'
    ubicacionZip='comprimido'
    ubicacionExtraer='archivos'
    archivoExtraer='texto'
    extensionExtraer='txt'

    archivo_zip = zipfile.ZipFile(ubicacionZip+'/'+nombreZip+'.zip')
    info= archivo_zip.getinfo(ubicacionExtraer+'/'+archivoExtraer +'.'+extensionExtraer )
    
    print(info.date_time)
    print(info.compress_size)
    print(info.file_size)
            
    archivo_zip.close()


        
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