from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class SimplePOSTHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # 1. Get the size of the incoming data
        content_length = int(self.headers.get('Content-Length', 0))
        
        # 2. Read and decode the raw body bytes
        post_data = self.rfile.read(content_length).decode('utf-8')
        
        # 3. Parse JSON if applicable
        try:
            data = json.loads(post_data)
            print("Received JSON:", data)
        except json.JSONDecodeError:
            print("Received raw text:", post_data)

        # 4. Send a 200 OK response back to the client
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        
        response = {"status": "received", "length": content_length}
        self.wfile.write(json.dumps(response).encode('utf-8'))

if __name__ == '__main__':
    server = HTTPServer(('localhost', 8000), SimplePOSTHandler)
    print("Server running at http://localhost:8000")
    server.serve_forever()