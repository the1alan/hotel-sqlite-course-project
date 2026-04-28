import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
DB_PATH = "database.db"


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


@app.route("/", methods=["GET", "POST"])
def index():
    conn = get_connection()

    if request.method == "POST":
        form_type = request.form.get("form_type")

        if form_type == "guest":
            conn.execute(
                """
                INSERT INTO guests (first_name, last_name, phone, email, passport_number)
                VALUES (?, ?, ?, ?, ?)
                """,
                (
                    request.form["first_name"],
                    request.form["last_name"],
                    request.form["phone"],
                    request.form.get("email") or None,
                    request.form["passport_number"],
                ),
            )
            conn.commit()
            conn.close()
            return redirect(url_for("index"))

        if form_type == "booking":
            conn.execute(
                """
                INSERT INTO bookings (guest_id, room_id, employee_id, check_in_date, check_out_date, status, total_price)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    request.form["guest_id"],
                    request.form["room_id"],
                    None,
                    request.form["check_in_date"],
                    request.form["check_out_date"],
                    "confirmed",
                    request.form["total_price"],
                ),
            )
            conn.commit()
            conn.close()
            return redirect(url_for("index"))

    stats = conn.execute(
        """
        SELECT
            (SELECT COUNT(*) FROM rooms) AS total_rooms,
            (SELECT COUNT(*) FROM guests) AS total_guests,
            (SELECT COUNT(*) FROM bookings) AS total_bookings,
            (SELECT COALESCE(SUM(amount), 0) FROM payments) AS total_payments
        """
    ).fetchone()

    rooms = conn.execute(
        """
        SELECT r.id, r.room_number, rt.name AS room_type, r.floor, r.status
        FROM rooms r
        JOIN room_types rt ON rt.id = r.room_type_id
        ORDER BY r.room_number
        """
    ).fetchall()

    guests = conn.execute(
        """
        SELECT id, first_name, last_name, phone, email, passport_number
        FROM guests
        ORDER BY id DESC
        """
    ).fetchall()

    bookings = conn.execute(
        """
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
        ORDER BY b.id DESC
        """
    ).fetchall()

    services = conn.execute(
        """
        SELECT id, name, price, is_active
        FROM services
        ORDER BY id
        """
    ).fetchall()

    payments = conn.execute(
        """
        SELECT p.id, p.booking_id, p.amount, p.method, p.paid_at
        FROM payments p
        ORDER BY p.paid_at DESC
        """
    ).fetchall()

    room_choices = conn.execute(
        "SELECT id, room_number FROM rooms WHERE status != 'maintenance' ORDER BY room_number"
    ).fetchall()

    conn.close()

    return render_template(
        "index.html",
        stats=stats,
        rooms=rooms,
        guests=guests,
        bookings=bookings,
        services=services,
        payments=payments,
        room_choices=room_choices,
    )


if __name__ == "__main__":
    app.run(debug=True)
