# HƯỚNG DẪN CHI TIẾT CÁCH CHỤP VÀ CROP ẢNH BẰNG CHỨNG (WIRESHARK LAB 7)

Tất cả các hình ảnh sau khi chụp và crop sẽ được lưu vào thư mục:  
📁 `Lab7/graphics/`  
với tên file tương ứng như liệt kê dưới đây để khớp 100% với file báo cáo `report.tex`.

---

## 📌 Hướng dẫn chung khi chụp ảnh trong Wireshark
* **Giao diện Wireshark gồm 3 khung:**
  1. *Khung trên (Packet List):* Danh sách gói tin (No., Time, Source, Destination, Protocol, Info).
  2. *Khung giữa (Packet Details):* Cây phân cấp chi tiết các giao thức (Frame, Radiotap, IEEE 802.11, IP, TCP, ...).
  3. *Khung dưới (Packet Bytes):* Mã hex/ASCII.
* **Cách crop chuẩn và đẹp nhất cho báo cáo:**
  * Chọn gói tin tương ứng ở khung trên.
  * Mở rộng (expand) nhánh thông tin cần làm bằng chứng ở khung giữa, nhấp chuột vào trường thông số để nó được tô sáng (highlight).
  * Dùng công cụ chụp màn hình (như **Snipping Tool** trên Windows: tổ hợp phím `Win + Shift + S`) để khoanh vùng:
    * Có thể chụp kết hợp: vài dòng packet list + khung chi tiết gói tin đã mở rộng trường cần chứng minh.
    * Đảm bảo thấy rõ số gói (`No.`), `Time`, và trường dữ liệu được in đậm/tô sáng.

---

## 📸 Danh mục 16 câu hỏi & Hướng dẫn chụp chi tiết

---

### CÂU 1: SSIDs của 2 AP phát nhiều Beacon nhất
* **Tên file cần lưu:** `fig1.png`
* **Bộ lọc Wireshark (Display Filter):**
  ```wireshark
  wlan.fc.type_subtype == 0x08
  ```
* **Gói tin cần chọn:** Gói **No. 1** (hoặc mở menu **Statistics $\rightarrow$ WLAN Traffic** nếu muốn chụp bảng thống kê).
* **Vùng cần mở ở khung giữa (Packet Details):**
  * Nhấp mở: `IEEE 802.11 wireless LAN management frame`
  * Nhấp mở: `Tagged parameters`
  * Nhấp chọn vào dòng: `Tag: SSID parameter set: 30 Munroe St` (để tô sáng tên SSID).
* **Cách crop:** Chụp khung trên thấy các gói tin Beacon mang SSID `'30 Munroe St'` và `'linksys12'` (ví dụ như gói 1 và gói 10), kèm khung giữa đang highlight `SSID parameter set: 30 Munroe St`.

---

### CÂU 2: Khoảng thời gian Beacon Interval của 2 AP
#### Hình 2.1: Cho AP "30 Munroe St"
* **Tên file cần lưu:** `fig2_1.png`
* **Bộ lọc Wireshark:**
  ```wireshark
  frame.number == 1
  ```
* **Vùng cần mở ở khung giữa:**
  * Mở `IEEE 802.11 wireless LAN management frame`
  * Mở `Fixed parameters`
  * Nhấp chọn dòng: **`Beacon Interval: 0.102400 [Seconds] (100 [Time Units])`** (hoặc `0.102400 seconds`).
* **Cách crop:** Crop khung giữa tập trung vào phần `Fixed parameters` hiển thị rõ `Beacon Interval`.

#### Hình 2.2: Cho AP "linksys_ses_24086"
* **Tên file cần lưu:** `fig2_2.png`
* **Bộ lọc Wireshark:**
  ```wireshark
  wlan.ssid contains "linksys_SES" && wlan.fc.type_subtype == 0x08
  ```
* **Gói tin cần chọn:** Chọn gói **No. 1774** (hoặc 1794, 1814,...).
* **Vùng cần mở ở khung giữa:**
  * Mở `Fixed parameters`
  * Nhấp chọn dòng: **`Beacon Interval: 0.102400 [Seconds] (100 [Time Units])`**.
* **Cách crop:** Crop khung giữa hiển thị rõ `Beacon Interval` của AP này.

---

