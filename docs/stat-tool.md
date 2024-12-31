# Statistical software

This documentation page provides a comprehensive guide on how to use the software installed on our Kristiania-HPC. It also includes instructions for accessing the software on a Kristiania-HPC cluster via SSH.

---

## 1. Accessing Stata on HPC

### SSH login

Log in to the HPC cluster via SSH:

```bash
ssh username@hpc_server_ip
```

### Launch Stata

To run Stata in interactive mode:

```bash
stata
```

To run Stata in batch mode, create a `.do` file and execute it:

```bash
stata -b do script.do
```

This will execute the commands in `script.do` and save the output to `script.log`.

### Forward GUI for Stata (Optional)

If you want to use Stata's graphical interface, enable X11 forwarding:

1. Install an X server on your local machine:

   - **For macOS:** Install [XQuartz](https://www.xquartz.org/).
   - **For Windows:** Use an SSH client with X11 support, such as [MobaXterm](https://mobaxterm.mobatek.net/) or [Xming](https://sourceforge.net/projects/xming/).
   - **For Linux:** Ensure `xauth` and an X server (e.g., `xorg`) are installed.

2. Connect to the HPC with X11 forwarding:

   ```bash
   ssh -X username@hpc_server_ip
   ```

3. Launch Stata GUI:
   ```bash
   xstata
   ```

---

## 2. Accessing RStudio on HPC

### Set Up SSH Tunnel for RStudio

To securely access RStudio Server, create an SSH tunnel:

```bash
ssh -L 8787:localhost:8787 username@hpc_server_ip
```

- Replace `username` with your HPC username.
- Replace `hpc_server_ip` with the HPC cluster's IP address.

This forwards the HPC's RStudio port (`8787`) to your local machine.

### Access RStudio in Your Browser

1. Open a web browser on your local machine.
2. Navigate to:
   ```
   http://localhost:8787
   ```
3. Log in using your HPC credentials.

---

## 3. [Optional] Mounting HPC Storage to Your Local System

You can mount HPC storage to your local system for easy file access.

### macOS

1. Install **macFUSE**:
   - Download and install from [macFUSE](https://osxfuse.github.io/).
2. Use `sshfs` to mount the HPC storage:
   ```bash
   brew install sshfs
   mkdir ~/hpc_mount
   sshfs username@hpc_server_ip:/path/to/hpc/storage ~/hpc_mount
   ```

### Windows

1. Install **WinFsp** and **SSHFS-Win**:
   - Download and install from [WinFsp](https://github.com/winfsp/winfsp) and [SSHFS-Win](https://github.com/billziss-gh/sshfs-win/releases).
2. Mount the HPC storage using File Explorer:
   - Open `This PC`, click `Map Network Drive`, and use the address:
     ```
     \sshfs\username@hpc_server_ip\path\to\hpc\storage
     ```

### Linux

1. Ensure `sshfs` is installed:
   ```bash
   sudo apt install sshfs
   ```
2. Mount the HPC storage:
   ```bash
   mkdir ~/hpc_mount
   sshfs username@hpc_server_ip:/path/to/hpc/storage ~/hpc_mount
   ```

---

## 4. [Alternative to 3] Accessing Remote Folders Using `VS Code`

You can use Visual Studio Code's Remote - SSH extension to access HPC remote folders seamlessly.

### Steps to Configure

1. **Install VS Code:**

   - Download and install Visual Studio Code from [code.visualstudio.com](https://code.visualstudio.com/).

2. **Install the Remote - SSH Extension:**

   - Open VS Code.
   - Go to the Extensions view (`Ctrl+Shift+X` or `Cmd+Shift+X` on macOS).
   - Search for "Remote - SSH" and install the extension.

3. **Configure SSH in VS Code:**

   - Open the Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P` on macOS).
   - Type "Remote-SSH: Add New SSH Host" and select it.
   - Enter the SSH command to connect to the HPC, e.g.:
     ```
     ssh username@hpc_server_ip
     ```
   - Choose the SSH configuration file where this should be saved (usually `~/.ssh/config`).

4. **Connect to the HPC:**

   - Open the Command Palette.
   - Type "Remote-SSH: Connect to Host" and select your HPC entry.
   - A new VS Code window will open, connected to the HPC.

5. **Access Remote Folders:**
   - In the new window, use the File Explorer to browse and edit remote files.

---

For assistance, contact your HPC system administrator.

```{eval-rst}
.. autosummary::
    :toctree: generated
```
