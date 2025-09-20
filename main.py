import requests
import os

year = "2023"
section = "M"
start_month = 1
end_month = 12
start_number = 10001
end_number = 11000

for month in range(start_month, end_month + 1):
    month_str = f"{month:02d}"
    folder_name = f"{year}{month_str}"
    
    # Create folder if it doesn't exist
    os.makedirs(folder_name, exist_ok=True)
    
    consecutive_failures = 0  # reset for each month

    for num in range(start_number, end_number + 1):
        nokp = f"{year}{month_str}{section}{num}"
        url = f"https://academic.utm.my/UGStudent/PhotoStudent.ashx?nokp={nokp}"
        response = requests.get(url)

        if response.status_code == 200 and len(response.content) > 100:
            consecutive_failures = 0  # reset on success
            file_path = os.path.join(folder_name, f"{nokp}.jpg")
            with open(file_path, "wb") as f:
                f.write(response.content)
            print(f"Downloaded {file_path}")
        else:
            consecutive_failures += 1
            print(f" Failed to download {nokp}.jpg ({consecutive_failures} fails in a row)")
            
            if consecutive_failures > 4:
                print(f" More than 4 consecutive failures — moving to next month.")
                break
