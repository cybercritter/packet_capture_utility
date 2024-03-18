# CS1400 Final Project Proposal - Simplified tcpdump clone in Python
 ---

This app will capture packets from the IP stack determine if the l4 protocol is well known or custom.<br>

If the protocol is well known the IP/TCP/UDP information and data will be processed and presented in user readable format.

If the protocol is custom the IP/TCP/UDP information will be provided in user format.

## Requirements  
JonA- From Discord Channel<br>

**IF YOU ARE NOT PLANNING ON DOING THE DEFAULT PROJECT MENTIONED ABOVE, YOU NEED TO PLAN AND DISCUSS WHAT YOUR'RE DOING WITH ME BEFORE THIS THURSDAY**<br>
The main goals / requirements for the final project are to get you familiar with the following:
1. Writing and using your own classes/objects
2. File Input / Output
3. Handling errors (when applicable)

---
## Project Requirements
1. Connect to the IP stack via raw socket
2. Process IP packet.
   
   * Determine packet type.
   * Decode TCP/UDP packet header 
   * Assign packet to data structure for future use (logging/console)
3. Read configuration in JSON format
   * set if log to screen or JSON data file

----

### Project Structure

```bash
app\
    pcktlib\
        __init__.py
        ip_header.py
        tcp_header.py
        udp_header.py
        packet_type.py
    logging\
        packt_log_json.py
        packt_log_logger.py
    utilities\
        __init__.py
        packet_logger.py
        packet_data_processor.py
    main.py
    packet_capture_config.json
```


 