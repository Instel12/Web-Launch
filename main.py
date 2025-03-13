import os
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

try:
    script_dir = os.path.dirname(os.path.realpath(__file__))

    web_dir = os.path.join(script_dir, 'server')

    if not os.path.exists(web_dir):
        raise Exception(f"Directory '{web_dir}' does not exist")

    os.chdir(web_dir)

    port_input = input("Enter the port number to use (default is 8080): ")
    if not port_input:
        port_input = 8080
    else:
        port_input = int(port_input)

    if port_input < 1024 or port_input > 65535:
        raise Exception("Please choose a port number between 1024 and 65535.")

    Handler = SimpleHTTPRequestHandler
    httpd = TCPServer(("", port_input), Handler)

    print(f"Serving {web_dir} at port {port_input}...")
    print(f"Access the server at http://localhost:{port_input} or http://<your_public_ip>:{port_input}")

    httpd.serve_forever()

except Exception as e:
    print(f"Error: {e}")
    input("Press Enter to exit...")
