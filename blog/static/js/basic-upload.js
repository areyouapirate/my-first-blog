$(function () {

  /* SCRIPT TO OPEN THE MODAL WITH THE PREVIEW */
  $("#id_img").change(function () {
    if (this.files && this.files[0]) {
      var reader = new FileReader();
      reader.onload = function (e) {
        $("#image").attr("src", e.target.result);
        $("#modalCrop").modal("show");
      }
      reader.readAsDataURL(this.files[0]);
    }
  });


  /* SCRIPTS TO HANDLE THE CROPPER BOX */
  var $image = $("#image");
  var cropBoxData;
  var canvasData;
  $("#modalCrop").on("shown.bs.modal", function () {
    $image.cropper({
      viewMode: 1,
      aspectRatio: 22/10,
      minCropBoxWidth: 1700,
      minCropBoxHeight: 760,
      ready: function () {
        $image.cropper("setCanvasData", canvasData);
        $image.cropper("setCropBoxData", cropBoxData);
      }
    });
  }).on("hidden.bs.modal", function () {
    cropBoxData = $image.cropper("getCropBoxData");
    canvasData = $image.cropper("getCanvasData");
    $image.cropper("destroy");
  });

  $(".js-zoom-in").click(function () {
    $image.cropper("zoom", 0.1);
  });

  $(".js-zoom-out").click(function () {
    $image.cropper("zoom", -0.1);
  });

  /* SCRIPT TO COLLECT THE DATA AND POST TO THE SERVER */
  $(".js-crop-and-upload").click(function () {
    var cropData = $image.cropper("getData");
    $("#id_x").val(cropData["x"]);
    $("#id_y").val(cropData["y"]);
    $("#id_height").val(cropData["height"]);
    $("#id_width").val(cropData["width"]);
  });

});



/*

$(function () {

  $(".js-upload-photos").click(function () {
    $("#fileupload").click();
  });

  $("#fileupload").fileupload({
    dataType: 'json',
    sequentialUploads: true, 
    start: function (e) {  
      $("#modal-progress").modal("show");
    },
    stop: function (e) {  
      $("#modal-progress").modal("hide");
    },
    progressall: function (e, data) {  
      var progress = parseInt(data.loaded / data.total * 100, 10);
      var strProgress = progress + "%";
      $(".progress-bar").css({"width": strProgress});
      $(".progress-bar").text(strProgress);
    },
    done: function (e, data) {
      if (data.result.is_valid) {
        $("#gallery tbody").prepend(
          "<tr><td><a href='" + data.result.url + "'>" + data.result.name + "</a></td></tr>"
        )
      }
    }

  });

});

*/