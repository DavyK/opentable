$(document).ready(function(){
    $('#sort-newest').on('click', function(){
        $('#writeup-search-form').attr("action", "/writeups/listWriteups/");
        $('#writeup-search-form').submit();
    });

    $('#sort-oldest').on('click', function(){
        $('#writeup-search-form').attr("action", "/writeups/listWriteups/");
        $('#writeup-search-form').submit();
    });
    $('#reverse-page-order').on('click', function(){
        var writeups = $('#to-be-sorted').children().get().reverse();
        for(var i = 0; i < writeups.length; i++){
            writeups[i].parentNode.appendChild(writeups[i])
        }
    })
});
