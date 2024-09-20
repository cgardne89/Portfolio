# Using socket library to check open ports and to get the IP address from a host name


import socket

while True:
    # Asks user to input what type of scan they want
    Scan_Type = input("Scan Type: ")
    Scan_Type = Scan_Type.capitalize()
    # If input host for the scan type it will get the IP address of said host
    if (Scan_Type == "Host"):
        Host = input("Host Name: ")
        Host_Name = socket.gethostbyname(Host)
        print("IP address: \033[92m" + str({Host_Name}))
        break
    # input port for scan type it will ask for what IP, a starting and an ending port
    if (Scan_Type == "Port"):
        open_ports = []
        IP_input = input("IP: ")
        Current_Port = int(input("Starting Port: "))
        End_Port = int(input("End Port: "))
        IP_Port = (IP_input, Current_Port)
        def connect(ip_port):
            # defining these as global so they can be used inside the function
            global Current_Port
            global End_Port
            global open_ports
            while True:
                ip_port = (IP_input, Current_Port)
                if Current_Port == End_Port:
                    break
                try:
                    socket.create_connection(ip_port)
                    # adds to the list of all open ports it finds
                    open_ports.append(Current_Port)
                    Current_Port -= 1
                except ConnectionRefusedError:
                    Current_Port -= 1
                    continue
                except Exception as e:
                    print(f"An error occurred: {e}")
            return open_ports
        testPorts = connect(IP_Port)
        if testPorts:
            print("\033[92mOpened ports:\033[0m " + str(open_ports))
        if Current_Port == End_Port:
            break
    else:
        # If user gives anything other than host or port it will loop back with an error
        print("\033[91mError:\033[0m host or port")
    
