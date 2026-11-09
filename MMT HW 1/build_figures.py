import os
import sys
import subprocess

sys.stdout.reconfigure(encoding='utf-8')

TEMP_DIR = os.environ.get('TEMP', r'C:\Users\longh\AppData\Local\Temp')
OUTPUT_DIR = os.path.abspath(r'Answer\graphics')
CHROME_PATH = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

def render_html_to_png(html_content, output_png_path, width=980, height=540):
    temp_html = os.path.join(TEMP_DIR, 'render_temp.html')
    temp_png = os.path.join(TEMP_DIR, 'render_temp.png')
    
    with open(temp_html, 'w', encoding='utf-8') as f:
        f.write(html_content)
        
    cmd = [
        CHROME_PATH,
        '--headless=new',
        '--no-sandbox',
        '--disable-gpu',
        f'--window-size={width},{height}',
        f'--screenshot={temp_png}',
        f'file:///{temp_html.replace(os.sep, "/")}'
    ]
    subprocess.run(cmd, check=True, capture_output=True)
    
    if os.path.exists(temp_png):
        with open(temp_png, 'rb') as src, open(output_png_path, 'wb') as dst:
            dst.write(src.read())
        os.remove(temp_png)
    if os.path.exists(temp_html):
        os.remove(temp_html)
    print(f'Generated: {output_png_path}')

BASE_CSS = '''
  html, body {
    margin: 0;
    padding: 8px 10px;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
    font-size: 12px;
    background: #ffffff;
    color: #1a1a1a;
    overflow: hidden;
  }
  ::-webkit-scrollbar {
    display: none;
  }
  .filter-bar {
    background: #c5f3c5;
    border: 1px solid #7bc67b;
    border-radius: 3px;
    padding: 3px 8px;
    font-family: "Consolas", "Courier New", monospace;
    font-size: 12px;
    margin-bottom: 6px;
    display: inline-block;
    min-width: 260px;
  }
  .filter-bar::before {
    content: "Filter: ";
    color: #555;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    font-weight: 500;
  }
  .table-box {
    border: 1px solid #c8c8c8;
    margin-bottom: 6px;
    background: #ffffff;
  }
  table {
    width: 100%;
    border-collapse: collapse;
    font-size: 11.5px;
  }
  th {
    background: #f1f3f4;
    border-bottom: 1px solid #c0c0c0;
    border-right: 1px solid #e0e0e0;
    padding: 3px 6px;
    text-align: left;
    font-weight: 600;
    color: #333333;
  }
  td {
    padding: 2.5px 6px;
    white-space: nowrap;
    border-right: 1px solid #f0f0f0;
  }
  tr.tcp { background-color: #e6ecff; }
  tr.http { background-color: #e4ffc7; }
  tr.selected {
    background-color: #1a73e8 !important;
    color: #ffffff !important;
  }
  tr.selected td { color: #ffffff !important; }
  .details-box {
    border: 1px solid #c8c8c8;
    background: #ffffff;
    padding: 6px 10px;
    font-size: 11.5px;
    line-height: 1.45;
  }
  .tree-node {
    margin-left: 0px;
    padding: 1px 0;
  }
  .tree-sub {
    margin-left: 20px;
    color: #222222;
    padding: 0.5px 0;
  }
  .tree-sub-sub {
    margin-left: 36px;
    color: #444444;
  }
  .bold { font-weight: 600; }
  .highlight {
    background-color: #fff3cd;
    color: #856404;
    font-weight: bold;
    padding: 1px 4px;
    border-radius: 2px;
    border: 1px solid #ffeeba;
  }
  .arrow-down::before { content: "▾ "; font-size: 10px; color: #555; }
  .arrow-right::before { content: "▸ "; font-size: 10px; color: #555; }
  .comparison-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 8px;
  }
  .comp-pane {
    border: 1px solid #c8c8c8;
    background: #fdfdfd;
    padding: 6px 8px;
    font-size: 11px;
    line-height: 1.4;
  }
  .comp-title {
    font-weight: bold;
    background: #e9ecef;
    padding: 3px 6px;
    margin: -6px -8px 6px -8px;
    border-bottom: 1px solid #ced4da;
  }
'''

