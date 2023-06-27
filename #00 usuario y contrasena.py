# En este código, se crea una ventana con etiquetas para el usuario
#y la contraseña, entradas para que el usuario pueda ingresar sus credenciales,
# un botón para verificar las credenciales y una etiqueta para mostrar el resultado
#de la verificación. Cuando se hace clic en el botón "Verificar", se llama a la función
#"verificar_credenciales", que verifica si el usuario y la contraseña ingresados son
#correctos. El resultado de la verificación
#se muestra en la etiqueta resultado
#FALTA AGREGAR UN INPUT PARA SOLICITAR NOMBRE Y CONTRASE#A
#una ventana de reguistro y que se  guarde el usuario

from tkinter import *
  
def verificar_credenciales():
    usuario_correcto = "antonio"
    contrasena_correcta = "8514982"
    
    usuario = entrada_usuario.get()
    contrasena = entrada_contrasena.get()
    
    if usuario == usuario_correcto and contrasena == contrasena_correcta:
        etiqueta_resultado.config(text="Bienvenido al programa que te va permitir a reprogramar tu subconciente")
    else:
        etiqueta_resultado.config(text="Usuario o contraseña inválido")

ventana = Tk()
ventana.title("Verificación de credenciales")
ventana.geometry("400x200")

etiqueta_usuario = Label(ventana, text="Usuario: ")
etiqueta_usuario.pack()



entrada_usuario = Entry(ventana)
entrada_usuario.pack()

etiqueta_contrasena = Label(ventana, text="Contraseña: ")
etiqueta_contrasena.pack()

entrada_contrasena = Entry(ventana, show="*")
entrada_contrasena.pack()

boton_verificar = Button(ventana, text="Verificar", command=verificar_credenciales)
boton_verificar.pack()

etiqueta_resultado = Label(ventana, text="")
etiqueta_resultado.pack()


print("*************************************************************************************")
print("* Sistema diseñado para programar el subconciente en cuarenta practicas de meditacion *")
print("****************************************************************************************\n")


ventana.mainloop()





























