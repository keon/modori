  // $('.carousel').carousel({
  //   interval: 3500
  // })

  // 


$(function(){
	$('button#send').bind('click', function(){


		var data = {
			"text":$('textarea[name="text"]').val()
		}
		console.log(data);

		$.ajax({
			type:"POST",
			url:"/api/pos",
			dataType:'json',
			encode:true,
			data:JSON.stringify(data),
                        contentType:"application/json"

		})
		.done(function(data){
			$('#result').text(data);
			console.log(data);
		})
		.fail(function(data){
			$('#result').html('<p>An error has occured</p>');
			console.log(data);
		});

	});
})
