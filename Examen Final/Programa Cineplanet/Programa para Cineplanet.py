import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

# -------------------- LOGIN --------------------
class Login(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login - Cineplanet")
        self.geometry("400x200")
        self.resizable(False, False)

        tk.Label(self, text="Código:").pack(pady=5)
        self.txtCodigo = tk.Entry(self)
        self.txtCodigo.pack()

        tk.Label(self, text="Clave:").pack(pady=5)
        self.txtClave = tk.Entry(self, show="*")
        self.txtClave.pack()

        tk.Button(self, text="Iniciar", command=self.validar).pack(pady=10)
        tk.Button(self, text="Salir", command=self.destroy).pack()

    def validar(self):
        if self.txtCodigo.get() == "admin" and self.txtClave.get() == "1234":
            self.destroy()
            VentanaPrincipal().mainloop()
        else:
            messagebox.showwarning("Error", "Credenciales incorrectas")

# -------------------- VENTANA PRINCIPAL --------------------
class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema Cineplanet")
        self.geometry("800x600")
        self.resizable(True, True)

        notebook = ttk.Notebook(self)
        notebook.pack(expand=True, fill="both")

        notebook.add(TabLimpieza(notebook), text="Limpieza")
        notebook.add(TabBoleteria(notebook), text="Boletería")
        notebook.add(TabCliente(notebook), text="Cliente")
        notebook.add(TabConfiteria(notebook), text="Confitería")
        notebook.add(TabRegistro(notebook), text="Registro")

# -------------------- LIMPIEZA --------------------
class TabLimpieza(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Canvas con scrollbar (solo para esta pestaña)
        canvas = tk.Canvas(self, highlightthickness=0)
        scrollbar = tk.Scrollbar(self, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Frame interno para scroll
        scroll_frame = tk.Frame(canvas)
        canvas.create_window((0, 0), window=scroll_frame, anchor="n")
        scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        # Contenedor principal
        contenedor = tk.Frame(scroll_frame)
        contenedor.pack(pady=20)

        # Encabezado
        tk.Label(contenedor, text="🔧 Bienvenido al Área de Limpieza", font=("Arial", 16, "bold")).pack(pady=10)

        # Lista de empleados
        empleados_frame = tk.LabelFrame(contenedor, text="Lista de Empleados", padx=10, pady=10)
        empleados_frame.pack(pady=10)
        self.listaEmpleados = tk.Listbox(empleados_frame, height=4, width=40, justify="center")
        for nombre in ["Juan Pérez", "Emil Contreras", "Pamela Quiroz", "Kevin Alcantara"]:
            self.listaEmpleados.insert(tk.END, nombre)
        self.listaEmpleados.pack()

        # Fecha
        fecha_frame = tk.Frame(contenedor)
        fecha_frame.pack(pady=10)
        tk.Label(fecha_frame, text="Fecha de limpieza:", font=("Arial", 12)).pack(side="left", padx=5)
        self.fechaLimpieza = tk.Entry(fecha_frame, justify="center", width=15)
        self.fechaLimpieza.insert(0, datetime.now().strftime("%d/%m/%Y"))
        self.fechaLimpieza.pack(side="left")

        # Salas distribuidas en 3 filas de 2
        tk.Label(contenedor, text="Seleccione la Sala que desea ingresar:", font=("Arial", 12)).pack(pady=10)
        self.estadoSalas = {}
        salas_frame = tk.Frame(contenedor)
        salas_frame.pack()

        salas = ["Sala 1", "Sala 2", "Sala 3", "Sala 4", "Sala 5", "Sala 6"]
        for i, sala in enumerate(salas):
            fila = i // 2
            columna = i % 2
            frame = tk.LabelFrame(salas_frame, text=sala, padx=10, pady=5)
            frame.grid(row=fila, column=columna, padx=20, pady=10)
            varCompleta = tk.IntVar()
            varProceso = tk.IntVar()
            varPendiente = tk.IntVar()
            tk.Checkbutton(frame, text="Limpieza Completa", variable=varCompleta).pack(anchor="w")
            tk.Checkbutton(frame, text="Limpieza en Proceso", variable=varProceso).pack(anchor="w")
            tk.Checkbutton(frame, text="Limpieza Pendiente", variable=varPendiente).pack(anchor="w")
            self.estadoSalas[sala] = (varCompleta, varProceso, varPendiente)

        # Botones finales
        botones = tk.Frame(contenedor)
        botones.pack(pady=20)
        tk.Button(botones, text="Guardar Cambios", command=self.guardar, width=20).pack(side="left", padx=10)
        tk.Button(botones, text="Salir", command=self.salir, width=20).pack(side="right", padx=10)

    def guardar(self):
        resumen = []
        for sala, (completa, proceso, pendiente) in self.estadoSalas.items():
            estado = []
            if completa.get(): estado.append("Completa")
            if proceso.get(): estado.append("En Proceso")
            if pendiente.get(): estado.append("Pendiente")
            resumen.append(f"{sala}: {', '.join(estado) if estado else 'Sin estado'}")
        messagebox.showinfo("Guardado", "\n".join(resumen))

    def salir(self):
        self.master.quit()

# -------------------- BOLETERÍA --------------------
class TabBoleteria(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        contenedor = tk.Frame(self)
        contenedor.pack(expand=True)

        self.peliculas = {
            "Deadpool and Wolverine": "Dos antihéroes se unen en una aventura caótica y llena de acción.",
            "Inside Out 2": "Las emociones de Riley enfrentan nuevos desafíos en su adolescencia.",
            "Dune: Parte Dos": "Paul Atreides lidera la rebelión en el planeta Arrakis.",
            "Kung Fu Panda 4": "Po regresa para entrenar a un nuevo guerrero dragón.",
            "Oppenheimer": "La historia del físico detrás de la bomba atómica.",
            "Barbie": "Una muñeca descubre el mundo real y su identidad.",
        }

        tk.Label(contenedor, text="🎟️ Bienvenido al Área de Boletería", font=("Arial", 14)).pack(pady=10)

        tk.Label(contenedor, text="Lista de Películas en Cartelera:").pack()
        # Combobox solo lectura
        self.comboPeliculas = ttk.Combobox(contenedor, values=list(self.peliculas.keys()), width=40, state="readonly")
        self.comboPeliculas.set("Deadpool and Wolverine")
        self.comboPeliculas.pack(pady=5)
        self.comboPeliculas.bind("<<ComboboxSelected>>", self.mostrar_sinopsis)

        self.labelSinopsis = tk.Label(contenedor, text=self.peliculas["Deadpool and Wolverine"], wraplength=500, justify="left")
        self.labelSinopsis.pack(pady=5)

        tk.Label(contenedor, text="Seleccione una Sala:").pack()
        # Combobox solo lectura
        self.comboSala = ttk.Combobox(contenedor, values=["Sala 1", "Sala 2", "Sala 3", "Sala 4", "Sala 5", "Sala 6"], width=40, state="readonly")
        self.comboSala.set("Sala 1")
        self.comboSala.pack(pady=5)

        tk.Label(contenedor, text="Seleccione Fecha y Hora de la función:").pack()
        self.dateTimeFuncion = tk.Entry(contenedor, width=42, justify="center")
        self.dateTimeFuncion.insert(0, datetime.now().strftime("%d/%m/%Y %H:%M"))
        self.dateTimeFuncion.pack(pady=5)

        tk.Label(contenedor, text="Seleccione la Cantidad de boletos:").pack()
        self.spinCantidad = tk.Spinbox(contenedor, from_=1, to=20, width=5)
        self.spinCantidad.pack(pady=5)

        tk.Button(contenedor, text="Emitir Boleto", command=self.emitir, width=20).pack(pady=10)

        tk.Label(contenedor, text="Boletos Emitidos:").pack()
        self.listaBoletos = tk.Listbox(contenedor, width=60, height=5)
        self.listaBoletos.pack(pady=5)

        tk.Label(contenedor, text="Precio Total:").pack()
        self.labelPrecio = tk.Label(contenedor, text="S/. 0.00", font=("Arial", 12, "bold"))
        self.labelPrecio.pack(pady=5)

    def mostrar_sinopsis(self, event=None):
        pelicula = self.comboPeliculas.get()
        sinopsis = self.peliculas.get(pelicula, "Sinopsis no disponible.")
        self.labelSinopsis.config(text=sinopsis)

    def emitir(self):
        pelicula = self.comboPeliculas.get()
        sinopsis = self.peliculas.get(pelicula, "Sinopsis no disponible.")
        sala = self.comboSala.get()
        fecha_hora = self.dateTimeFuncion.get()
        cantidad = int(self.spinCantidad.get())
        total = cantidad * 15.00
        self.labelPrecio.config(text=f"S/. {total:.2f}")
        self.listaBoletos.insert(tk.END, f"{pelicula} | {sala} | {fecha_hora} | {cantidad} boletos")

        detalles = (
            f"🎬 Película: {pelicula}\n"
            f"📝 Sinopsis: {sinopsis}\n"
            f"📍 Sala: {sala}\n"
            f"📅 Fecha y Hora: {fecha_hora}\n"
            f"🎟️ Cantidad de Boletos: {cantidad}\n"
            f"💰 Precio Total: S/. {total:.2f}"
        )
        messagebox.showinfo("Detalles del Boleto", detalles)

# -------------------- CLIENTE --------------------
class TabCliente(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        canvas = tk.Canvas(self, highlightthickness=0)
        scrollbar = tk.Scrollbar(self, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        scroll_frame = tk.Frame(canvas)
        canvas.create_window((0, 0), window=scroll_frame, anchor="n")
        scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        contenedor = tk.Frame(scroll_frame)
        contenedor.pack(pady=10)

        self.peliculas = {
            "Deadpool and Wolverine": {"descripcion": "Dos antihéroes se unen en una aventura caótica.", "genero": "Acción / Comedia"},
            "Inside Out 2": {"descripcion": "Las emociones de Riley enfrentan nuevos desafíos.", "genero": "Animación / Familiar"},
            "Dune: Parte Dos": {"descripcion": "Paul Atreides lidera la rebelión en Arrakis.", "genero": "Ciencia Ficción / Drama"},
            "Barbie": {"descripcion": "Una muñeca descubre el mundo real y su identidad.", "genero": "Comedia / Fantasía"},
            "Kung Fu Panda 4": {"descripcion": "Po regresa para entrenar a un nuevo guerrero dragón.", "genero": "Acción / Comedia"},
            "Oppenheimer": {"descripcion": "La historia del físico detrás de la bomba atómica.", "genero": "Acción / Suspenso"},
        }

        self.historial = []

        tk.Label(contenedor, text="👤 Bienvenido Cliente", font=("Arial", 14)).pack(pady=10)

        tk.Label(contenedor, text="Clientes registrados (Socios):", font=("Arial", 12)).pack()
        self.listaSocios = tk.Listbox(contenedor, height=6, width=40, justify="center")
        for nombre in ["Axel Mendoza", "Lucía Torres", "Carlos Rivas", "Sofía Paredes", "Diego Salazar", "Valeria Quispe"]:
            self.listaSocios.insert(tk.END, nombre)
        self.listaSocios.pack(pady=5)

        tk.Label(contenedor, text="Cartelera:").pack()
        # Combobox solo lectura
        self.comboCartelera = ttk.Combobox(contenedor, values=list(self.peliculas.keys()), width=40, state="readonly")
        self.comboCartelera.set("Inside Out 2")
        self.comboCartelera.pack(pady=5)

        tk.Button(contenedor, text="Abrir detalles de Películas", command=self.abrir_detalles, width=25).pack(pady=5)
        tk.Button(contenedor, text="Comprar Entrada", command=self.comprar, width=25).pack(pady=5)

        tk.Label(contenedor, text="Historial de Compras:").pack()
        self.listaHistorial = tk.Listbox(contenedor, width=60, height=5)
        self.listaHistorial.pack(pady=5)

        tk.Button(contenedor, text="Mostrar Historial de Compras", command=self.mostrar_historial, width=25).pack(pady=10)
        tk.Button(contenedor, text="Salir", command=self.salir, width=25).pack(pady=10)

    def abrir_detalles(self):
        pelicula = self.comboCartelera.get()
        detalles = self.peliculas.get(pelicula, {})
        descripcion = detalles.get("descripcion", "Sin descripción.")
        genero = detalles.get("genero", "Sin género.")
        messagebox.showinfo("Detalles de Película", f"🎬 {pelicula}\n📝 {descripcion}\n🎞️ Género: {genero}")

    def comprar(self):
        pelicula = self.comboCartelera.get()
        fecha_hora = datetime.now().strftime("%d/%m/%Y %H:%M")
        sala = "Sala 1"
        self.historial.append({
            "pelicula": pelicula,
            "fecha_hora": fecha_hora,
            "sala": sala
        })
        self.listaHistorial.insert(tk.END, f"Entrada comprada: {pelicula}")
        messagebox.showinfo("Compra Exitosa", f"Has comprado una entrada para: {pelicula}")

    def mostrar_historial(self):
        if not self.historial:
            messagebox.showinfo("Historial", "No hay compras registradas.")
            return
        resumen = ""
        for item in self.historial:
            resumen += (
                f"🎬 Película: {item['pelicula']}\n"
                f"📅 Fecha y Hora: {item['fecha_hora']}\n"
                f"📍 Sala: {item['sala']}\n\n"
            )
        messagebox.showinfo("Historial de Compras", resumen.strip())

    def salir(self):
        self.master.quit()

# -------------------- CONFITERÍA --------------------
class TabConfiteria(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Canvas con scrollbar
        canvas = tk.Canvas(self, highlightthickness=0)
        scrollbar = tk.Scrollbar(self, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        scroll_frame = tk.Frame(canvas)
        canvas.create_window((0, 0), window=scroll_frame, anchor="n")
        scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        contenedor = tk.Frame(scroll_frame)
        contenedor.pack(pady=20)

        tk.Label(contenedor, text="🛍️ Bienvenido al Área de Confitería", font=("Arial", 16, "bold")).pack(pady=10)

        # Sección de productos
        productos_frame = tk.LabelFrame(contenedor, text="Lista de Productos", padx=10, pady=10)
        productos_frame.pack(pady=10)

        self.tablaProductos = ttk.Treeview(productos_frame, columns=("Código", "Producto", "Precio", "Marca"), show="headings", height=10)
        for col in self.tablaProductos["columns"]:
            self.tablaProductos.heading(col, text=col)
            self.tablaProductos.column(col, anchor="center", width=120)
        self.tablaProductos.pack()

        productos = [
            ("C001", "Combo Malteadas", 25.0, "Cineplanet"),
            ("C002", "Cancha Salada", 8.0, "Cineplanet"),
            ("C003", "Cancha Dulce", 8.0, "Cineplanet"),
            ("C004", "Hot Dog", 12.0, "Cineplanet"),
            ("C005", "Nachos con Queso", 15.0, "Cineplanet"),
            ("C006", "Gaseosa Mediana", 10.0, "Coca-Cola"),
            ("C007", "Gaseosa Grande", 13.0, "Coca-Cola"),
            ("C008", "Agua Mineral", 6.0, "San Luis"),
            ("C009", "Chocolates", 7.0, "Nestlé"),
            ("C010", "Combo Pareja", 30.0, "Cineplanet"),
        ]
        for item in productos:
            self.tablaProductos.insert("", "end", values=item)

        # Sección de selección y acciones
        acciones_frame = tk.Frame(contenedor)
        acciones_frame.pack(pady=10)

        seleccionados_frame = tk.LabelFrame(acciones_frame, text="Productos Seleccionados", padx=10, pady=10)
        seleccionados_frame.grid(row=0, column=0, padx=20)

        self.listaSeleccionados = tk.Listbox(seleccionados_frame, width=40, height=8)
        self.listaSeleccionados.pack()

        botones_frame = tk.Frame(acciones_frame)
        botones_frame.grid(row=0, column=1, padx=20)

        tk.Button(botones_frame, text="Agregar Producto Seleccionado", command=self.agregar_producto, width=30).pack(pady=5)
        tk.Button(botones_frame, text="Eliminar Producto Seleccionado", command=self.eliminar_producto, width=30).pack(pady=5)
        tk.Button(botones_frame, text="Confirmar Venta", command=self.confirmar_venta, width=30).pack(pady=10)

        # Total y historial
        resumen_frame = tk.Frame(contenedor)
        resumen_frame.pack(pady=10)

        total_frame = tk.Frame(resumen_frame)
        total_frame.pack()
        tk.Label(total_frame, text="Total de Confitería:", font=("Arial", 12)).pack(side="left", padx=5)
        self.labelTotal = tk.Label(total_frame, text="S/. 0.00", font=("Arial", 12, "bold"))
        self.labelTotal.pack(side="left")

        historial_frame = tk.LabelFrame(contenedor, text="Historial de Ventas", padx=10, pady=10)
        historial_frame.pack(pady=10)
        self.listaHistorial = tk.Listbox(historial_frame, width=60, height=5)
        self.listaHistorial.pack()

        # Botones finales
        botones_finales = tk.Frame(contenedor)
        botones_finales.pack(pady=15)
        tk.Button(botones_finales, text="Guardar", command=self.guardar, width=20).pack(side="left", padx=10)
        tk.Button(botones_finales, text="Salir", command=self.salir, width=20).pack(side="right", padx=10)

    def agregar_producto(self):
        selected = self.tablaProductos.selection()
        for item in selected:
            valores = self.tablaProductos.item(item)["values"]
        try:
            precio = float(valores[2])
            texto = f"{valores[1]} - S/. {precio:.2f}"
            self.listaSeleccionados.insert(tk.END, texto)
        except ValueError:
            messagebox.showerror("Error", "El precio no es válido.")

    def eliminar_producto(self):
        seleccion = self.listaSeleccionados.curselection()
        for i in reversed(seleccion):
            self.listaSeleccionados.delete(i)

    def confirmar_venta(self):
        total = 0
        for i in range(self.listaSeleccionados.size()):
            texto = self.listaSeleccionados.get(i)
            try:
                precio = float(texto.split("S/.")[1])
                total += precio
            except:
                pass
        self.labelTotal.config(text=f"S/. {total:.2f}")
        self.listaHistorial.insert(tk.END, f"Venta registrada: S/. {total:.2f}")
        self.listaSeleccionados.delete(0, tk.END)

    def guardar(self):
        messagebox.showinfo("Guardado", "Datos de confitería guardados correctamente")

    def salir(self):
        self.master.quit()

# -------------------- REGISTRO --------------------
class TabRegistro(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        canvas = tk.Canvas(self, highlightthickness=0)
        scrollbar = tk.Scrollbar(self, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        scroll_frame = tk.Frame(canvas)
        canvas.create_window((0, 0), window=scroll_frame, anchor="n")
        scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        contenedor = tk.Frame(scroll_frame)
        contenedor.pack(pady=10)

        tk.Label(contenedor, text="📝 Únete al Club Cineplanet", font=("Arial", 16)).pack(pady=10)
        tk.Label(contenedor, text="Disfruta de beneficios exclusivos, promociones y mucho más", font=("Arial", 11)).pack(pady=5)

        self.txtNombre = tk.Entry(contenedor, width=40)
        self.txtNacimiento = tk.Entry(contenedor, width=40)
        self.txtDNI = tk.Entry(contenedor, width=40)
        self.comboGenero = ttk.Combobox(contenedor, values=["Masculino", "Femenino", "Otro"], width=37, state="readonly")
        self.txtCorreo = tk.Entry(contenedor, width=40)
        self.txtTelefono = tk.Entry(contenedor, width=40)
        self.txtDireccion = tk.Entry(contenedor, width=40)

        for label, widget in [("Nombre Completo:", self.txtNombre),
                              ("Fecha de Nacimiento:", self.txtNacimiento),
                              ("DNI o Carnet de Extranjería:", self.txtDNI),
                              ("Género:", self.comboGenero),
                              ("Correo Electrónico:", self.txtCorreo),
                              ("Número de Teléfono:", self.txtTelefono),
                              ("Dirección:", self.txtDireccion)]:
            tk.Label(contenedor, text=label, font=("Arial", 10)).pack()
            widget.pack(pady=2)

        tk.Label(contenedor, text="Seleccione sus Preferencias de Películas:", font=("Arial", 12)).pack(pady=10)
        framePreferencias = tk.Frame(contenedor)
        framePreferencias.pack(pady=5)

        col1 = tk.Frame(framePreferencias)
        col1.pack(side="left", padx=20)
        col2 = tk.Frame(framePreferencias)
        col2.pack(side="right", padx=20)

        self.prefVars = {}
        generos = ["Acción", "Comedia", "Terror", "Animación", "Romance", "Drama", "Documental", "Ciencia Ficción"]
        for i, genero in enumerate(generos):
            var = tk.IntVar()
            self.prefVars[genero] = var
            target_col = col1 if i < 4 else col2
            tk.Checkbutton(target_col, text=genero, variable=var, anchor="w").pack(anchor="w", pady=2)

        tk.Label(contenedor, text="Ingrese sus Datos de Cuenta:", font=("Arial", 12)).pack(pady=10)
        self.txtUsuario = tk.Entry(contenedor, width=40)
        self.txtClave = tk.Entry(contenedor, show="*", width=40)
        self.txtConfirmar = tk.Entry(contenedor, show="*", width=40)

        for label, widget in [("Nombre de Usuario:", self.txtUsuario),
                              ("Contraseña:", self.txtClave),
                              ("Confirmar Contraseña:", self.txtConfirmar)]:
            tk.Label(contenedor, text=label, font=("Arial", 10)).pack()
            widget.pack(pady=2)

        self.checkTerminos = tk.IntVar()
        self.checkMarketing = tk.IntVar()
        self.checkPromociones = tk.IntVar()

        tk.Checkbutton(contenedor, text="Acepto los Términos y Condiciones [Obligatorio]", variable=self.checkTerminos).pack(anchor="w", padx=20)
        tk.Checkbutton(contenedor, text="Autorizo el uso de mis datos para fines de marketing", variable=self.checkMarketing).pack(anchor="w", padx=20)
        tk.Checkbutton(contenedor, text="Acepto recibir promociones y novedades por correo o SMS", variable=self.checkPromociones).pack(anchor="w", padx=20)

        tk.Button(contenedor, text="Registrarme", command=self.registrar, width=25).pack(pady=15)

    def registrar(self):
        if not self.checkTerminos.get():
            messagebox.showwarning("Error", "Debes aceptar los términos y condiciones")
            return
        if self.txtClave.get() != self.txtConfirmar.get():
            messagebox.showwarning("Error", "Las contraseñas no coinciden")
            return
        nombre = self.txtNombre.get()
        messagebox.showinfo("Registro Exitoso", f"¡Bienvenido al Club Cineplanet, {nombre}!")

# -------------------- EJECUCIÓN --------------------
if __name__ == "__main__":
    Login().mainloop()
