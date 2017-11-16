$(function(){
  var csrftoken = getCookie('csrftoken');

  $.ajaxSetup({
    tryCount: 0,
    retryLimit: 3,
    beforeSend: function(xhr, settings) {
      if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
        xhr.setRequestHeader("X-CSRFToken", csrftoken);
      }
    },
    error: function(x, t, m){
        bootbox.alert("Houve um erro ao executar esta ação. Status: " + x.status)
    }
  });

  $('[data-toggle="tooltip"]').tooltip()

  $("#logout-btn").on("click", function(event){
      event.preventDefault()
      let intro_text = "Tá cedo, fique mais um poquinho... <span class='fa fa-frown-o'></span>"
      let final_text = "Ou então vá simbora logo, você que sabe! <span class='fa fa-meh-o'></span>"
      bootbox.confirm({
        title: "<h4 class='modal-title' style='color:black;font-weight: bold;'>Tem certeza que deseja sair?</h4>",
        message: "<div class='text-center'><p><span class='text-danger'>"+intro_text+"</span><br/>"+final_text+"</p></div>",
        className: "confirm-delete-modal",
        callback: function(confirmed){
          if(confirmed){
            window.location.replace("/logout")
          }
        }
      })
  })
});