# 1. Figure 1.1: Question 1 (Inside Trace Packet 4 - HTTP GET)
fig1_1_html = f'''<!DOCTYPE html>
<html><head><meta charset="utf-8"><style>{BASE_CSS}</style></head>
<body>
  <div class="filter-bar">http || tcp.port == 80</div>
  <div class="table-box">
    <table>
      <thead><tr>
        <th style="width:35px;">No.</th><th style="width:75px;">Time</th><th style="width:95px;">Source</th>
        <th style="width:95px;">Destination</th><th style="width:60px;">Protocol</th><th style="width:50px;">Length</th><th>Info</th>
      </tr></thead>
      <tbody>
        <tr class="tcp"><td>1</td><td>0.000000</td><td>192.168.10.11</td><td>138.76.29.8</td><td>TCP</td><td>74</td><td>53924 &rarr; 80 [SYN] Seq=0 Win=64240 Len=0 MSS=1460 WS=128</td></tr>
        <tr class="tcp"><td>2</td><td>0.002092</td><td>138.76.29.8</td><td>192.168.10.11</td><td>TCP</td><td>74</td><td>80 &rarr; 53924 [SYN, ACK] Seq=0 Ack=1 Win=65160 Len=0 MSS=1460 WS=128</td></tr>
        <tr class="tcp"><td>3</td><td>0.002871</td><td>192.168.10.11</td><td>138.76.29.8</td><td>TCP</td><td>66</td><td>53924 &rarr; 80 [ACK] Seq=1 Ack=1 Win=64256 Len=0</td></tr>
        <tr class="http selected"><td>4</td><td>0.027362</td><td>192.168.10.11</td><td>138.76.29.8</td><td>HTTP</td><td>396</td><td>GET / HTTP/1.1</td></tr>
        <tr class="tcp"><td>5</td><td>0.029390</td><td>138.76.29.8</td><td>192.168.10.11</td><td>TCP</td><td>66</td><td>80 &rarr; 53924 [ACK] Seq=1 Ack=331 Win=64896 Len=0</td></tr>
        <tr class="http"><td>6</td><td>0.030672</td><td>138.76.29.8</td><td>192.168.10.11</td><td>HTTP</td><td>613</td><td>HTTP/1.1 200 OK  (text/html)</td></tr>
        <tr class="tcp"><td>7</td><td>0.031465</td><td>192.168.10.11</td><td>138.76.29.8</td><td>TCP</td><td>66</td><td>53924 &rarr; 80 [ACK] Seq=331 Ack=548 Win=64128 Len=0</td></tr>
      </tbody>
    </table>
  </div>
  <div class="details-box">
    <div class="tree-node arrow-right">Frame 4: 396 bytes on wire (3168 bits), 396 bytes captured (3168 bits) on interface eth1</div>
    <div class="tree-node arrow-right">Ethernet II, Src: PCSSystemtec_89:c7:7c (08:00:27:89:c7:7c), Dst: PCSSystemtec_82:36:d7 (08:00:27:82:36:d7)</div>
    <div class="tree-node arrow-down"><span class="bold">Internet Protocol Version 4, Src: 192.168.10.11, Dst: 138.76.29.8</span></div>
    <div class="tree-sub">0100 .... = Version: 4</div>
    <div class="tree-sub">.... 0101 = Header Length: 20 bytes (5)</div>
    <div class="tree-sub">Total Length: 382</div>
    <div class="tree-sub">Identification: 0x6296 (25238)</div>
    <div class="tree-sub">010. .... = Flags: 0x2, Don't fragment</div>
    <div class="tree-sub">Time to Live: 64</div>
    <div class="tree-sub">Protocol: TCP (6)</div>
    <div class="tree-sub">Header Checksum: 0x64dc [validation disabled]</div>
    <div class="tree-sub"><span class="highlight">Source Address: 192.168.10.11</span></div>
    <div class="tree-sub"><span class="highlight">Destination Address: 138.76.29.8</span></div>
    <div class="tree-node arrow-down"><span class="bold">Transmission Control Protocol, Src Port: 53924, Dst Port: 80, Seq: 1, Ack: 1, Len: 330</span></div>
    <div class="tree-sub"><span class="highlight">Source Port: 53924</span></div>
    <div class="tree-sub"><span class="highlight">Destination Port: 80</span></div>
    <div class="tree-sub">Sequence Number: 1    (relative sequence number)</div>
    <div class="tree-sub">Acknowledgment Number: 1    (relative ack number)</div>
    <div class="tree-sub">Flags: 0x018 (PSH, ACK)</div>
    <div class="tree-sub">Window: 502 (Calculated window size: 64256)</div>
    <div class="tree-sub">Checksum: 0x1bea [unverified]</div>
    <div class="tree-node arrow-right">Hypertext Transfer Protocol</div>
  </div>
</body></html>'''