### CÂU 3, 4, 5: Địa chỉ MAC Source, Destination và BSSID của Beacon Frame (30 Munroe St)
* **Tên file cần lưu:** `fig3_4_5.png` (sử dụng làm bằng chứng chung cho cả 3 câu 3, 4, 5)
* **Bộ lọc Wireshark:**
  ```wireshark
  frame.number == 1
  ```
* **Gói tin cần chọn:** Gói **No. 1**.
* **Vùng cần mở ở khung giữa:**
  * Mở nhánh: `IEEE 802.11 Beacon Frame`
  * Sẽ thấy rõ 3 trường địa chỉ liên tiếp:
    * `Receiver address: Broadcast (ff:ff:ff:ff:ff:ff)` $\rightarrow$ **Destination MAC (Câu 4)**
    * `Destination address: Broadcast (ff:ff:ff:ff:ff:ff)`
    * `Transmitter address: Cisco-Li_f7:1d:51 (00:16:b6:f7:1d:51)` $\rightarrow$ **Source MAC (Câu 3)**
    * `Source address: Cisco-Li_f7:1d:51 (00:16:b6:f7:1d:51)`
    * `BSS Id: Cisco-Li_f7:1d:51 (00:16:b6:f7:1d:51)` $\rightarrow$ **BSS ID (Câu 5)**
* **Cách crop:** Crop khung giữa chứa trọn vẹn phần Header của IEEE 802.11 thấy đủ cả 3 địa chỉ MAC trên.

---

### CÂU 6: Tốc độ truyền (Supported Rates & Extended Supported Rates) của 30 Munroe St
* **Tên file cần lưu:** `fig6.png`
* **Bộ lọc Wireshark:**
  ```wireshark
  frame.number == 1
  ```
* **Gói tin cần chọn:** Gói **No. 1**.
* **Vùng cần mở ở khung giữa:**
  * Mở `IEEE 802.11 wireless LAN management frame` $\rightarrow$ `Tagged parameters`
  * Mở rộng cả 2 thẻ:
    * `Tag: Supported Rates 1(B), 2(B), 5.5(B), 11(B) [Mbit/sec]` (4 tốc độ 802.11b).
    * `Tag: Extended Supported Rates 6, 9, 12, 18, 24, 36, 48, 54 [Mbit/sec]` (8 tốc độ 802.11g).
* **Cách crop:** Crop phần Tagged parameters hiển thị rõ cả 2 danh sách tốc độ trên.

---

### CÂU 7: Gói tin chứa TCP SYN (Tải file alice.txt)
* **Tên file cần lưu:** `fig7.png`
* **Bộ lọc Wireshark:**
  ```wireshark
  tcp.flags.syn == 1 && tcp.flags.ack == 0
  ```
* **Gói tin cần chọn:** Gói **No. 474** ($t = 24.811093\,\text{s}$).
* **Vùng cần mở ở khung giữa:**
  * Mở `IEEE 802.11 QoS Data`:
    * `Receiver address: 00:16:b6:f7:1d:51` (AP)
    * `Transmitter address: 00:13:02:d1:b6:4f` (Host)
    * `Destination address: 00:16:b6:f4:eb:a8` (First-hop router)
    * `Source address: 00:13:02:d1:b6:4f` (Host)
  * Mở `Internet Protocol Version 4`:
    * `Source: 192.168.1.109`
    * `Destination: 128.119.245.12`
* **Cách crop:** Crop bao gồm dòng gói No. 474 ở khung danh sách và chi tiết các trường MAC Address 1, 2, 3 cùng IP Source/Destination.

---

### CÂU 8: Gói tin chứa TCP SYNACK
* **Tên file cần lưu:** `fig8.png`
* **Bộ lọc Wireshark:**
  ```wireshark
  tcp.flags.syn == 1 && tcp.flags.ack == 1
  ```
* **Gói tin cần chọn:** Gói **No. 476** ($t = 24.827751\,\text{s}$).
* **Vùng cần mở ở khung giữa:**
  * Mở `IEEE 802.11 QoS Data`:
    * `Receiver address: 91:2a:b0:49:b6:4f` (Host)
    * `Transmitter address: 00:16:b6:f7:1d:51` (AP)
    * `Source address: 00:16:b6:f4:eb:a8` (First-hop router)
  * Mở `Internet Protocol Version 4`:
    * `Source: 128.119.245.12` (Web server)
    * `Destination: 192.168.1.109` (Host)
