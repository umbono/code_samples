# API DEMO TEST EXAMPLE

<table>
<tr>
        <td>License</td>
        <td>
            <a href="https://opensource.org/licenses/MIT"/>
            <img src="https://img.shields.io/badge/License-MIT-yellow.svg"/>
        </td>
    </tr>
</table>

## Definition

API (Application Programming Interface) and WebSockets are both methods for building real-time, interactive applications.

API is a set of rules and protocols that allows different software applications to communicate with each other. It defines how data is exchanged between different software components. API is typically used for sending and receiving data between a client and a server, where the client makes a request to the server and the server sends back a response. REST and SOAP are examples of API protocols.

WebSockets, on the other hand, provide a way for the client and server to communicate in real-time over a single, long-lived connection. This allows for a more interactive experience, as the client can receive updates from the server as soon as they happen, rather than having to constantly poll the server for new data. WebSockets use the WebSocket protocol, which is designed to work over standard HTTP ports and uses a similar handshake process as HTTP.

Both API and WebSockets have their own use cases and advantages. API is best for simple data transfer operations, while WebSockets are more suited for real-time, bidirectional communication.

## SampleAPI

This is a sample API built using the FastAPI framework in Python. This is an example of a simple API.

## Features

    The API has a single endpoint / which returns a JSON response with the message "Hello World" when a GET request is made to it.
    The API also has a single endpoint /items/ which takes in a JSON payload with a "name" field and returns a JSON response with the name and a randomly generated id.

## Usage

    Clone the repository
    Install the required packages by running pip install -r requirements.txt
    Run the application by running python sampleapi.py

## Testing

Tests can be run using the command pytest apitest.py

# WEBSOCKET DEMO TEST EXAMPLE

## SampleAPI

This is a sample websocket built using the FastAPI framework in Python. This is an example of a simple websocket example.

## Features

This is a sample code to demonstrate the usage of WebSockets in FastAPI. The code creates a simple WebSocket endpoint at the path "/ws" and accepts incoming messages, echoes back the received message with a prefix "Message text was: ".

## Usage

    Clone the repository
    Install the required packages by running pip install -r requirements.txt
    Run the application by running python samplews.py

## Requirements

Python 3.7 or later
fastapi, uvicorn

### Output

## License

This project is licensed under the Apache License - see the LICENSE file for details.[https://github.com/rtiwariops/code_samples/blob/main/LICENSE]

## Author

Ravi Tiwari
