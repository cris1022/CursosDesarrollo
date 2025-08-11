archivo= open('prueba1.txt','w')
archivo.write('Este es la actualizacion del archivo\n')
archivo.write('Este es la segunda del archivo\n')
archivo.writelines(['esta ', 'es la '])

archivo.close()