* **Cách crop:** Crop hiển thị dòng No. 476, 3 địa chỉ MAC ở tầng 802.11 và Source IP ở tầng IP (để chứng minh MAC router khác với Server IP).

---

### CÂU 9: Hai hành động của Host lúc t=49 để ngắt kết nối (DHCP Release & Deauthentication)
* **Tên file cần lưu:** `fig9.png`
* **Bộ lọc Wireshark:**
  ```wireshark
  frame.number >= 1732 && frame.number <= 1736
  ```
* **Gói tin hiển thị:** Sẽ thấy rõ 2 gói chính:
  * **No. 1733** ($t = 49.583609\,\text{s}$): Giao thức DHCP, Info: `DHCP Release` (IP layer action).
  * **No. 1735** ($t = 49.609623\,\text{s}$): Giao thức IEEE 802.11, Info: `Deauthentication` (802.11 layer action).
* **Cách crop:** Crop khung Packet List hiển thị rõ cả 2 gói 1733 và 1735 kèm cột thời gian `Time` ($49.58$s và $49.60$s) và cột `Info`.

---

### CÂU 10: Số lượng gói AUTHENTICATION gửi tới linksys_ses_24086
* **Tên file cần lưu:** `fig10.png`
* **Bộ lọc Wireshark:**
  ```wireshark
  wlan.fc.type_subtype == 0x0b && wlan.da == 00:18:39:f5:ba:bb
  ```
* **Kết quả hiển thị:** Danh sách gồm đúng **6 gói tin**:
  * No. 1740 ($t = 49.638927\,\text{s}$)
  * No. 1741 ($t = 49.639733\,\text{s}$)
  * No. 1742 ($t = 49.640742\,\text{s}$)
  * No. 1744 ($t = 49.642340\,\text{s}$)
  * No. 1746 ($t = 49.645347\,\text{s}$)
  * No. 1749 ($t = 49.649718\,\text{s}$)
* **Cách crop:** Crop toàn bộ khung Packet List hiển thị đủ cả 6 dòng này (thấy rõ tổng cộng 6 gói Authentication).

---

### CÂU 11: Chế độ xác thực (Open hay Key) của Host
* **Tên file cần lưu:** `fig11.png`
* **Gói tin cần chọn:** Gói **No. 1740** (trong kết quả lọc của câu 10).
* **Vùng cần mở ở khung giữa:**
  * Mở: `IEEE 802.11 wireless LAN management frame`
  * Mở: `Fixed parameters`
  * Nhấp chọn dòng: **`Authentication Algorithm: Open System (0)`**.
* **Cách crop:** Crop khung giữa tô sáng dòng `Authentication Algorithm: Open System (0)`.

---

### CÂU 12: Kiểm tra có gói phản hồi Authentication từ AP linksys_ses_24086 không
* **Tên file cần lưu:** `fig12.png`
* **Bộ lọc Wireshark:**
  ```wireshark
  wlan.fc.type_subtype == 0x0b && wlan.sa == 00:18:39:f5:ba:bb
  ```
  *(Hoặc lọc `wlan.fc.type_subtype == 0x0b && wlan.addr == 00:18:39:f5:ba:bb`)*
* **Kết quả hiển thị:**
  * Nếu dùng bộ lọc thứ nhất: Không có gói nào hiển thị (màn hình trống).
  * Nếu dùng bộ lọc thứ hai: Tất cả các gói đều có Source là `00:13:02:d1:b6:4f` (Host) gửi đi, không hề có chiều ngược lại từ AP.
* **Cách crop:** Crop thanh filter bar cùng khung danh sách gói tin (để chứng minh không có frame reply nào từ AP).

---

### CÂU 13: Các gói AUTHENTICATION trao đổi với AP 30 Munroe St lúc t ≈ 63s
* **Tên file cần lưu:** `fig13.png`
* **Bộ lọc Wireshark:**
  ```wireshark
  wlan.fc.subtype == 11 && wlan.fc.type == 0 && wlan.addr == 00:13:02:d1:b6:4f
  ```
* **Kết quả:** Cuộn xuống khu vực $t \approx 63\,\text{s}$, sẽ thấy 4 gói tin quan trọng:
  * **No. 2156** ($t = 63.168087\,\text{s}$): Host $\rightarrow$ AP (Auth Request, Seq 1)
  * **No. 2158** ($t = 63.169071\,\text{s}$): AP $\rightarrow$ Host (Auth Reply, Seq 2, Successful)
  * **No. 2160** ($t = 63.169707\,\text{s}$): Host $\rightarrow$ AP
  * **No. 2164** ($t = 63.170692\,\text{s}$): AP $\rightarrow$ Host
