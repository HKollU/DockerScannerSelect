import http.server
import socketserver
import subprocess
target = 'google.com'
class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
	def _set_response(self):
		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()
	def do_GET(self):
		if self.path == '/':
			self.path = 'index.html'
		return http.server.SimpleHTTPRequestHandler.do_GET(self)
	def do_POST(self):
		global target
		post_data = self.rfile.read(int(self.headers['Content-Length']))
		print(post_data)
		self._set_response()
		if "target" in str(post_data):
			target=str(post_data)
			target = target[:-1]
			target = target[9:]
			if target[-1] =='F' and target[-2] == '2' and target[-3] == '%':
				target = target[:3]
			target = target.replace("http%3A%2F%2F",'')
			target = target.replace("https%3A%2F%2F",'')
			self.wfile.write(('target set to '+target + '<br> Please return to homepage to continue!').encode('utf-8'))
			print('Please return to homepage to continue!') 
		elif "1" in str(post_data):
			self.wfile.write('<!DOCTYPE html><p>The scan will take a while\n</p></html>'.encode('utf-8'))
			rec=subprocess.call(['./basic_nmap.sh', str(target)])
			file=open('BasicScan.txt','r')
			ok=file.read()
			ok=ok.replace('<',' ')
			ok=ok.replace('>',' ')
			ok=ok.replace('\n','<br />')
			self.wfile.write(('<!DOCTYPE html><p>'+str(ok)+'</p></html>').encode('utf-8'))
		elif "2" in str(post_data):
			self.wfile.write("The scan will take a while\n".encode('utf-8'))
			rc=subprocess.call(['./tcp_syn_nmap.sh', target])
			file=open('TCPSYNScan.txt','r')
			ok=file.read()
			ok=ok.replace('<',' ')
			ok=ok.replace('>',' ')
			ok=ok.replace('\n','<br />')
			self.wfile.write(('<!DOCTYPE html><p>'+str(ok)+'</p></html>').encode('utf-8'))
		elif "3" in str(post_data):
			self.wfile.write("The scan will take a while\n".encode('utf-8'))
			rc=subprocess.call(['./tcp_ack_nmap.sh', target])
			file=open('TCPACKScan.txt','r')
			ok=file.read()
			ok=ok.replace('<',' ')
			ok=ok.replace('>',' ')
			ok=ok.replace('\n','<br />')
			self.wfile.write(('<!DOCTYPE html><p>'+str(ok)+'</p></html>').encode('utf-8'))
		elif "4" in str(post_data):
			self.wfile.write("The scan will take a while\n".encode('utf-8'))
			rc=subprocess.call(['./aggressive_nmap.sh', target])
			file=open('AggressiveScan.txt','r')
			ok=file.read()
			ok=ok.replace('<',' ')
			ok=ok.replace('>',' ')
			ok=ok.replace('\n','<br />')
			self.wfile.write(('<!DOCTYPE html><p>'+str(ok)+'</p></html>').encode('utf-8'))

		elif "5" in str(post_data):
			self.wfile.write("The scan will take a while\n".encode('utf-8'))
			rc=subprocess.call(['./service_nmap.sh', target])
			file=open('ServiceScan.txt','r')
			ok=file.read()
			ok=ok.replace('<',' ')
			ok=ok.replace('>',' ')
			ok=ok.replace('\n','<br />')
			self.wfile.write(('<!DOCTYPE html><p>'+str(ok)+'</p></html>').encode('utf-8'))

		elif "6" in str(post_data):
			self.wfile.write("The scan will take a while\n".encode('utf-8'))
			rc=subprocess.call(['./uniscans.sh', target])
			file=open('Uni_Scan.txt','r')
			ok=file.read()
			ok=ok.replace('<',' ')
			ok=ok.replace('>',' ')
			ok=ok.replace('\n','<br />')
			self.wfile.write(('<!DOCTYPE html><p>'+str(ok)+'</p></html>').encode('utf-8'))
		elif "7" in str(post_data):
			self.wfile.write("The scan will take a while\n".encode('utf-8'))
			rc=subprocess.call(['./niktoscans.sh', target])
			file=open('niktoScan.txt','r')
			ok=file.read()
			ok=ok.replace('<',' ')
			ok=ok.replace('>',' ')
			ok=ok.replace('\n','<br />')
			self.wfile.write(('<!DOCTYPE html><p>'+str(ok)+'</p></html>').encode('utf-8'))
		elif "8" in str(post_data):
			self.wfile.write("The scan will take a while\n".encode('utf-8'))
			rc=subprocess.call(['./VulnerableJSDependency.sh', target])
			file=open('BurpJSDep.txt','r')
			ok=file.read()
			ok=ok.replace('<',' ')
			ok=ok.replace('>',' ')
			ok=ok.replace('\n','<br />')
			self.wfile.write(('<!DOCTYPE html><p>'+str(ok)+'</p></html>').encode('utf-8'))
		elif "9" in str(post_data):
			self.wfile.write("The scan will take a while\n".encode('utf-8'))
			rc=subprocess.call(['./HTTPParamPollute.sh', target])
			file=open('HTTPPollute.txt','r')
			ok=file.read()
			ok=ok.replace('<',' ')
			ok=ok.replace('>',' ')
			ok=ok.replace('\n','<br />')
			self.wfile.write(('<!DOCTYPE html><p>'+str(ok)+'</p></html>').encode('utf-8'))
		elif "0" in str(post_data):
			self.wfile.write("The scan will take a while\n".encode('utf-8'))
			rc=subprocess.call(['./transportSecurity.sh', target])
			file=open('TransportSec.txt','r')
			ok=file.read()
			ok=ok.replace('<',' ')
			ok=ok.replace('>',' ')
			ok=ok.replace('\n','<br />')
			self.wfile.write(('<!DOCTYPE html><p>'+str(ok)+'</p></html>'))
		elif "p" in str(post_data):
			self.wfile.write("The scan will take a while\n".encode('utf-8'))
			rc=subprocess.call(['./SourceCode.sh', target])
			file=open('Source.txt','r')
			ok=file.read()
			ok=ok.replace('<',' ')
			ok=ok.replace('>',' ')
			ok=ok.replace('\n','<br />')
			self.wfile.write(('<!DOCTYPE html><p>'+str(ok)+'</p></html>').encode('utf-8'))
		elif "q" in str(post_data):
			self.wfile.write("The scan will take a while\n".encode('utf-8'))
			rc=subprocess.call(['./cacheable.sh', target])
			file=open('cache.txt','r')
			ok=file.read()
			ok=ok.replace('<',' ')
			ok=ok.replace('>',' ')
			ok=ok.replace('\n','<br />')
			self.wfile.write(('<!DOCTYPE html><p>'+str(ok)+'</p></html>').encode('utf-8'))
		elif "r" in str(post_data):
			self.wfile.write("The scan will take a while\n".encode('utf-8'))
			rc=subprocess.call(['./robots.sh', target])
			file=open('robots.txt','r')
			ok=file.read()
			ok=ok.replace('<',' ')
			ok=ok.replace('>',' ')
			ok=ok.replace('\n','<br />')
			self.wfile.write(('<!DOCTYPE html><p>'+str(ok)+'</p></html>').encode('utf-8'))

handler_object = MyHttpRequestHandler

PORT = 80
my_server = socketserver.TCPServer(("",PORT),handler_object)

my_server.serve_forever()
