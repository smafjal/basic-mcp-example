# Basic MCP Example

## Project Description
This project demonstrates a simple implementation of a Model Context Protocol (MCP) server using the `fastmcp` library. It provides basic arithmetic operations such as addition, subtraction, multiplication, and division through an MCP server.

## Features
- **MCP Server**: Hosts tools for arithmetic operations.
- **HTTP Client**: Interacts with the MCP server to perform operations.
- **CLI Client**: Command-line interface for performing operations.

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd basic-mcp-example
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the MCP Server
Start the MCP server:
```bash
python app/server.py
```

### Using the HTTP Client
Run the HTTP client to perform operations:
```bash
python app/clients/http_client.py
```

### Using the CLI Client
Use the CLI client to perform operations:
```bash
python app/clients/cli.py <tool> <a> <b>
```
Replace `<tool>` with one of `add`, `subtract`, `multiply`, or `divide`, and `<a>` and `<b>` with numbers.

Example:
```bash
python app/clients/cli.py add 10 5
```

## Dependencies
- Python >= 3.12
- `fastmcp` >= 2.10.6