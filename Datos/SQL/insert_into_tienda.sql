INSERT INTO Tienda (nombre, correo, telefono, horario_atencion, estado)
VALUES
('Tienda Gamer', 'contacto@tiendagamer.cl', 987654321, '2026-10-18 09:00:00', 'Activa'),
('Tech Store', 'ventas@techstore.cl', 912345678, '2026-10-18 10:00:00', 'Activa'),
('Mundo PC', 'contacto@mundopc.cl', 998765432, '2026-10-18 08:30:00', 'Inactiva'),
('Cyber Shop', 'ventas@cybershop.cl', 976543210, '2026-10-18 11:00:00', 'Activa'),
('Digital Zone', 'info@digitalzone.cl', 965432187, '2026-10-18 09:30:00', 'Activa');

ALTER TABLE tienda
ADD COLUMN habilitado BOOLEAN NOT NULL DEFAULT TRUE;