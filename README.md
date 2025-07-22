# PermiControl

**PermiControl** is a Linux user and permission management tool that simplifies system administration by providing both command-line and graphical interfaces. It helps admins manage users, groups, and file permissions securely and efficiently.

---

## Features

- Add, delete, and modify Linux users and groups
- Change file and directory ownership and permissions
- View audit logs of all changes made through the tool
- Bulk operations for user and permission management
- User-friendly GUI for quick and easy administration
- CLI interface for advanced users and automation
- Role-based access control for tool usage (planned)

---

## Installation

### Prerequisites

- Python 3.x
- Linux operating system (tested on Ubuntu/Debian)
- Python `venv` module (for virtual environment)

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/PermiControl.git
   cd PermiControl
2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
