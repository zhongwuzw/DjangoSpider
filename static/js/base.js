jQuery(function(){
	setInterval("update()",100000);
	setInterval("startCrawler()",60000);
	$('#byr_link').mouseover(function(){
		$('#qing_hua_link').removeClass('active');
		$('#byr_link').addClass('active');
	});
	$('#byr_link').mouseout(function(){
		$('#byr_link').removeClass('active');
	});
	$('#qing_hua_link').mouseout(function(){
		$('#qing_hua_link').removeClass('active');
	});
	
	$('#qing_hua_link').mouseover(function(){
		$('#byr_link').removeClass('active');
		$('#qing_hua_link').addClass('active');
	});
	}
);

function update(){
	most_recent = $('#update-holder').find('div:first');
	var temp_most_recent = most_recent.attr('id');
	if(temp_most_recent === undefined)
	{
		temp_most_recent = 0;
	}
	$.getJSON('/get/updates/' + temp_most_recent + '/', 
		function(data) {
		cycle_class = most_recent.hasClass("odd") ? "even" : "odd";
		jQuery.each(data, function() {
			$('#update-holder').prepend('<div id="' + this.fields.job_id + 
                    '" class="col-md-6 ' + cycle_class + '"><a href="' + this.pk + 
                    '" target="view_window">' + this.fields.text + '</a></div>');
			cycle_class = (cycle_class == "odd") ? "even" : "odd";
		});
	});
}

function startCrawler(){
	$.get('/start/crawler/');
}