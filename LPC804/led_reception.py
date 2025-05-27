import socket # pour la communication réseau
import serial # pour la communication série


## Configuration
ARTNET_PORT = 6454
BUFFER_SIZE = 1024

## Création du socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("0.0.0.0", ARTNET_PORT))

print("Listening for Art-Net packets...")

def send_dmx_data_port_serie(dmx_data):
    # Envoi des données DMX au panneau LED en envoyant dmx_data via
    # communication série 
    with serial.Serial('/dev/ttyACM0', 9600, timeout=1) as ser:
        ser.write(dmx_data)

def conversion_hexa_to_int(dmx_data):
    #conversion de la trame dmx from hexa to int ddans [0,253]
    #pour plus de lisibilité dans à la réception
    #on renvoie dans [0, 253] car les valeurs de start et stop sont 255 et 254
    dmx_data_int = []
    #on met sous la forme 0x
    for value_hexa in dmx_data:
        if int(value_hexa) > 253:
            dmx_data_int.append(253)
        else:
            dmx_data_int.append(int(value_hexa))
        #on met une virgule entre chaque valeur
        dmx_data_int.append(',')
    return dmx_data_int

while True:
    data, addr = sock.recvfrom(BUFFER_SIZE)
    
    # Vérification de l'identifiant
    if data[:8] == b'Art-Net\0':
        opcode = int.from_bytes(data[8:10], "little")
        
        if opcode == 0x5000:  # ArtDMX packet
            universe = int.from_bytes(data[14:16], "little")
            length = int.from_bytes(data[16:18], "big")
            #on range dans les bons univers
            if universe == 0:
                dmx_data_univ_0 = data[18:18+length]
            elif universe == 1:
                dmx_data_univ_1 = data[18:18+length]
            else:
                dmx_data_unknown = data[18:18+length]
        else:
            print(f"Unknown opcode: {opcode}")
        
        #on vérifie si on a reçu les deux univers
        if dmx_data_univ_0 != [] and dmx_data_univ_1 != []:
            ## on met en forme pour envoyer le bon msg à la LPC804
                #on concatène les deux univers
            dmx_trame = dmx_data_univ_0 + dmx_data_univ_1
                #on convertit en int
            #dmx_trame = conversion_hexa_to_int(dmx_trame)
                #on rajoute bit de start et de stop
            #dmx_trame = [255] + dmx_trame + [254]
                
                #on fait un grand char en ascii
            dmx_trame = bytes(dmx_trame)
            

            dmx_data_univ_0 = []
            dmx_data_univ_1 = []
            print(f"Received DMX data for Universe {universe}: {dmx_trame}")
        
        #Envoie les données au panneau LED
        #send_dmx_data_port_serie(dmx_data)
    
    
            

