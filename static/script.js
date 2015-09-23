if (url) {
	// loads url into iframe
	var iframe = document.getElementById("iframe");
	iframe.src = url;

	// wrap spans around each opening and closing tag with class [tagname]-tag
	var source_html = document.getElementById("source_code").innerHTML;
	source_html = source_html.replace(/&lt;(\/?)(\w+)(.*?)&gt;/g, "<span class=\$2-tag\>&lt;$1$2$3&gt;</span>");
	document.getElementById("source_code").innerHTML = source_html;

	var previousClassName = null;

	// toggles highlight class for tags with the same class name on click events
	$('li').click(function(){
		var className = '.' + this.className;

		if (className !== previousClassName) {
			$('#source_code').find(previousClassName).removeClass('highlight');
		}

		$('#source_code').find(className).toggleClass('highlight');
		previousClassName = className;
	});
} else {
	$('#main-wrapper').hide();
}

