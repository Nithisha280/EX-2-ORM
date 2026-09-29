from http.server import HTTPServer, BaseHTTPRequestHandler
import platform

class MyRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            html = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <title>Laptop Device Specifications</title>
                <style>
                    body {{
                        font-family: Arial, sans-serif;
                        background-color: #f2f2f2;
                        text-align: center;
                    }}

                    h1 {{
                        color: #333333;
                    }}

                    table {{
                        margin: 30px auto;
                        border-collapse: collapse;
                        background-color: white;
                    }}

                    th, td {{
                        border: 1px solid black;
                        padding: 12px 20px;
                    }}

                    th {{
                        background-color: #dddddd;
                    }}
                </style>
            </head>

            <body>
                <h1>Laptop Device Specifications</h1>

                <table>
                    <tr>
                        <th>Specification</th>
                        <th>Details</th>
                    </tr>

                    <tr>
                        <td>Operating System</td>
                        <td>{platform.system()} {platform.release()}</td>
                    </tr>

                    <tr>
                        <td>Machine</td>
                        <td>{platform.machine()}</td>
                    </tr>

                    <tr>
                        <td>Processor</td>
                        <td>{platform.processor()}</td>
                    </tr>

                    <tr>
                        <td>Python Version</td>
                        <td>{platform.python_version()}</td>
                    </tr>
                </table>
            </body>
            </html>
            """

            self.wfile.write(html.encode("utf-8"))

        else:
            self.send_error(404, "Page Not Found")


HOST = "127.0.0.1"
PORT = 8000

server = HTTPServer((HOST, PORT), MyRequestHandler)

print(f"Server running at http://{HOST}:{PORT}")
print("Press Ctrl+C to stop the server.")

server.serve_forever()
