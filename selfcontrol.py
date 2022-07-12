from datetime import datetime

end_time = datetime(2022, 1, 1, 20)
#tahun, bulan, tanggal, jam

sites_to_block = ['www.facebook.com'] #sites yang diblock

hosts_path = r"C:\Windows\System32\drivers\etc\hosts"

redirect = "127.0.0.1"

def block_sites():
    if datetime.now () < end_time:
        print("block sites")
        with open(hosts_path, 'r+') as hostsfile:
            hosts_content = hostsfile.read()
            for site in sites_to_block:
                if site not in hosts_content:
                    hostsfile.write(redirect + " " + site + "\n")
    else:
        print("Unblock sites")
        with open(hosts_path, 'r+') as hostsfile:
            lines = hostsfile.readlines()
            hostsfile.seek(0)
            for line in lines:
                if not any(site in line for site in sites_to_block):
                    hostsfile.write(line)
            hostsfile.truncate()

if __name__ == "__main__":
    block_sites()