$(document).ready(function(){
    $('#sort-newest').on('click', function(){
        $('#writeup-search-form').attr("action", "/writeups/listWriteups/newest/");
        $('#writeup-search-form').submit();
    });

    $('#sort-oldest').on('click', function(){
        $('#writeup-search-form').attr("action", "/writeups/listWriteups/oldest/");
        $('#writeup-search-form').submit();
    });
});
