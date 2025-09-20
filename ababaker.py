import requests
for i in range(1,550):
    nokp = f"202309M10{i:03d}" 
    url = f"https://academic.utm.my/UGStudent/PhotoStudent.ashx?nokp={nokp}"
    response = requests.get(url)

    if response.status_code == 200 and len(response.content) > 100:
        with open(f"{nokp}.jpg", "wb") as f:
            f.write(response.content)
            print(f"Downloaded {nokp}.jpg")
    else:
            print(f"Failed to download {nokp}.jpg")
