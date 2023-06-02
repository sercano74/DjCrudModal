/* ------------------------------------------------------------------------- */
//                      SCRIPT EXTENDED TO ALL PAGES
/* ------------------------------------------------------------------------- */

// 1) Script to confirm save changes (if it exist)
$(document).ready(function() {
    $("#btn-back").click(function() {
        var name=$("#name").val();
        var purchase=$("#purchase").val();
        var sale=$("#sale").val();
        var qty=$("#qty").val();
        var gender=$("#gender").val();
        var note=$("#note").val();

        //Hidden inputs
        var name2=$("#name2").val();
        var purchase2=$("#purchase2").val();
        var sale2=$("#sale2").val();
        var qty2=$("#qty2").val();
        var gender2=$("#gender2").val();
        var note2=$("#note2").val();
        // Button to call the modal
        if ( (name != name2) || (purchase != purchase2) || (sale != sale2) || (qty != qty2) || (gender != gender2) || (note != note2) ) {
            $("#modal-confirm").trigger("click");
            return false;

        }
    })
})


// 2) Disabled button statement
$("#name, #name2").on("keyup", function (){
    $(".btn-action").prop("disabled", true);
    if ( ($("#name").val()) != ($("#name2").val()) ) {
        $(".btn-action").prop("disabled", false);
    }
});

$("#purchase, #purchase2").on("keyup", function (){
    $(".btn-action").prop("disabled", false);
    if ( ($("#purchase").val()) == ($("#purchase2").val()) ) {
        $(".btn-action").prop("disabled", true);
    }
});

$("#sale, #sale2").on("keyup", function (){
    $(".btn-action").prop("disabled", false);
    if ( ($("#sale").val()) == ($("#sale2").val()) ) {
        $(".btn-action").prop("disabled", true);
    }
});

$("#qty, #qty2").on("keyup", function (){
    $(".btn-action").prop("disabled", false);
    if ( ($("#qty").val()) == ($("#qty2").val()) ) {
        $(".btn-action").prop("disabled", true);
    }
});

$("#note, #note2").on("keyup", function (){
    $(".btn-action").prop("disabled", false);
    if ( ($("#note").val()) == ($("#note2").val()) ) {
        $(".btn-action").prop("disabled", true);
    }
});

// 3) SELECT OPTION
$(document).ready(function () {
    $(".btn-action").prop("disabled", true);
    $("#gender,#gender2").change(function () {
        if ( ($("#gender").val()) == ($("#gender2").val())) {
            $(".btn-action").attr("disabled","disabled");
        }
        else{
            $(".btn-action").removeAttr("disabled");
        }
    })
});