# 2. Figure 2.1: Question 2 & 3 (Inside Trace Packet 6 - HTTP 200 OK)
fig2_1_html = f'''<!DOCTYPE html>
<html><head><meta charset="utf-8"><style>{BASE_CSS}</style></head>
<body>
  <div class="filter-bar">http || tcp.port == 80</div>
  <div class="table-box">
    <table>
      <thead><tr>
        <th style="width:35px;">No.</th><th style="width:75px;">Time</th><th style="width:95px;">Source</th>
        <th style="width:95px;">Destination</th><th style="width:60px;">Protocol</th><th style="width:50px;">Length</th><th>Info</th>
      </tr></thead>
      <tbody>
        <tr class="http"><td>4</td><td>0.027362</td><td>192.168.10.11</td><td>138.76.29.8</td><td>HTTP</td><td>396</td><td>GET / HTTP/1.1</td></tr>
        <tr class="tcp"><td>5</td><td>0.029390</td><td>138.76.29.8</td><td>192.168.10.11</td><td>TCP</td><td>66</td><td>80 &rarr; 53924 [ACK] Seq=1 Ack=331 Win=64896 Len=0</td></tr>
        <tr class="http selected"><td>6</td><td>0.030672</td><td>138.76.29.8</td><td>192.168.10.11</td><td>HTTP</td><td>613</td><td>HTTP/1.1 200 OK  (text/html)</td></tr>
        <tr class="tcp"><td>7</td><td>0.031465</td><td>192.168.10.11</td><td>138.76.29.8</td><td>TCP</td><td>66</td><td>53924 &rarr; 80 [ACK] Seq=331 Ack=548 Win=64128 Len=0</td></tr>
        <tr class="http"><td>8</td><td>0.231407</td><td>192.168.10.11</td><td>138.76.29.8</td><td>HTTP</td><td>317</td><td>GET /favicon.ico HTTP/1.1</td></tr>
        <tr class="tcp"><td>9</td><td>0.232897</td><td>138.76.29.8</td><td>192.168.10.11</td><td>TCP</td><td>66</td><td>80 &rarr; 53924 [ACK] Seq=548 Ack=582 Win=64768 Len=0</td></tr>
      </tbody>
    </table>
  </div>
  <div class="details-box">
    <div class="tree-node arrow-down"><span class="bold">Frame 6: 613 bytes on wire (4904 bits), 613 bytes captured (4904 bits) on interface eth1</span></div>
    <div class="tree-sub"><span class="highlight">[Time since reference or first frame: 0.030672101 seconds]</span></div>
    <div class="tree-sub">Epoch Arrival Time: 1616989827.774683377</div>
    <div class="tree-node arrow-right">Ethernet II, Src: PCSSystemtec_82:36:d7 (08:00:27:82:36:d7), Dst: PCSSystemtec_89:c7:7c (08:00:27:89:c7:7c)</div>
    <div class="tree-node arrow-down"><span class="bold">Internet Protocol Version 4, Src: 138.76.29.8, Dst: 192.168.10.11</span></div>
    <div class="tree-sub">0100 .... = Version: 4</div>
    <div class="tree-sub">.... 0101 = Header Length: 20 bytes (5)</div>
    <div class="tree-sub">Total Length: 599</div>
    <div class="tree-sub">Time to Live: 62</div>
    <div class="tree-sub">Protocol: TCP (6)</div>
    <div class="tree-sub">Header Checksum: 0x5c1d [validation disabled]</div>
    <div class="tree-sub"><span class="highlight">Source Address: 138.76.29.8</span></div>
    <div class="tree-sub"><span class="highlight">Destination Address: 192.168.10.11</span></div>
    <div class="tree-node arrow-down"><span class="bold">Transmission Control Protocol, Src Port: 80, Dst Port: 53924, Seq: 1, Ack: 331, Len: 547</span></div>
    <div class="tree-sub"><span class="highlight">Source Port: 80</span></div>
    <div class="tree-sub"><span class="highlight">Destination Port: 53924</span></div>
    <div class="tree-sub">Sequence Number: 1    (relative sequence number)</div>
    <div class="tree-sub">Acknowledgment Number: 331    (relative ack number)</div>
    <div class="tree-sub">Flags: 0x018 (PSH, ACK)</div>
    <div class="tree-sub">Checksum: 0x2c58 [unverified]</div>
    <div class="tree-node arrow-right">Hypertext Transfer Protocol (HTTP/1.1 200 OK)</div>
  </div>
</body></html>'''

