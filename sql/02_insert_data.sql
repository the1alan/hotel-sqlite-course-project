INSERT INTO room_types (name, description, base_price, capacity) VALUES
('Standard', 'Базовый номер с одной кроватью', 2800, 2),
('Deluxe', 'Улучшенный номер с видом на город', 4500, 3),
('Suite', 'Просторный двухкомнатный номер', 7500, 4);

INSERT INTO rooms (room_number, room_type_id, floor, status) VALUES
('101', 1, 1, 'available'),
('102', 1, 1, 'occupied'),
('201', 2, 2, 'available'),
('202', 2, 2, 'maintenance'),
('301', 3, 3, 'occupied');

INSERT INTO guests (first_name, last_name, phone, email, passport_number) VALUES
('Иван', 'Петров', '+79990000001', 'ivan.petrov@mail.com', '4001 123456'),
('Анна', 'Смирнова', '+79990000002', 'anna.smirnova@mail.com', '4002 654321'),
('Дмитрий', 'Ильин', '+79990000003', 'd.ilyin@mail.com', '4003 777777');

INSERT INTO employees (full_name, role, hire_date, salary) VALUES
('Мария Орлова', 'manager', '2023-04-10', 65000),
('Олег Руднев', 'receptionist', '2024-02-15', 50000),
('Светлана Власова', 'accountant', '2022-09-01', 70000);

INSERT INTO bookings (guest_id, room_id, employee_id, check_in_date, check_out_date, status, total_price) VALUES
(1, 2, 2, '2026-04-25', '2026-04-30', 'checked_in', 14000),
(2, 3, 1, '2026-05-01', '2026-05-04', 'confirmed', 13500),
(3, 5, 2, '2026-04-20', '2026-04-24', 'completed', 30000);

INSERT INTO services (name, price, is_active) VALUES
('Завтрак', 600, 1),
('Трансфер', 1500, 1),
('Прачечная', 400, 1),
('SPA', 2500, 0);

INSERT INTO booking_services (booking_id, service_id, quantity, unit_price) VALUES
(1, 1, 2, 600),
(1, 2, 1, 1500),
(2, 1, 3, 600),
(3, 3, 2, 400);

INSERT INTO payments (booking_id, amount, method, paid_at) VALUES
(1, 8000, 'card', '2026-04-26 10:30:00'),
(2, 5000, 'transfer', '2026-04-28 09:00:00'),
(3, 30800, 'cash', '2026-04-24 12:15:00');
