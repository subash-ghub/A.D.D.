import time
import random

class Drug:
    def __init__(self, name, dosage):
        self.name = name
        self.dosage = dosage

class DrugDispenser:
    def __init__(self, drugs):
        self.drugs = drugs

    def dispense_drug(self, drug_name, dosage):
        for drug in self.drugs:
            if drug.name == drug_name and drug.dosage == dosage:
                print(f"Dispensing {dosage} of {drug_name}")
                return True
        print("Drug not found or dosage incorrect")
        return False

class ProximitySensor:
    def detect_proximity(self):
        # Simulating proximity detection
        return random.choice([True, False])

class QRCodeScanner:
    def scan_qr_code(self):
        # Simulating QR code scanning
        return random.choice(["Aspirin", "Paracetamol", "Ibuprofen"]), random.choice([50, 100, 200])

# Example usage:
if __name__ == "__main__":
    drugs = [Drug("Aspirin", 50), Drug("Paracetamol", 100), Drug("Ibuprofen", 200)]

    dispenser = DrugDispenser(drugs)
    proximity_sensor = ProximitySensor()
    qr_code_scanner = QRCodeScanner()

    while True:
        # Wait for the user to bring the container close
        while not proximity_sensor.detect_proximity():
            print("Bring the container close to the dispenser")
            time.sleep(1)

        print("Container detected. Please scan the QR code.")
        drug_name, dosage = qr_code_scanner.scan_qr_code()
        print(f"QR code scanned: {drug_name}, Dosage: {dosage}")

        if dispenser.dispense_drug(drug_name, dosage):
            print("Please take your medication.")
            # Reset the dispenser for the next operation
            time.sleep(2)  # Simulating time to take medication
        else:
            print("Failed to dispense medication. Please try again.")

        print("------------------------------")
