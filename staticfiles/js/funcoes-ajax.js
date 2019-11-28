function utilizouHoraExtra(id){
        alert('foi');
		console.log(id);
		token = document.getElementsByName("csrfmiddlewaretoken")[0].value;
		$.ajax({
				type:'POST',
				url: '/horas-extras/utilizou_hora-extra/' + id + '/',
				data: {
						csrfmiddlewaretoken: token

				},
				success: function(result){
					console.log(result);
					$("#mensagem").text('result.mensagem');
					$("#horas_atualizadas").text(result.horas);

				}

		});

}
