var xmlhttp;
        xmlhttp = new XMLHttpRequest();

        function forward() {
            xmlhttp.open("GET", "cgi-bin/forward.py", true);
            xmlhttp.send();
        }

        function stop() {
            xmlhttp.open("GET", "cgi-bin/stop.py", true);
            xmlhttp.send();
        }

        function left() {
            xmlhttp.open("GET", "cgi-bin/left.py", true);
            xmlhttp.send();
        }

        function right() {
            xmlhttp.open("GET", "cgi-bin/right.py", true);
            xmlhttp.send();
        }

        function reverse() {
            xmlhttp.open("GET", "cgi-bin/reverse.py", true);
            xmlhttp.send();
        }

        function finishedATMO(){
            alert("FINISHED ATMO\nPlease leave this window open until you have been given the next link");
        }

        function finishedGMO(){
            alert("FINISHED GMO\nPlease leave this window upen until you have been given the next link");
        }
/*  These functions are not currently in use
        function lowspeed() {
            xmlhttp.open("GET", "filename", true);
            xmlhttp.send();
        }

        function regularspeed() {
            xmlhttp.open("GET", "filename", true);
            xmlhttp.send();
        }

        function highspeed() {
            xmlhttp.open("GET", "filename", true);
            xmlhttp.send();
        }

        function nospeed() {
            xmlhttp.open("GET", "filename", true);
            xmlhttp.send();
        }

        function camera() {
            xmlhttp.open("GET", cgi - bin / )
        }
*/