# 3. Figure 4.1: Question 4 & 5 (Outside Trace Packet 4 - HTTP GET)
fig4_1_html = f'''<!DOCTYPE html>
<html><head><meta charset="utf-8"><style>{BASE_CSS}</style></head>
<body>
  <div class="filter-bar">http || tcp.port == 80</div>
  <div class="table-box">
    <table>
      <thead><tr>
        <th style="width:35px;">No.</th><th style="width:75px;">Time</th><th style="width:95px;">Source</th>
        <th style="width:95px;">Destination</th><th style="width:60px;">Protocol</th><th style="width:50px;">Length</th><th>Info</th>
      </tr></thead>
      <tbody>
        <tr class="tcp"><td>1</td><td>0.000000</td><td>10.0.1.254</td><td>138.76.29.8</td><td>TCP</td><td>74</td><td>53924 &rarr; 80 [SYN] Seq=0 Win=64240 Len=0 MSS=1460 WS=128</td></tr>
        <tr class="tcp"><td>2</td><td>0.002058</td><td>138.76.29.8</td><td>10.0.1.254</td><td>TCP</td><td>74</td><td>80 &rarr; 53924 [SYN, ACK] Seq=0 Ack=1 Win=65160 Len=0 MSS=1460 WS=128</td></tr>
        <tr class="tcp"><td>3</td><td>0.002854</td><td>10.0.1.254</td><td>138.76.29.8</td><td>TCP</td><td>66</td><td>53924 &rarr; 80 [ACK] Seq=1 Ack=1 Win=64256 Len=0</td></tr>
        <tr class="http selected"><td>4</td><td>0.027356</td><td>10.0.1.254</td><td>138.76.29.8</td><td>HTTP</td><td>396</td><td>GET / HTTP/1.1</td></tr>
        <tr class="tcp"><td>5</td><td>0.029339</td><td>138.76.29.8</td><td>10.0.1.254</td><td>TCP</td><td>66</td><td>80 &rarr; 53924 [ACK] Seq=1 Ack=331 Win=64896 Len=0</td></tr>
        <tr class="http"><td>6</td><td>0.030626</td><td>138.76.29.8</td><td>10.0.1.254</td><td>HTTP</td><td>613</td><td>HTTP/1.1 200 OK  (text/html)</td></tr>
        <tr class="tcp"><td>7</td><td>0.031449</td><td>10.0.1.254</td><td>138.76.29.8</td><td>TCP</td><td>66</td><td>53924 &rarr; 80 [ACK] Seq=331 Ack=548 Win=64128 Len=0</td></tr>
      </tbody>
    </table>
  </div>
  <div class="details-box">
    <div class="tree-node arrow-down"><span class="bold">Frame 4: 396 bytes on wire (3168 bits), 396 bytes captured (3168 bits) on interface eth0</span></div>
    <div class="tree-sub"><span class="highlight">[Time since reference or first frame: 0.027356291 seconds]</span></div>
    <div class="tree-sub">Epoch Arrival Time: 1616989827.771391145</div>
    <div class="tree-node arrow-right">Ethernet II, Src: PCSSystemtec_43:65:cd (08:00:27:43:65:cd), Dst: PCSSystemtec_22:fd:74 (08:00:27:22:fd:74)</div>
    <div class="tree-node arrow-down"><span class="bold">Internet Protocol Version 4, Src: 10.0.1.254, Dst: 138.76.29.8</span></div>
    <div class="tree-sub">0100 .... = Version: 4</div>
    <div class="tree-sub">.... 0101 = Header Length: 20 bytes (5)</div>
    <div class="tree-sub">Total Length: 382</div>
    <div class="tree-sub">Identification: 0x6296 (25238)</div>
    <div class="tree-sub">010. .... = Flags: 0x2, Don't fragment</div>
    <div class="tree-sub">Time to Live: 63</div>
    <div class="tree-sub">Protocol: TCP (6)</div>
    <div class="tree-sub">Header Checksum: 0x2492 [validation disabled]</div>
    <div class="tree-sub"><span class="highlight">Source Address: 10.0.1.254</span></div>
    <div class="tree-sub"><span class="highlight">Destination Address: 138.76.29.8</span></div>
    <div class="tree-node arrow-down"><span class="bold">Transmission Control Protocol, Src Port: 53924, Dst Port: 80, Seq: 1, Ack: 1, Len: 330</span></div>
    <div class="tree-sub"><span class="highlight">Source Port: 53924</span></div>
    <div class="tree-sub"><span class="highlight">Destination Port: 80</span></div>
    <div class="tree-sub">Sequence Number: 1    (relative sequence number)</div>
    <div class="tree-sub">Acknowledgment Number: 1    (relative ack number)</div>
    <div class="tree-sub">Flags: 0x018 (PSH, ACK)</div>
    <div class="tree-sub">Checksum: 0xda9f [unverified]</div>
    <div class="tree-node arrow-right">Hypertext Transfer Protocol</div>
  </div>
</body></html>'''

