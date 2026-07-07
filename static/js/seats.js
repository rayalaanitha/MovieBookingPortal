const seatContainer = document.getElementById("seat-container");

let selectedSeats = [];
const ticketPrice = 12;

for (let row = 65; row <= 69; row++) {

    const rowDiv = document.createElement("div");
    rowDiv.className = "mb-2";

    for (let col = 1; col <= 8; col++) {

        const seat = document.createElement("button");

        seat.type = "button";
        seat.className = "btn btn-outline-secondary m-1";
        seat.textContent = String.fromCharCode(row) + col;

        // Already booked seats
        if (bookedSeats.includes(seat.textContent)) {
            seat.classList.remove("btn-outline-secondary");
            seat.classList.add("btn-danger");
            seat.disabled = true;
        }

        seat.addEventListener("click", function () {

            if (seat.disabled) return;

            if (seat.classList.contains("btn-success")) {

                seat.classList.remove("btn-success");
                seat.classList.add("btn-outline-secondary");

                selectedSeats = selectedSeats.filter(
                    s => s !== seat.textContent
                );

            } else {

                seat.classList.remove("btn-outline-secondary");
                seat.classList.add("btn-success");

                selectedSeats.push(seat.textContent);
            }

            document.getElementById("selectedSeats").textContent =
                selectedSeats.length ? selectedSeats.join(", ") : "None";

            document.getElementById("price").textContent =
                selectedSeats.length * ticketPrice;

            document.getElementById("seat_numbers").value =
                selectedSeats.join(",");

            document.getElementById("total_paid").value =
                selectedSeats.length * ticketPrice;
        });

        rowDiv.appendChild(seat);
    }

    seatContainer.appendChild(rowDiv);
}