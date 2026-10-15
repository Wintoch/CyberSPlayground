**How to run it:**
1. Download scapy into your own computergit
2. Find the IP addresses of three devices on your network and put them into `data.py`:
   * `ipRouter` - your main router
   * `ipLocal` - the attacking machine
   * `ipPhone` - the target device
3. Run the `main.py` file with root privileges (`sudo`).

**Notes & Limitations:**
The attack works only on unsecured `HTTP`. This is where we get a plain-text connection where devices on the local network blindly trust the responses, and there is no cryptographic verification involved. 

With `HTTPS`, it is impossible to conduct the attack in the same way because we would need valid cryptographic keys/certificates that almost all modern sites use right now. Modern traffic is heavily protected (TLS, HSTS, Certificate Pinning), making this classic attack very hard to pull off against real targets nowadays.

Modern devices cache resolved DNS queries locally for some time. If the attack doesn't seem to work, the target device might not even be sending requests to the network. In that case, you may need to clear the browser cache or flush the device's DNS cache (e.g. by toggling Airplane Mode on and off on a mobile device).