# bariera

## Description
Some repo to store what triggers the barrier automation.
Just in case, if SD card is toasted, the backup is lost, etc.

One would need to set a hostname (I use duckDNS or similar) 
Also, HTTP header is required to authorize the call.

There is also rate-limiting in the nginx conf, and specific 
sleep times are per the original BFT remote.

## Redeploy on fresh Raspberry

-It would be best to install DietPI.
-Make sure you have python 3.x and nginx installed
-Copy the nginx config  file over /etc/nginx/sites-available/default
-Satisfy the lib dependencies from bariera.py using pip install
-Place bariera.py e.g. in /opt, and make it executable
-Start it using python3 /opt/bariera.py
-Optionally  add the above to start on boot.
