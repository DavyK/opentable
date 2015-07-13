$(document).ready(function(){
    $('#reverse-page-order').on('click', function(){
        var writeups = $('#to-be-sorted').children().get().reverse();
        for(var i = 0; i < writeups.length; i++){
            writeups[i].parentNode.appendChild(writeups[i])
        }
    });
    $('#id_date_added').datetimepicker();

});
