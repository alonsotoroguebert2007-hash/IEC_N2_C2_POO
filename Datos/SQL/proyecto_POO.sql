-- Crear la base de datos 
CREATE DATABASE app_tienda;

-- Crear las tablas correspondientes a las entidades

CREATE TABLE Tienda (
    id_tienda INT PRIMARY KEY AUTO_INCREMENT,
    nombre CHAR(50) NOT NULL,
    correo CHAR(100) NOT NULL, 
    telefono INT NOT NULL,
    horario_atencion DATETIME NOT NULL,
    estado CHAR(20)
); 

CREATE TABLE Usuario (
    id_usuario INT PRIMARY KEY AUTO_INCREMENT,
    nombre CHAR(50) NOT NULL,
    correo CHAR(100), 
    telefono INT,
    contrasena VARCHAR(200) NOT NULL,
    fecha_nac DATE,
    rut INT NOT NULL 
); 

CREATE TABLE Pedido (
    id_pedido INT PRIMARY KEY AUTO_INCREMENT,
    fecha DATE DEFAULT (CURRENT_DATE),
    estado VARCHAR(30) NOT NULL DEFAULT 'Creando',
    id_tienda INT,
    id_usuario INT,
    
    FOREIGN KEY (id_tienda) REFERENCES Tienda(id_tienda),
    FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario)
);

CREATE TABLE Detalle_pedido (
    id_detalle INT PRIMARY KEY AUTO_INCREMENT,
    cantidad INT,
    precio_unitario INT, 
    sub_total INT,
    id_pedido INT,
    id_producto INT,

    FOREIGN KEY (id_producto) REFERENCES Producto(id_producto),
    FOREIGN KEY (id_pedido) REFERENCES Pedido(id_pedido)
); 

CREATE TABLE Producto (
    id_producto INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(200),
    stock INT, 
    precio INT,
    categoria VARCHAR(250),
    descripcion VARCHAR(255),
    imagen VARCHAR(255),
    id_tienda INT,
    
    FOREIGN KEY (id_tienda) REFERENCES Tienda(id_tienda)
); 

CREATE TABLE Pago (
    id_pago INT PRIMARY KEY AUTO_INCREMENT,
    fecha DATETIME DEFAULT (CURRENT_DATE),
    estado TEXT, 
    monto INT,
    metodo_pago CHAR(10), 
    id_pedido INT,

    FOREIGN KEY (id_pedido) REFERENCES Pedido(id_pedido)
); 

CREATE TABLE Direccion (
    id_direccion INT PRIMARY KEY AUTO_INCREMENT,
    calle CHAR(20),
    pais VARCHAR(100), 
    num_postal INT,
    ciudad VARCHAR(100),
    region VARCHAR(100),
    id_usuario INT,
    
    FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario)
); 

CREATE TABLE Envio (
    id_envio INT PRIMARY KEY AUTO_INCREMENT,
    costo INT NOT NULL,
    estado TEXT, 
    num_seguimiento INT NOT NULL,
    fecha_envio DATETIME DEFAULT (CURRENT_DATE),
    fecha_entrega DATETIME DEFAULT (CURRENT_DATE),
    transporte CHAR(15),
    id_pedido INT,
    id_direccion INT,

    FOREIGN KEY (id_pedido) REFERENCES Pedido(id_pedido),
    FOREIGN KEY (id_direccion) REFERENCES Direccion(id_direccion)
); 