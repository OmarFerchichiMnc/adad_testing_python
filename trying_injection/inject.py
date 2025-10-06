import paramiko

host = "example.com"
port = 22
username = "username"
password = "password"

local_file = "/path/to/local/file.txt"
remote_path = "/remote/directory/file.txt"

# Connect
transport = paramiko.Transport((host, port))
transport.connect(username=username, password=password)

sftp = paramiko.SFTPClient.from_transport(transport)

# Upload
sftp.put(local_file, remote_path)
print("File uploaded successfully!")

# Close
sftp.close()
transport.close()
