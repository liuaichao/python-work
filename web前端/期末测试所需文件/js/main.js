/**
 * Created by Administrator on 16-6-23.
 */
window.onload = function () {
    var oDt = new Date();
    var sWd = "";
    var iWeekDay = oDt.getDay();
    switch (iWeekDay) {
        case 0:
            sWd = "Sunday";
            break;
        case 1:
            sWd = "Monday";
            break;
        case 2:
            sWd = "Tuesday";
            break;
        case 3:
            sWd = "Wednesday";
            break;
        case 4:
            sWd = "Thursday";
            break;
        case 5:
            sWd = "Friday";
            break;
        case 6:
            sWd = "Saturday";
            break;
    }
    var iMonth = parseInt(oDt.getMonth()) + 1;
    document.getElementById("displaydate").innerHTML = "<span>" + oDt.getFullYear() + "-" + iMonth + "-" + oDt.getDate() + " " + sWd + "</span>";
    var iTimerid = window.setInterval("showtime()", 1000);

    if (document.getElementById("a1") != null) {
        document.getElementById("a1").onmouseover = function () {
            document.getElementById("badimg").src = "images/b-ad1.jpg";
        }
    }
    if (document.getElementById("a2") != null) {
        document.getElementById("a2").onmouseover = function () {
            document.getElementById("badimg").src = "images/b-ad2.jpg";
        }
    }
    if (document.getElementById("a3") != null) {
        document.getElementById("a3").onmouseover = function () {
            document.getElementById("badimg").src = "images/b-ad3.jpg";
        }
    }
    if (document.getElementById("a4") != null) {
        document.getElementById("a4").onmouseover = function () {
            document.getElementById("badimg").src = "images/b-ad4.jpg";
        }
    }

}
function showtime() {
    var oDt = new Date();
    var iTimerid;
    var sTime = "";
    if (oDt.getHours() < 10) {
        sTime += "0" + oDt.getHours() + ":";
    }
    else {
        sTime += oDt.getHours() + ":";
    }
    if (oDt.getMinutes() < 10) {
        sTime += "0" + oDt.getMinutes() + ":";
    }
    else {
        sTime += oDt.getMinutes() + ":";
    }
    if (oDt.getSeconds() < 10) {
        sTime += "0" + oDt.getSeconds();
    }
    else {
        sTime += oDt.getSeconds();
    }
    document.getElementById("displaytime").innerHTML = "<span>" + sTime + "</span>";
}

