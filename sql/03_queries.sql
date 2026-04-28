-- 1. Общая статистика
SELECT
    (SELECT COUNT(*) FROM rooms) AS total_rooms,
    (SELECT COUNT(*) FROM guests) AS total_guests,
    (SELECT COUNT(*) FROM bookings) AS total_bookings,
    (SELECT COALESCE(SUM(amount), 0) FROM payments) AS total_payments;

-- 2. Список номеров с типами
SELECT r.id, r.room_number, rt.name AS room_type, r.floor, r.status
FROM rooms r
JOIN room_types rt ON rt.id = r.room_type_id
ORDER BY r.room_number;

-- 3. Список гостей
SELECT id, first_name, last_name, phone, email, passport_number
FROM guests
ORDER BY id DESC;

-- 4. Бронирования с данными гостя и номера
SELECT
    b.id,
    g.first_name || ' ' || g.last_name AS guest,
    r.room_number,
    b.check_in_date,
    b.check_out_date,
    b.status,
    b.total_price
FROM bookings b
JOIN guests g ON g.id = b.guest_id
JOIN rooms r ON r.id = b.room_id
ORDER BY b.id DESC;

-- 5. Активные услуги
SELECT id, name, price
FROM services
WHERE is_active = 1
ORDER BY name;

-- 6. Платежи
SELECT p.id, p.booking_id, p.amount, p.method, p.paid_at
FROM payments p
ORDER BY p.paid_at DESC;
