# Apply Access

A login is required to access the HPC cluster of the University.
Use your student or employee email address of the university to sign up for the account.

- Fill the [Application Form](https://nettskjema.no/a/403264), or scan the QR code.

  ![QR code](images/qr2apply.png)
  <!-- <img src="images/qr2apply.png" alt="drawing" width="200"/> -->

- Feel free to reach out to us via email at `hpc@kristiania.no` to request HPC special access for a project, need additional storage access, or require dedicated execution time on a node.

## Accessing Resources On and Off Campus

In order to seamlessly utilize resources, whether on or off campus, it is essential to understand the distinct methods for connectivity.

### On-Campus Connectivity

When physically present within the campus premises and connected to either the `EGMS` or `Student` network, you can effortlessly access High-Performance Computing (HPC) resources. Specifically, a direct Secure Shell (SSH) connection to the HPC login node can be established using the following command:

```
ssh <username>@<Domain name or IP of HPC>
```

Here, the IP address or domain name corresponds to the IP/hostname of the HPC login node.

### Off-Campus Connectivity

When operating from a remote location, accessing resources off campus requires specific procedures. Here are the guidelines for both students and employees:The off-campus VPN (Virtual Private Network) provides secure connectivity from anywhere in the world. To use this service:

**For students (follow the instruction - [link](https://www.kristiania.no/en/for-students/it-support/vpn/)):**

- Visit `https://vpnstudent.kristiania.no`,
- Download and install ‘global protect’ app,
- Go to the app and enter `vpnstudent.kristiania.no` in the portal address,
- Click ‘connect’ and enter username and password to login,
- Connected!

**For employees and PhD students (follow the instruction - [link](https://www.kristiania.no/for-ansatte/it/vpn-ansatt/)):**

- Visit `saml-intern.kristiania.no`,
- Download and install `global protect` app,
- Open the app and enter `saml-intern.kristiania.no` in the portal address,
- Click ‘connect’ and enter username and password to login,
- Connected!

Notes: Linux user, follow the instruction - [link](https://docs.paloaltonetworks.com/globalprotect/5-1/globalprotect-app-user-guide/globalprotect-app-for-linux).
