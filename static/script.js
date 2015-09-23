if (url) {
	$('#title-form-msg').removeClass('vertical-center');
	$('#title-form-msg').addClass('padding-bottom', '10px');

	// loads url into iframe
	var iframe = document.getElementById("iframe");
	iframe.src = url;

	// wrap spans around each opening and closing tag with class [tagname]-tag
	var source_html = document.getElementById("source_code").innerHTML;
	source_html = source_html.replace(/&lt;(\/?)(\w+)(.*?)&gt;/g, "<span class=\$2-tag\>&lt;$1$2$3&gt;</span>");
	document.getElementById("source_code").innerHTML = source_html;

	var previousClassName = null;

	$('li').on({
		// adds or removes bold text for hover events
		mouseover: function(){
			$(this).addClass('hover');
		},
		mouseout: function(){
			$(this).removeClass('hover');
		},
		// toggles highlight class for tags with the same class name on click events
		click: function(){
			$(this).removeClass('hover');

			var className = '.' + this.className;

			if (className !== previousClassName) {
				$('#source_code').find(previousClassName).removeClass('highlight');
			}

			$('#source_code').find(className).toggleClass('highlight');
			previousClassName = className;

			$(this).addClass('hover');
		}
	});
} else {
	$('#main-wrapper').hide();
}

