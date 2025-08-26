# 💬 NiceGUI Chat App

This is a simple **real-time chat application** built with [NiceGUI](https://nicegui.io/).  
Each user gets a unique avatar (generated with [RoboHash](https://robohash.org/)) and can send messages in a shared chat room.

---

## 🚀 Features
- 🆔 Unique User IDs with random avatars  
- 💬 Send and display messages in a chat interface  
- ⚡ Live UI refresh using `@ui.refreshable`  
- 📱 Responsive design with NiceGUI layouts  

---

## 📂 Project Structure
├── app.py                           # Main chat application
├── requirements.txt                 # Python dependencies
└── README.md                        # Project documentation

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/your-username/nicegui-chat.git
cd nicegui-chat

### 2. Create a virtual environment

python -m venv .venv
source .venv/bin/activate   # On Linux/Mac
.venv\Scripts\activate      # On Windows

### 3. Install dependencies
pip install -r requirements.txt

### 4. Run the app
python app.py

The app will start on:
👉 http://localhost:8080


📝 Usage

Open the app in your browser.
Type your message in the input box.
Press Enter to send.
Messages appear with your unique avatar.


📦 Dependencies

NiceGUI
uuid(standard Python library)