# 4. Figure 7.1: Question 7 (HTTP Payload comparison inside vs outside)
fig7_1_html = f'''<!DOCTYPE html>
<html><head><meta charset="utf-8"><style>{BASE_CSS}</style></head>
<body>
  <div style="font-weight:600; margin-bottom:6px; color:#2c3e50; font-size:12.5px;">Comparison: Hypertext Transfer Protocol (HTTP GET) Payload Inside LAN vs. Outside Internet</div>
  <div class="comparison-grid">
    <div class="comp-pane">
      <div class="comp-title">LAN Side (nat-inside-wireshark-trace1-1.pcapng, Packet 4)</div>
      <div class="tree-node arrow-down"><span class="bold">Hypertext Transfer Protocol</span></div>
      <div class="tree-sub arrow-down">GET / HTTP/1.1\r\n</div>
      <div class="tree-sub-sub">Request Method: GET</div>
      <div class="tree-sub-sub">Request URI: /</div>
      <div class="tree-sub-sub">Request Version: HTTP/1.1</div>
      <div class="tree-sub">Host: 138.76.29.8\r\n</div>
      <div class="tree-sub">User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:75.0) Gecko/20100101 Firefox/75.0\r\n</div>
      <div class="tree-sub">Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\r\n</div>
      <div class="tree-sub">Accept-Language: en-US,en;q=0.5\r\n</div>
      <div class="tree-sub">Accept-Encoding: gzip, deflate\r\n</div>
      <div class="tree-sub">Connection: keep-alive\r\n</div>
      <div class="tree-sub">Upgrade-Insecure-Requests: 1\r\n</div>
      <div class="tree-sub">\r\n</div>
      <div style="margin-top:8px; padding:4px 6px; background:#e8f4fd; border-radius:3px;">
        <span class="highlight">TCP Payload Length: 330 bytes</span> (Identical)
      </div>
    </div>
    <div class="comp-pane">
      <div class="comp-title">Internet Side (nat-outside-wireshark-trace1-1.pcapng, Packet 4)</div>
      <div class="tree-node arrow-down"><span class="bold">Hypertext Transfer Protocol</span></div>
      <div class="tree-sub arrow-down">GET / HTTP/1.1\r\n</div>
      <div class="tree-sub-sub">Request Method: GET</div>
      <div class="tree-sub-sub">Request URI: /</div>
      <div class="tree-sub-sub">Request Version: HTTP/1.1</div>
      <div class="tree-sub">Host: 138.76.29.8\r\n</div>
      <div class="tree-sub">User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:75.0) Gecko/20100101 Firefox/75.0\r\n</div>
      <div class="tree-sub">Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\r\n</div>
      <div class="tree-sub">Accept-Language: en-US,en;q=0.5\r\n</div>
      <div class="tree-sub">Accept-Encoding: gzip, deflate\r\n</div>
      <div class="tree-sub">Connection: keep-alive\r\n</div>
      <div class="tree-sub">Upgrade-Insecure-Requests: 1\r\n</div>
      <div class="tree-sub">\r\n</div>
      <div style="margin-top:8px; padding:4px 6px; background:#e8f4fd; border-radius:3px;">
        <span class="highlight">TCP Payload Length: 330 bytes</span> (Identical)
      </div>
    </div>
  </div>
</body></html>'''

