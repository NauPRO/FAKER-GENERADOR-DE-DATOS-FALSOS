import tkinter as tk
from tkinter import scrolledtext, messagebox
import webbrowser
from faker import Faker

# Lista de países con sus códigos para Faker
paises = {
    "Argentina": "es_AR",
    "España": "es_ES",
    "Brasil": "pt_BR",
    "México": "es_MX",
    "Francia": "fr_FR",
    "Alemania": "de_DE",
    "Italia": "it_IT",
    "Reino Unido": "en_GB",
    "Colombia": "es_CO",
    "Estados Unidos": "en_US"
}

# Función para generar datos falsos
# Función para generar datos falsos
def generar_datos_falsos(pais=""):
    datos = []
    Faker.seed(0)  # Para tener datos consistentes (semilla fija)
    
    # Configurar Faker con el país seleccionado
    if pais:
        fake = Faker(pais)  # Establecer el país seleccionado
    else:
        fake = Faker()  # Si no se selecciona país, generamos datos globales

    for _ in range(5):
        nombre = fake.name()
        direccion = fake.address().replace("\n", ", ")  # Limpiar nueva línea en la dirección
        correo = fake.email()
        telefono = fake.phone_number()
        ciudad = fake.city()
        fecha_nacimiento = fake.date_of_birth(minimum_age=18, maximum_age=85).strftime('%Y-%m-%d')
        profesion = fake.job()
        compania = fake.company()
        tarjeta_credito = fake.credit_card_number(card_type='mastercard')
        usuario_instagram = fake.user_name()
        estado_civil = fake.random_element(elements=('Soltero', 'Casado', 'Divorciado', 'Viudo'))
        
        # Usamos 'postcode()' en lugar de 'zipcode()'
        codigo_postal = fake.postcode()
        
        fecha_registro = fake.date_this_decade().strftime('%Y-%m-%d')
        ip = fake.ipv4()

        persona = {
            "Nombre": nombre,
            "Dirección": direccion,
            "Correo": correo,
            "Teléfono": telefono,
            "Ciudad": ciudad,
            "Fecha de Nacimiento": fecha_nacimiento,
            "Profesión": profesion,
            "Compañía": compania,
            "Tarjeta de Crédito": tarjeta_credito,
            "Instagram": usuario_instagram,
            "Estado Civil": estado_civil,
            "Código Postal": codigo_postal,
            "Fecha de Registro": fecha_registro,
            "IP": ip
        }
        
        datos.append(persona)
    
    return datos

# Función para mostrar los datos en el cuadro de texto
def mostrar_datos():
    pais = pais_var.get()  # Obtener el país seleccionado
    datos_generados = generar_datos_falsos(paises[pais])  # Generar datos según el país seleccionado
    output_text.delete(1.0, tk.END)  # Limpiar el cuadro de texto antes de mostrar los nuevos datos
    
    for i, persona in enumerate(datos_generados, 1):
        output_text.insert(tk.END, f"Persona {i}:\n")
        for key, value in persona.items():
            output_text.insert(tk.END, f"  {key}: {value}\n")
        output_text.insert(tk.END, "\n")

# Función para abrir Telegram y mostrar el mensaje emergente
def abrir_telegram_y_mensaje():
    # Abrir enlace de Telegram (reemplaza con tu link de Telegram)
    webbrowser.open("https://t.me/tu_usuario")  # Cambia "tu_usuario" por tu nombre de usuario o enlace directo
    
    # Mostrar mensaje emergente con créditos
    messagebox.showinfo("Créditos", "Créditos: Noctámbulo")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Faker.py")
ventana.geometry("600x600")  # Tamaño de la ventana
ventana.configure(bg="#d3d3d3")  # Establecer color gris de fondo

# Establecer el icono de la ventana
ventana.iconbitmap("Fakericon.ico")  # Asegúrate de tener el archivo 'Fakericon.ico' en el mismo directorio

# Ejecutar la función de abrir Telegram y mostrar el mensaje emergente al iniciar
ventana.after(100, abrir_telegram_y_mensaje)  # Se ejecuta después de 100 ms

# Etiqueta de título
titulo_label = tk.Label(ventana, text="Generador de Datos Falsos", font=("Arial", 18), bg="#d3d3d3")
titulo_label.pack(pady=10)

# Botón para generar los datos
generar_button = tk.Button(ventana, text="Generar Datos", command=mostrar_datos, font=("Arial", 14), bg="lime", fg="black", relief="solid")
generar_button.pack(pady=10)

# Dropdown (OptionMenu) para seleccionar el país
pais_var = tk.StringVar(ventana)
pais_var.set(list(paises.keys())[0])  # Establecer Argentina como valor por defecto

pais_menu = tk.OptionMenu(ventana, pais_var, *paises.keys())
pais_menu.config(font=("Arial", 12), bg="lime", fg="black")
pais_menu.pack(pady=10)

# Cuadro de texto para mostrar los datos generados
output_text = scrolledtext.ScrolledText(ventana, width=70, height=20, font=("Courier New", 12), bg="black", fg="lime", wrap=tk.WORD)
output_text.pack(pady=10)

# Iniciar la interfaz gráfica
ventana.mainloop()
