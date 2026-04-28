document.addEventListener('DOMContentLoaded', () => {
    const bookingForm = document.getElementById('booking-form');
    if (!bookingForm) return;

    bookingForm.addEventListener('submit', (event) => {
        const checkIn = bookingForm.querySelector('input[name="check_in_date"]').value;
        const checkOut = bookingForm.querySelector('input[name="check_out_date"]').value;

        if (checkIn && checkOut && checkOut <= checkIn) {
            event.preventDefault();
            alert('Дата выезда должна быть позже даты заезда.');
        }
    });
});
