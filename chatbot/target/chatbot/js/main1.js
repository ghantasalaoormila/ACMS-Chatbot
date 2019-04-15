/* 
 _____   _           _         _                        _                  
|_   _| | |         | |       | |                      | |                 
  | |   | |__   __ _| |_ ___  | |_ ___  _ __ ___   __ _| |_ ___   ___  ___ 
  | |   | '_ \ / _` | __/ _ \ | __/ _ \| '_ ` _ \ / _` | __/ _ \ / _ \/ __|
 _| |_  | | | | (_| | ||  __/ | || (_) | | | | | | (_| | || (_) |  __/\__ \
 \___/  |_| |_|\__,_|\__\___|  \__\___/|_| |_| |_|\__,_|\__\___/ \___||___/

Oh nice, welcome to the js file of dreams.
Enjoy responsibly!
@ihatetomatoes

*/
$("#loader-wrapper").css("display","none");
	/*  cookie */
	 var status = '';
		if (document.cookie && document.cookie.indexOf('ExpirationCookieTest=1') != -1) {
			status = 'Cookie is present';
			$("#loader-wrapper").css("display","none");
		} else {
			debugger;
			$("#loader-wrapper").css("display","block");
			status = 'Cookie is NOT present. It may be expired, or never set';
			setTimeout(function(){
				$('body').addClass('loaded');
				
			}, 4000);
			setCookie();
		}
		console.log(status);

	function setCookie() {
		var secs = 600; /*10 minutes */
		var now = new Date();
		var exp = new Date(now.getTime() + secs*1000);
		var status = '';
		document.cookie = 'ExpirationCookieTest=1; expires='+exp.toUTCString();
		if (document.cookie && document.cookie.indexOf('ExpirationCookieTest=1') != -1) {
			status = 'Cookie successfully set. Expiration in '+secs+' seconds';
		} else {
			status = 'Cookie NOT set. Please make sure your browser is accepting cookies';
		}
		console.log(status)
    }
   

$(document).ready(function() {
	
	

	
	
});

