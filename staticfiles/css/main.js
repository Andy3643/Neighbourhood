let i=0;
let images=[];
const TIME=3000;
images[0] ="./";
images[1] ="../static/images/five.jpg";
images[2] ="../static/images/five.jpg";
images[3] ="../static/images/five.jpg";
images[4] ="../static/images/five.jpg";


function slideshow(){

  document.querySelector('#display-photo').src= images[i];
  if(i<images.length-1){
    i++;
  }else{
    i=0;
  }

  setTimeout("slideshow()",TIME);
};

window.onload=slideshow();