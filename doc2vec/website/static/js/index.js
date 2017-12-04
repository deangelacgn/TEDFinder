function createVideoHtml(video_url){
  url = video_url.replace("/www.", "/embed.")
  htmlToAppend = '<div style="max-width:600px">' +
    '<div style="position:relative;height:0;padding-bottom:56.25%">' +
      '<iframe src="'+url+'" width="600" height="337" style="position:absolute;left:0;top:0;width:100%;height:100%" frameborder="0" scrolling="no" allowfullscreen></iframe>' +
    '</div>' +
  '</div>';
  return htmlToAppend;
}

function showVideo(keys, title, videoHtml){
  $("#search-keys").text('"'+keys+'"');
  $("#video-title").text(title);
  $("#embed-video").html(video_html);
  $(".slider-content").css({top: "9%"});
  $("#presentation-header").slideUp(300);
  $("#video-container").slideDown(300);
}

function discardVideo(){
  $("#embed-video").html("");
  $(".slider-content").css({top: "20%"});
  $("#presentation-header").slideDown(300);
  $("#video-container").slideUp(300);
}

function openWait(){
  var wait = $('#wait-modal');
  wait.modal({backdrop: 'static', keyboard: false});
  $("#wait-modal").modal('show');
}
function closeWait(){
  $("#wait-modal").modal('hide');
}


function selectMinVideosClicked(event){
  event.preventDefault();
  numberOfVideos = $(this).data('video');
  $("#n-btn-select").html(numberOfVideos);
  $("select[name='min-videos']").val(numberOfVideos);
}

$(function(){
  $("#select-min-videos a").on('click', selectMinVideosClicked);

  // $("select[name='min-videos']").on('change', function(event){
  //   event.preventDefault();
  //   alert('here');
  //   selectMinVideosClicked(event);
  // });

  $("#search-form").submit(function(event){
    event.preventDefault();
    openWait();

    var input = $(this).find("input[name='keyword']"), btn = $(this).find("button[type='submit']");
    var keywords = input.val();

    input.blur();
    btn.attr('disabled', true);

    $.post('/pesquisa/', $(this).serialize(), function(result){
      if(result.video !== undefined){
        input.val("");
        video_html = createVideoHtml(result.video);
        showVideo(keywords, "Melhor palestra encontrada:", video_html);
      }else{
        bootbox.alert('Houve um erro ao processar sua pesquisa...')
      }
    }).always(function(){
      btn.attr('disabled', false);
      closeWait();
    });

    return false;
  });

  $("#close-video-btn").on('click', function(event){
    event.preventDefault();
    discardVideo();
  })
})
