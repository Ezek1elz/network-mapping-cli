import click
from ip_tracker import IPTracker

tracker = IPTracker()

@click.group()
def main():
    """Network Mapping CLI"""
    pass

@main.command()
@click.argument('ip_address')
def add(ip_address):
    """Add an unknown IP address to the tracking list."""
    tracker.add_ip(ip_address)
    click.echo(f"Added IP address: {ip_address}")

@main.command()
@click.argument('ip_address')
def remove(ip_address):
    """Remove an IP address from the tracking list."""
    tracker.remove_ip(ip_address)
    click.echo(f"Removed IP address: {ip_address}")

@main.command()
def list():
    """Display all currently tracked IP addresses."""
    ips = tracker.list_ips()
    click.echo("Tracked IP addresses:")
    for ip in ips:
        click.echo(ip)