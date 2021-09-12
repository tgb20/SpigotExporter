from http.server import BaseHTTPRequestHandler, HTTPServer
import requests

hostName = "localhost"
serverPort = 4829

API_URL = "https://api.spigotmc.org/simple/0.1/index.php?action=getResourcesByAuthor&id="

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):

        if self.path == "/favicon.ico":
            self.send_response(404)
            return

        author_id = self.path[1:]
        print(author_id)
        r = requests.get(API_URL + author_id)
        resources = r.json()
        if "code" in resources:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(bytes("not found", "utf-8"))
            return

        total_downloads = 0
        exporter_text = ""

        for resource in resources:
            title = resource["title"].replace(" ", "_")
            downloads = resource["stats"]["downloads"]
            total_downloads += int(downloads)
            rating = resource["stats"]["rating"]
            exporter_text += f"# HELP {title}_downloads The total number of downloads for {title}.\n# TYPE {title}_downloads counter\n{title}_downloads {downloads}\n\n"
            exporter_text += f"# HELP {title}_rating The current rating for {title}.\n# TYPE {title}_rating gauge\n{title}_rating {rating}\n\n"

        exporter_text += f"# HELP total_downloads The total number of downloads for this account.\n# TYPE total_downloads counter\ntotal_downloads {total_downloads}\n\n"
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(bytes(exporter_text, "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
