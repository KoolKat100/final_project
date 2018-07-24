function button1Function(section){
  if(document.getElementById(section).style.display=="none") {
    document.getElementById("button1").innerHTML="Hide Bio";
    document.getElementById(section).style.display="block";
  } else {
    document.getElementById("button3").innerHTML="Show Bio";
    document.getElementById(section).style.display="none";
  }
}
function button2Function(){
  if(document.getElementById(section).style.display=="none") {
    document.getElementById("show/hide").innerHTML="Hide Bio";
    document.getElementById(section).style.display="block";
  } else {
    document.getElementById("show/hide").innerHTML="Show Bio";
    document.getElementById(section).style.display="none";
  }
}
function button3Function(){
  if(document.getElementById(section).style.display=="none") {
    document.getElementById("show/hide").innerHTML="Hide Bio";
    document.getElementById(section).style.display="block";
  } else {
    document.getElementById("show/hide").innerHTML="Show Bio";
    document.getElementById(section).style.display="none";
  }
}
if(document.getElementById(section).style.display=="none") {
  document.getElementById("show/hide").innerHTML="Hide Bio";
  document.getElementById(section).style.display="block";
} else {
  document.getElementById("show/hide").innerHTML="Show Bio";
  document.getElementById(section).style.display="none";
}
}
