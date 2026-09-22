#import RPi.GPIO as GPIO
from http.server import BaseHTTPRequestHandler, HTTPServer
with open("AppCommands.txt", "w") as f:
            f.write("app-off\n")
Request = None
payload = "Empty"
def replace_line(filename, text):
   lines = None
   with open(filename,"r") as file:
       lines = file.readlines()
       #print(lines)
   if(len(lines)<2):

       with open(filename, "a") as file:
           file.write(str(text))

   elif(len(lines)==2):
       with open(filename, "w") as file:
           file.write(lines[0])
           file.write(str(text))

class RequestHandler_httpd(BaseHTTPRequestHandler):
  def do_GET(self):
    global Request
    global payload
    messagetosend = bytes(str(payload),"utf")
    self.send_response(200)
    self.send_header('Content-Type', 'text/plain')
    self.send_header('Content-Length', len(messagetosend))
    self.end_headers()
    self.wfile.write(messagetosend)
    Request = self.requestline
    Request = Request[5 : int(len(Request)-9)]
    print(Request)
    if Request == "app1":
        with open("AppCommands.txt", "w") as f:
            f.write("app-on\n")
        
    
    elif Request == "app0":
        with open("AppCommands.txt", "w") as f:
            f.write("app-off\n")
    
    elif Request == 'on':
        replace_line("AppCommands.txt","on")
        print("on")
    elif Request == 'off':
        replace_line("AppCommands.txt","off")
        print("off")
    elif "+" in Request:
        data = Request
        value = data.strip("+")
        value = ((float(value)-7*10**(-8))/(6.6*10**(-8)))+135
        print(float(value))
        with open("LUX.txt", "w") as f:
            f.write(str(int(value)))
        
    elif "%" in Request:
        value = Request
        value = value.strip("%")
        replace_line("AppCommands.txt",value)
        value = float(value)
    elif "new" in Request:
        #global payload
        with open("datalog.txt", "r") as f:
            payload = f.read()
            print(payload)
        
    else:
        print(str(Request))
    return


server_address_httpd = ('192.168.68.177',8080)
httpd = HTTPServer(server_address_httpd, RequestHandler_httpd)
print('Starting Server...')
httpd.serve_forever()
