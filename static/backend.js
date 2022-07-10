

$(document).ready(function(){
    $(document).on('click', '.summary-btn', function() {
        const selectedSeats = document.querySelectorAll(".row .seat.selected");
        var screening_date = document.querySelector('.screening_date')

        var seatList = [];

        let valuesSeats = Object.values(selectedSeats);

        for (let value of valuesSeats) {
            seatList.push(value.id);
            }

        $.ajax({
            url: "/order-summary",
            data: {
                'seat_list' : seatList,
                'screening_date': screening_date.id
            },
            success: function(response){
               $("body").html(response);
            }
        });
    });
});

$(document).ready(function(){
    $(document).on('click', '.order-seats', function() {
        const selectedSeats = document.querySelectorAll(".selected-seat");
        var screening_date = document.querySelector('.screening_date')

        var seatList = [];

        let valuesSeats = Object.values(selectedSeats);

        for (let value of valuesSeats) {
            seatList.push(value.id);
            }

        $.ajax({
            url: "/order-complete",
            data: {
                'seat_list' : seatList,
                'screening_date': screening_date.id
            },
            success: function(response){
               $("body").html(response);
            }
        });
    });
});

