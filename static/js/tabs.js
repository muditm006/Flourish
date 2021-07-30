function openPage(pageName,elmnt,color) {
	  var i, tabcontent, tablinks;
	  tabcontent = document.getElementsByClassName("tabcontent");
	  for (i = 0; i < tabcontent.length; i++) {
		tabcontent[i].style.display = "none";
	  }
	  tablinks = document.getElementsByClassName("tablink");
	  for (i = 0; i < tablinks.length; i++) {
		tablinks[i].style.backgroundColor = "";
	  }
	  document.getElementById(pageName).style.display = "block";
	  elmnt.style.backgroundColor = color;
	}

	// Get the element with id="defaultOpen" and click on it
	document.getElementById("defaultOpen").click();
	
function openCity(evt, cityName) {
		  var i, tabcontents, tablinkss;
		  tabcontents = document.getElementsByClassName("tabcontents");
		  for (i = 0; i < tabcontents.length; i++) {
			tabcontents[i].style.display = "none";
		  }
		  tablinkss = document.getElementsByClassName("tablinkss");
		  for (i = 0; i < tablinkss.length; i++) {
			tablinkss[i].className = tablinkss[i].className.replace(" active", "");
		  }
		  document.getElementById(cityName).style.display = "block";
		  evt.currentTarget.className += " active";
		}

		// Get the element with id="defaultOpen" and click on it
		document.getElementById("defaultsOpen").click();
		
