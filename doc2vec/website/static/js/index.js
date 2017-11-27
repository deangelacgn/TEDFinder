function createVideoHtml(video_url){
  url = video_url.replace("/www.", "/embed.")
  htmlToAppend = '<div style="max-width:840px">' +
    '<div style="position:relative;height:0;padding-bottom:56.25%">' +
      '<iframe src="'+url+'" width="840" height="472" style="position:absolute;left:0;top:0;width:100%;height:100%" frameborder="0" scrolling="no" allowfullscreen></iframe>' +
    '</div>' +
  '</div>';
  return htmlToAppend;
}

function showVideo(title, videoHtml){
  $("#video-title").text(title);
  $("#embed-video").html(video_html);
  $(".slider-content").css({top: "2.5%"});
  $("#presentation-header").slideUp(300);
  $("#video-container").slideDown(300);
}

function discardVideo(){
  $("#embed-video").html("");
  $(".slider-content").css({top: "20%"});
  $("#presentation-header").slideDown(300);
  $("#video-container").slideUp(300);
}

$(function(){
  $("#search-form").submit(function(event){
    event.preventDefault();
    var input = $(this).find("input[name='keyword']"), btn = $(this).find("button[type='submit']");

    input.blur();
    btn.attr('disabled', true);

    $.post('/pesquisa/', $(this).serialize(), function(result){
      if(result.video !== undefined){
        video_html = createVideoHtml(result.video);
        showVideo("Meu vídeo", video_html);
      }else{
        bootbox.alert('Houve um erro ao processar sua pesquisa...')
      }
    }).always(function(){
      btn.attr('disabled', false);
    });

    return false;
  });

  $("#close-video-btn").on('click', function(event){
    event.preventDefault();
    discardVideo();
  })
})
