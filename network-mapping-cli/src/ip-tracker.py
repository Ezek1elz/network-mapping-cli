class IPTracker:
    def __init__(self):
        self.tracked_ips = []

    def add_ip(self, ip_address):
        if ip_address not in self.tracked_ips:
            self.tracked_ips.append(ip_address)

    def remove_ip(self, ip_address):
        if ip_address in self.tracked_ips:
            self.tracked_ips.remove(ip_address)

    def list_ips(self):
        return self.tracked_ips