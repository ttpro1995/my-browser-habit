// ==UserScript==
// @name     fetch-url
// @version  1
// @include  *
// @grant    none
// ==/UserScript==

// SET URL to web-server HERE
// var yourUrl= "http://127.0.0.1:6789/log-url";
var yourUrl= "https://my-personal-seedbox.de.r.appspot.com/log-url";


// sample data
// {"timestamp":1602941379,"url":"https://stackoverflow.com/questions/10434599/get-the-data-received-in-a-flask-request"}
var data = {"timestamp": Math.floor(Date.now() / 1000),"url":window.location.href};

var xhr = new XMLHttpRequest();
xhr.open("POST", yourUrl, true);
xhr.setRequestHeader('Content-Type', 'application/json');
xhr.send(JSON.stringify(data));
console.log("sent " + JSON.stringify(data));
