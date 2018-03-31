function desempenho() {
   
    
    console.log("Entrou aqui nessa porra")
    var insc = $("#insc").val();
    var cd_periodo = $("#cd_periodo").val();;
    var url = "desempenho/";
    var postData = {
        "mat": insc,
        "cd_periodo": cd_periodo

    };

    $.post(url, postData, function (data, status) {
        console.log("Entrou aqui nessa porra")
        if (status == "success") {
            $("#desempenho").html(data);
        } else {
            $("#desempenho").html('<div class="alert alert-danger" ><h3>Ainda nao foi Realizado correção do academico!</h3></div>');
        }
    });
}