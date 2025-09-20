import requests
import os

year = "2022"
month = "10"   
section = "M" 
start_number = 10001
end_number = 11000

folder_name = os.path.join(year, f"{month}_Male")
os.makedirs(folder_name, exist_ok=True)

consecutive_failures = 0
print(f"\nStarting downloads for {folder_name}...")

for num in range(start_number, end_number + 1):
    nokp = f"{year}{month}{section}{num}"
    url = f"https://academic.utm.my/UGStudent/PhotoStudent.ashx?nokp={nokp}"

    response = requests.get(url)

    if response.status_code == 200 and len(response.content) > 100:
        consecutive_failures = 0  # reset on success
        file_path = os.path.join(folder_name, f"{nokp}.jpg")
        with open(file_path, "wb") as f:
            f.write(response.content)

        print(f"✅ Downloaded {file_path}")
    else:
        print(f"❌ Failed to download {nokp}.jpg")
        consecutive_failures += 1

        if consecutive_failures > 4:
            print("⚠️ Too many consecutive failures. Stopping early.")
            break