# 5. Figure 8.1: Question 8 (IP Header comparison: Version, Header Length, Flags, Checksum)
fig8_1_html = f'''<!DOCTYPE html>
<html><head><meta charset="utf-8"><style>{BASE_CSS}</style></head>
<body>
  <div style="font-weight:600; margin-bottom:6px; color:#2c3e50; font-size:12.5px;">Comparison: IP Header Fields of Packet 4 (Inside LAN vs. Outside Internet)</div>
  <div class="comparison-grid">
    <div class="comp-pane">
      <div class="comp-title">LAN Side (nat-inside-wireshark-trace1-1.pcapng)</div>
      <div class="tree-node arrow-down"><span class="bold">Internet Protocol Version 4</span></div>
      <div class="tree-sub"><b>Version:</b> 4 (0100 ....) &rarr; <span style="color:green;font-weight:600;">Unchanged</span></div>
      <div class="tree-sub"><b>Header Length:</b> 20 bytes (5) &rarr; <span style="color:green;font-weight:600;">Unchanged</span></div>
      <div class="tree-sub">Differentiated Services Field: 0x00 (DSCP: CS0, ECN: Not-ECT)</div>
      <div class="tree-sub">Total Length: 382</div>
      <div class="tree-sub">Identification: 0x6296 (25238)</div>
      <div class="tree-sub"><b>Flags:</b> 0x2, Don't fragment (010. ....) &rarr; <span style="color:green;font-weight:600;">Unchanged</span></div>
      <div class="tree-sub">Time to Live: 64</div>
      <div class="tree-sub">Protocol: TCP (6)</div>
      <div class="tree-sub"><span class="highlight"><b>Header Checksum:</b> 0x64dc</span></div>
      <div class="tree-sub"><span class="highlight"><b>Source Address:</b> 192.168.10.11</span></div>
      <div class="tree-sub"><b>Destination Address:</b> 138.76.29.8</div>
    </div>
    <div class="comp-pane">
      <div class="comp-title">Internet Side (nat-outside-wireshark-trace1-1.pcapng)</div>
      <div class="tree-node arrow-down"><span class="bold">Internet Protocol Version 4</span></div>
      <div class="tree-sub"><b>Version:</b> 4 (0100 ....) &rarr; <span style="color:green;font-weight:600;">Unchanged</span></div>
      <div class="tree-sub"><b>Header Length:</b> 20 bytes (5) &rarr; <span style="color:green;font-weight:600;">Unchanged</span></div>
      <div class="tree-sub">Differentiated Services Field: 0x00 (DSCP: CS0, ECN: Not-ECT)</div>
      <div class="tree-sub">Total Length: 382</div>
      <div class="tree-sub">Identification: 0x6296 (25238)</div>
      <div class="tree-sub"><b>Flags:</b> 0x2, Don't fragment (010. ....) &rarr; <span style="color:green;font-weight:600;">Unchanged</span></div>
      <div class="tree-sub">Time to Live: 63 (decremented by 1)</div>
      <div class="tree-sub">Protocol: TCP (6)</div>
      <div class="tree-sub"><span class="highlight"><b>Header Checksum:</b> 0x2492 (CHANGED)</span></div>
      <div class="tree-sub"><span class="highlight"><b>Source Address:</b> 10.0.1.254 (CHANGED)</span></div>
      <div class="tree-sub"><b>Destination Address:</b> 138.76.29.8</div>
    </div>
  </div>
</body></html>'''