* **Cách crop:** Crop khung Packet List hiển thị rõ 4 dòng gói tin 2156, 2158, 2160, 2164 kèm cột thời gian `Time` và cột `Source/Destination`.

---

### CÂU 14: Thời gian gửi ASSOCIATE REQUEST và ASSOCIATE RESPONSE
* **Tên file cần lưu:** `fig14.png`
* **Bộ lọc Wireshark:**
  ```wireshark
  wlan.fc.subtype < 2 && wlan.fc.type == 0 && wlan.addr == 00:13:02:d1:b6:4f
  ```
* **Kết quả:** Cuộn xuống khu vực $t \approx 63\,\text{s}$, sẽ thấy:
  * **No. 2162** ($t = 63.169910\,\text{s}$): `Association Request` (từ Host gửi tới 30 Munroe St)
  * **No. 2166** ($t = 63.192101\,\text{s}$): `Association Response` (từ 30 Munroe St gửi về Host)
* **Cách crop:** Crop khung Packet List hiển thị rõ 2 dòng gói 2162 và 2166 kèm cột `Time` và `Info`.

---

### CÂU 15: Tốc độ truyền của Host và AP trong quá trình Associate
#### Hình 15.1: Tốc độ của Host (trong AssocReq)
* **Tên file cần lưu:** `fig15_host.png`
* **Gói tin cần chọn:** Gói **No. 2162** (`Association Request`).
* **Vùng cần mở ở khung giữa:**
  * Mở `Tagged parameters`
  * Mở rộng cả:
    * `Tag: Supported Rates 1(B), 2(B), 5.5(B), 11(B), 6, 9, 12, 18 [Mbit/sec]`
    * `Tag: Extended Supported Rates 24, 36, 48, 54 [Mbit/sec]`
* **Cách crop:** Crop phần Tagged parameters của gói 2162 hiển thị đủ 12 tốc độ trên.

#### Hình 15.2: Tốc độ của AP (trong AssocResp)
* **Tên file cần lưu:** `fig15_ap.png`
* **Gói tin cần chọn:** Gói **No. 2166** (`Association Response`).
* **Vùng cần mở ở khung giữa:**
  * Mở `Tagged parameters`
  * Mở rộng cả `Tag: Supported Rates ...` (1, 2, 5.5, 11) và `Tag: Extended Supported Rates ...` (6, 9, 12, 18, 24, 36, 48, 54).
* **Cách crop:** Crop phần Tagged parameters của gói 2166 hiển thị đủ các tốc độ trên.

---

### CÂU 16: Probe Request và Probe Response Frames
#### Hình 16.1: Probe Request
* **Tên file cần lưu:** `fig16_req.png`
* **Bộ lọc Wireshark:**
  ```wireshark
  wlan.fc.type_subtype == 0x04
  ```
* **Gói tin cần chọn:** Gói **No. 1737** (hoặc gói No. 50).
* **Vùng cần mở ở khung giữa:**
  * Mở `IEEE 802.11 Probe Request`:
    * Highlight `Receiver address: Broadcast (ff:ff:ff:ff:ff:ff)`
    * Highlight `Transmitter address: 00:13:02:d1:b6:4f` (Sender)
    * Highlight `BSS Id: Broadcast (ff:ff:ff:ff:ff:ff)`
* **Cách crop:** Crop khung giữa hiển thị rõ 3 địa chỉ MAC này.

#### Hình 16.2: Probe Response
* **Tên file cần lưu:** `fig16_resp.png`
* **Bộ lọc Wireshark:**
  ```wireshark
  wlan.fc.type_subtype == 0x05
  ```
* **Gói tin cần chọn:** Gói **No. 27**.
* **Vùng cần mở ở khung giữa:**
  * Mở `IEEE 802.11 Probe Response`:
    * Highlight `Receiver address: 00:13:02:d1:b6:4f` (Client)
    * Highlight `Transmitter address: Cisco-Li_f7:1d:51 (00:16:b6:f7:1d:51)` (AP)
    * Highlight `BSS Id: Cisco-Li_f7:1d:51 (00:16:b6:f7:1d:51)`
* **Cách crop:** Crop khung giữa hiển thị rõ 3 địa chỉ MAC này.
