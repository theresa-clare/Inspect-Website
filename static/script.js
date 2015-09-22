if (url) {
	// loads url into iframe
	var iframe = document.getElementById("iframe");
	iframe.src = url;

	// wrap spans around each opening and closing tag with class [tagname]-tag
	var source_html = document.getElementById("source_code").innerHTML;
	source_html = source_html.replace(/&lt;(\/?)(\S+)(.*?)&gt;/g, "<span class=\$2-tag\>&lt;$1$2$3&gt;</span>");
	document.getElementById("source_code").innerHTML = source_html;
}