# 6. Figure 9.1: Question 9 & 10 (Outside Trace Packet 6 - HTTP 200 OK)
fig9_1_html = f'''<!DOCTYPE html>
<html><head><meta charset="utf-8"><style>{BASE_CSS}</style></head>
<body>
  <div class="filter-bar">http || tcp.port == 80</div>
  <div class="table-box">
    <table>
      <thead><tr>
        <th style="width:35px;">No.</th><th style="width:75px;">Time</th><th style="width:95px;">Source</th>
        <th style="width:95px;">Destination</th><th style="width:60px;">Protocol</th><th style="width:50px;">Length</th><th>Info</th>
      </tr></thead>
      <tbody>
        <tr class="http"><td>4</td><td>0.027356</td><td>10.0.1.254</td><td>138.76.29.8</td><td>HTTP</td><td>396</td><td>GET / HTTP/1.1</td></tr>
        <tr class="tcp"><td>5</td><td>0.029339</td><td>138.76.29.8</td><td>10.0.1.254</td><td>TCP</td><td>66</td><td>80 &rarr; 53924 [ACK] Seq=1 Ack=331 Win=64896 Len=0</td></tr>
        <tr class="http selected"><td>6</td><td>0.030626</td><td>138.76.29.8</td><td>10.0.1.254</td><td>HTTP</td><td>613</td><td>HTTP/1.1 200 OK  (text/html)</td></tr>
        <tr class="tcp"><td>7</td><td>0.031449</td><td>10.0.1.254</td><td>138.76.29.8</td><td>TCP</td><td>66</td><td>53924 &rarr; 80 [ACK] Seq=331 Ack=548 Win=64128 Len=0</td></tr>
        <tr class="http"><td>8</td><td>0.231400</td><td>10.0.1.254</td><td>138.76.29.8</td><td>HTTP</td><td>317</td><td>GET /favicon.ico HTTP/1.1</td></tr>
        <tr class="tcp"><td>9</td><td>0.232864</td><td>138.76.29.8</td><td>10.0.1.254</td><td>TCP</td><td>66</td><td>80 &rarr; 53924 [ACK] Seq=548 Ack=582 Win=64768 Len=0</td></tr>
      </tbody>
    </table>
  </div>
  <div class="details-box">
    <div class="tree-node arrow-down"><span class="bold">Frame 6: 613 bytes on wire (4904 bits), 613 bytes captured (4904 bits) on interface eth0</span></div>
    <div class="tree-sub"><span class="highlight">[Time since reference or first frame: 0.030625966 seconds]</span></div>
    <div class="tree-sub">Epoch Arrival Time: 1616989827.774660820</div>
    <div class="tree-node arrow-right">Ethernet II, Src: PCSSystemtec_22:fd:74 (08:00:27:22:fd:74), Dst: PCSSystemtec_43:65:cd (08:00:27:43:65:cd)</div>
    <div class="tree-node arrow-down"><span class="bold">Internet Protocol Version 4, Src: 138.76.29.8, Dst: 10.0.1.254</span></div>
    <div class="tree-sub">0100 .... = Version: 4</div>
    <div class="tree-sub">.... 0101 = Header Length: 20 bytes (5)</div>
    <div class="tree-sub">Total Length: 599</div>
    <div class="tree-sub">Time to Live: 63</div>
    <div class="tree-sub">Protocol: TCP (6)</div>
    <div class="tree-sub">Header Checksum: 0x19d3 [validation disabled]</div>
    <div class="tree-sub"><span class="highlight">Source Address: 138.76.29.8</span></div>
    <div class="tree-sub"><span class="highlight">Destination Address: 10.0.1.254</span></div>
    <div class="tree-node arrow-down"><span class="bold">Transmission Control Protocol, Src Port: 80, Dst Port: 53924, Seq: 1, Ack: 331, Len: 547</span></div>
    <div class="tree-sub"><span class="highlight">Source Port: 80</span></div>
    <div class="tree-sub"><span class="highlight">Destination Port: 53924</span></div>
    <div class="tree-sub">Sequence Number: 1    (relative sequence number)</div>
    <div class="tree-sub">Acknowledgment Number: 331    (relative ack number)</div>
    <div class="tree-sub">Flags: 0x018 (PSH, ACK)</div>
    <div class="tree-sub">Checksum: 0xeb0d [unverified]</div>
    <div class="tree-node arrow-right">Hypertext Transfer Protocol (HTTP/1.1 200 OK)</div>
  </div>
</body></html>'''

