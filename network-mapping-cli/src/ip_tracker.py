import json
import os

class IPTracker:
    def __init__(self, storage_file='tracked_ips.json'):
        self.storage_file = storage_file
        self.tracked_ips = self.load_ips()

    def load_ips(self):
        if os.path.exists(self.storage_file):
            with open(self.storage_file, 'r') as f:
                return json.load(f)
        return []

    def save_ips(self):
        with open(self.storage_file, 'w') as f:
            json.dump(self.tracked_ips, f)

    def add_ip(self, ip_address):
        if ip_address not in self.tracked_ips:
            self.tracked_ips.append(ip_address)
            self.save_ips()

    def remove_ip(self, ip_address):
        if ip_address in self.tracked_ips:
            self.tracked_ips.remove(ip_address)
            self.save_ips()

    def list_ips(self):
        return self.tracked_ips