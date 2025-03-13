# Network Mapping CLI and GUI

This project is a command-line interface (CLI) and graphical user interface (GUI) application designed to track unknown IP addresses discovered during network mapping. It provides a simple way to manage and monitor IP addresses that may be of interest during network exploration.

## Features

- Track unknown IP addresses
- Add and remove IP addresses from the tracking list
- Display currently tracked IP addresses
- GUI for managing IP addresses

## Installation

To get started with the Network Mapping CLI and GUI, follow these steps:

1. Clone the repository:

   ```
   git clone <repository-url>
   cd network-mapping-cli
   ```

2. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

## Usage

### CLI

To run the CLI application, execute the following command:

```
python src/main.py
```

### Commands

- **add <ip_address>**: Add an unknown IP address to the tracking list.
- **remove <ip_address>**: Remove an IP address from the tracking list.
- **list**: Display all currently tracked IP addresses.

### GUI

To run the GUI application, execute the following command:

```
python gui.py
```

## Persistent Storage

The application uses a JSON file (`tracked_ips.json`) to store the tracked IP addresses persistently.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.