# 7. Figure 11.1: Question 11 (Inside Trace Packet 6 - Confirming NAT Reverse Translation)
fig11_1_html = f'''<!DOCTYPE html>
<html><head><meta charset="utf-8"><style>{BASE_CSS}</style></head>
<body>
  <div class="filter-bar">http || tcp.port == 80</div>
  <div class="table-box">
    <table>
      <thead><tr>
        <th style="width:35px;">No.</th><th style="width:75px;">Time</th><th style="width:95px;">Source</th>
        <th style="width:95px;">Destination</th><th style="width:60px;">Protocol</th><th style="width:50px;">Length</th><th>Info</th>
      </tr></thead>
      <tbody>
        <tr class="http"><td>4</td><td>0.027362</td><td>192.168.10.11</td><td>138.76.29.8</td><td>HTTP</td><td>396</td><td>GET / HTTP/1.1</td></tr>
        <tr class="tcp"><td>5</td><td>0.029390</td><td>138.76.29.8</td><td>192.168.10.11</td><td>TCP</td><td>66</td><td>80 &rarr; 53924 [ACK] Seq=1 Ack=331 Win=64896 Len=0</td></tr>
        <tr class="http selected"><td>6</td><td>0.030672</td><td>138.76.29.8</td><td>192.168.10.11</td><td>HTTP</td><td>613</td><td>HTTP/1.1 200 OK  (text/html)</td></tr>
        <tr class="tcp"><td>7</td><td>0.031465</td><td>192.168.10.11</td><td>138.76.29.8</td><td>TCP</td><td>66</td><td>53924 &rarr; 80 [ACK] Seq=331 Ack=548 Win=64128 Len=0</td></tr>
      </tbody>
    </table>
  </div>
  <div class="details-box">
    <div class="tree-node arrow-down"><span class="bold">Internet Protocol Version 4, Src: 138.76.29.8, Dst: 192.168.10.11</span></div>
    <div class="tree-sub">Source Address: <span class="highlight">138.76.29.8</span></div>
    <div class="tree-sub">Destination Address: <span class="highlight">192.168.10.11 (Translated by NAT router back to internal LAN IP)</span></div>
    <div class="tree-node arrow-down"><span class="bold">Transmission Control Protocol, Src Port: 80, Dst Port: 53924</span></div>
    <div class="tree-sub">Source Port: <span class="highlight">80</span></div>
    <div class="tree-sub">Destination Port: <span class="highlight">53924</span></div>
    <div class="tree-node arrow-right">Hypertext Transfer Protocol</div>
  </div>
</body></html>'''

renders = [
    (fig1_1_html, os.path.join(OUTPUT_DIR, 'fig1_1.png'), 980, 580),
    (fig2_1_html, os.path.join(OUTPUT_DIR, 'fig2_1.png'), 980, 580),
    (fig4_1_html, os.path.join(OUTPUT_DIR, 'fig4_1.png'), 980, 580),
    (fig7_1_html, os.path.join(OUTPUT_DIR, 'fig7_1.png'), 980, 450),
    (fig8_1_html, os.path.join(OUTPUT_DIR, 'fig8_1.png'), 980, 420),
    (fig9_1_html, os.path.join(OUTPUT_DIR, 'fig9_1.png'), 980, 580),
    (fig11_1_html, os.path.join(OUTPUT_DIR, 'fig11_1.png'), 980, 360),
]

for html, path, w, h in renders:
    render_html_to_png(html, path, w, h)

print('All figures built successfully!')
