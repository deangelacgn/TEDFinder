$(function(){
  $(document).on('click', function (e) {
      $('[data-toggle="popover"],[data-original-title]').each(function () {
          //the 'is' for buttons that trigger popups
          //the 'has' for icons within a button that triggers a popup
          if (!$(this).is(e.target) && $(this).has(e.target).length === 0 && $('.popover').has(e.target).length === 0) {
              (($(this).popover('hide').data('bs.popover')||{}).inState||{}).click = false  // fix for BS 3.3.6
          }
      })
    })

    if ($.fn.popover.Constructor.VERSION == "3.3.7") {
      $('[data-toggle="popover"]').on("hidden.bs.popover", function() {
          $(this).data("bs.popover").inState.click = false
      })
    }

    $('#add-doc-btn').popover({
        html : true,
        title: "<center>Novo Documento</center>",
        content: function() {
          return $('#doc-form-container').html()
        }
    })
});
