import scapy.all as scapy
import threading
import time

class PacketCapture:
    def __init__(self, interface):
        self.interface = interface
        self.capture_packets = []
        self.capture_lock = threading.Lock()
        self.stop_sniffing = threading.Event()
        self.capture_thread = None

    def sniff_packets(self):
        # Filtro de captura para el puerto 502
        filter_expr = "port 502"
        
        def packet_handler(packet):
            # Procesa el paquete capturado
            with self.capture_lock:
                self.capture_packets.append(packet)  # Agrega el paquete a la lista
        
        # Captura paquetes en la interfaz especificada con el filtro
        scapy.sniff(iface=self.interface, filter=filter_expr, store=False, prn=packet_handler, stop_filter=lambda p: self.stop_sniffing.is_set())

    def start_capture(self):
        self.stop_sniffing.clear()  # Asegúrate de que el evento de parada esté en estado no activado
        self.capture_thread = threading.Thread(target=self.sniff_packets)
        self.capture_thread.start()
        return self.capture_thread

    def stop_capture(self):
        self.stop_sniffing.set()  # Activa el evento de parada para detener la captura
        if self.capture_thread:
            self.capture_thread.join()  # Espera a que el hilo de captura termine
        
        # Devolver el número de paquetes y los paquetes capturados
        return len(self.capture_packets), self.capture_packets

def main():
    # Especifica la interfaz de loopback
    loopback_interface = "lo"  # Cambia a "lo0" en macOS si es necesario
    capture_duration = 10  # Duración de la captura en segundos
    
    print(f"Comenzando la captura en la interfaz {loopback_interface} para el puerto 502...")
    
    # Crear una instancia de PacketCapture
    packet_capture = PacketCapture(loopback_interface)
    
    # Iniciar la captura
    capture_thread = packet_capture.start_capture()
    
    # Espera durante el tiempo de captura
    time.sleep(capture_duration)
    
    # Detener la captura y obtener resultados
    num_packets, packets = packet_capture.stop_capture()
    
    print(f"Captura completada. Número total de paquetes capturados: {num_packets}")
    for packet in packets:
        print(packet.summary())  # Muestra un resumen de cada paquete

if __name__ == "__main__":
    main()

