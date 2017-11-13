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
      $(".modal .btn-success").removeAttr("disabled");
      if(t==="timeout" || x.status==0) {
        this.tryCount++;
        if (this.tryCount<=this.retryLimit){
          $.ajax(this);
          return;
        }
        else{
        alert("Por favor, tente novamente!");
      }
      }
      else if(x.status==401){
        alert("Você não tem permissões para executar essa ação.<br> Se você acha que não deveria estar recebendo essa mensagem, entre em contato com o suporte!")
      }
    }
  });

  $('[data-toggle="tooltip"]').tooltip()

  // $("#logout-btn").on("click", function(event){
  //     event.preventDefault()
  //     let intro_text = "Parece que você quer sair do Connet <span class='fa fa-frown-o'></span>"
  //     let final_text = "Por favor confirme sua ação para prosseguir."
  //     bootbox.confirm({
  //       title: "<h4 class='modal-title' style='color:black;font-weight: bold;'>Atenção</h4>",
  //       message: "<div class='text-center'><p><span class='text-danger'>"+intro_text+"</span><br/>"+final_text+"</p></div>",
  //       className: "confirm-delete-modal",
  //       callback: function(confirmed){
  //         if(confirmed){
  //           window.location.replace("/logout")
  //         }
  //       }
  //     })
  // })
});
