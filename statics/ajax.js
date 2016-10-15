var object = document.getElementById('download');
object.onclick = function(){
	handleClick();
}

function handleClick(){
	xttp = new XMLHttpRequest();
	// if (xttp.readyState == 4 && xttp.status == 200) {
 //    	alert(xttp.responseText);
 //  	}
	xttp.open("GET","/download/ajax/15/",true);
	xttp.send();
}