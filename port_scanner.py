import subprocess
import logging

logging.basicConfig(filename='port_scan.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def scan_ports(target_ip):
    logging.info(f'Starting scan on {target_ip}')
    try:
        result = subprocess.check_output(['nmap', '-sS', '-p-', target_ip], text=True)
        logging.info(f'Scan result for {target_ip}:\n{result}')
        print(result)  
    except subprocess.CalledProcessError as e:
        logging.error(f'Command failed with error: {e.output}')
        print(f"Erro ao executar o comando: {e.output}")
    except Exception as e:
        logging.error(f'Error scanning {target_ip}: {str(e)}')
        print(f"Erro ao escanear {target_ip}: {str(e)}")

if __name__ == "__main__":
    target = input("Enter the IP address to scan: ")
    scan_ports(target)
