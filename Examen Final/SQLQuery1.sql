-- Crear base de datos
CREATE DATABASE cine;
GO

USE cine;
GO

-- ===================== USUARIO =====================
CREATE TABLE Usuario (
    id_usuario INT PRIMARY KEY,
    codigo VARCHAR(50) UNIQUE,
    clave VARCHAR(50),
    rol VARCHAR(20) -- admin, trabajador, cliente
);

-- ===================== CLIENTE =====================
CREATE TABLE Cliente (
    id_cliente INT PRIMARY KEY,
    id_usuario INT,
    nombre VARCHAR(100),
    apellido VARCHAR(100),
    doc_identidad VARCHAR(20),
    tipo_cliente VARCHAR(10), -- 'Socio' o 'No Socio'
    fecha_nacimiento DATE,
    genero VARCHAR(10),
    correo VARCHAR(100),
    telefono VARCHAR(15),
    direccion VARCHAR(150),
    ciudad VARCHAR(50),
    fecha_registro DATE,
    puntos_acumulados INT,
    estado_membresia VARCHAR(20),
    fecha_vencimiento DATE,
    FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario)
);

-- ===================== TRABAJADOR =====================
CREATE TABLE Trabajador (
    id_trabajador INT PRIMARY KEY,
    id_usuario INT,
    nombre VARCHAR(100),
    apellido VARCHAR(100),
    doc_identidad VARCHAR(20),
    telefono VARCHAR(15),
    area_trabajo VARCHAR(20),
    FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario)
);

-- ===================== PELICULA =====================
CREATE TABLE Pelicula (
    id_pelicula INT PRIMARY KEY,
    titulo VARCHAR(100),
    genero VARCHAR(50),
    duracion INT,
    clasificacion VARCHAR(10),
    idioma VARCHAR(50),
    subtitulos BIT,
    formato VARCHAR(20),
    director VARCHAR(100),
    fecha_estreno DATE
);

-- ===================== FUNCION =====================
CREATE TABLE Funcion (
    id_funcion INT PRIMARY KEY,
    id_pelicula INT,
    horario DATETIME,
    precio DECIMAL(6,2),
    num_sala INT,
    FOREIGN KEY (id_pelicula) REFERENCES Pelicula(id_pelicula)
);

-- ===================== BOLETA =====================
CREATE TABLE Boleta (
    id_boleta INT PRIMARY KEY,
    id_cliente INT,
    id_trabajador INT,
    id_funcion INT,
    fecha_emision DATETIME,
    entradas INT,
    total DECIMAL(8,2),
    FOREIGN KEY (id_cliente) REFERENCES Cliente(id_cliente),
    FOREIGN KEY (id_trabajador) REFERENCES Trabajador(id_trabajador),
    FOREIGN KEY (id_funcion) REFERENCES Funcion(id_funcion)
);

-- ===================== PRODUCTO =====================
CREATE TABLE Producto (
    id_producto INT PRIMARY KEY,
    nombre VARCHAR(100),
    precio DECIMAL(6,2),
    marca VARCHAR(50)
);

-- ===================== VENTA CONFITERIA =====================
CREATE TABLE VentaConfiteria (
    id_venta INT PRIMARY KEY,
    id_trabajador INT,
    fecha DATETIME,
    total DECIMAL(8,2),
    FOREIGN KEY (id_trabajador) REFERENCES Trabajador(id_trabajador)
);

CREATE TABLE DetalleVentaConfiteria (
    id_detalle INT PRIMARY KEY,
    id_venta INT,
    id_producto INT,
    cantidad INT,
    subtotal DECIMAL(8,2),
    FOREIGN KEY (id_venta) REFERENCES VentaConfiteria(id_venta),
    FOREIGN KEY (id_producto) REFERENCES Producto(id_producto)
);

-- ===================== LIMPIEZA =====================
CREATE TABLE Limpieza (
    id_limpieza INT PRIMARY KEY,
    id_trabajador INT,
    sala VARCHAR(20),
    fecha DATE,
    estado VARCHAR(20),
    FOREIGN KEY (id_trabajador) REFERENCES Trabajador(id_trabajador)
);

-- ===================== DATOS =====================

-- USUARIO
INSERT INTO Usuario VALUES
(1, 'admin', '1234', 'admin'),
(2, 'marco', 'boleto123', 'trabajador'),
(3, 'sandra', 'confite456', 'trabajador'),
(4, 'patricia', 'limpieza789', 'trabajador'),
(5, 'lucia', 'cliente111', 'cliente'),
(6, 'carlos', 'cliente222', 'cliente');

-- CLIENTE
INSERT INTO Cliente VALUES
(1, 5, 'Lucía', 'Gómez', '12345678', 'Socio', '1990-05-12', 'Femenino', 'lucia@gmail.com', '987654321', 'Av. Lima 123', 'Lima', '2023-01-10', 120, 'Activo', '2025-01-10'),
(2, 6, 'Carlos', 'Mendoza', '23456789', 'Socio', '1985-08-22', 'Masculino', 'carlos@hotmail.com', '912345678', 'Jr. Arequipa 456', 'Lima', '2022-11-05', 80, 'Activo', '2024-11-05'),
(3, NULL, 'Ana', 'Torres', '34567890', 'Socio', '1992-03-30', 'Femenino', 'ana@gmail.com', '956789012', 'Calle Sol 789', 'Callao', '2023-06-15', 150, 'Activo', '2025-06-15'),
(4, NULL, 'Luis', 'Ramírez', '45678901', 'Socio', '1988-12-01', 'Masculino', 'luis@gmail.com', '934567890', 'Av. Mar 321', 'Lima', '2023-03-20', 60, 'Activo', '2024-03-20'),
(5, NULL, 'María', 'Fernández', '56789012', 'Socio', '1995-07-18', 'Femenino', 'maria@gmail.com', '945678901', 'Jr. Luna 654', 'Lima', '2023-09-01', 100, 'Activo', '2025-09-01'),
(6, NULL, 'Jorge', 'Paredes', '67890123', 'Socio', '1991-11-11', 'Masculino', 'jorge@gmail.com', '923456789', 'Calle Estrella 987', 'Callao', '2023-02-28', 90, 'Activo', '2025-02-28'),
(7, NULL, 'Elena', 'Rojas', '78901234', 'No Socio', '1993-04-25', 'Femenino', 'elena@gmail.com', '987123456', 'Av. Norte 111', 'Lima', NULL, NULL, NULL, NULL),
(8, NULL, 'Pedro', 'Salas', '89012345', 'No Socio', '1987-09-10', 'Masculino', 'pedro@gmail.com', '976543210', 'Jr. Sur 222', 'Lima', NULL, NULL, NULL, NULL);

-- TRABAJADOR
INSERT INTO Trabajador VALUES
(1, 2, 'Marco', 'García', '87654321', '987654321', 'Boletería'),
(2, 3, 'Sandra', 'Lopez', '76543210', '976543210', 'Confitería'),
(3, 4, 'Patricia', 'Reyes', '65432109', '954321098', 'Limpieza'),
(4, NULL, 'Raúl', 'Torres', '54321098', '943210987', 'Proyección'),
(5, NULL, 'Carmen', 'Delgado', '43210987', '932109876', 'Boletería'),
(6, NULL, 'Héctor', 'Morales', '32109876', '921098765', 'Confitería');

-- PELICULA
INSERT INTO Pelicula VALUES
(11, 'Deadpool and Wolverine', 'Acción / Comedia', 120, 'R', 'Inglés', 1, '2D', 'Shawn Levy', '2024-07-26'),
(12, 'Inside Out 2', 'Animación / Familiar', 100, 'PG', 'Español', 0, '2D', 'Kelsey Mann', '2024-06-20'),
(13, 'Dune: Parte Dos', 'Ciencia Ficción / Drama', 155, 'PG-13', 'Inglés', 1, '2D', 'Denis Villeneuve', '2024-03-01'),
(14, 'Barbie', 'Comedia / Fantasía', 120, 'PG-13', 'Español', 0, '2D', 'Greta Gerwig', '2023-07-20'),
(15, 'Kung Fu Panda 4', 'Acción / Comedia', 95, 'PG', 'Español', 0, '2D', 'Mike Mitchell', '2024-03-08'),
(16, 'Oppenheimer', 'Acción / Suspenso', 170, 'R', 'Inglés', 1, '2D', 'Christopher Nolan', '2023-05-09');