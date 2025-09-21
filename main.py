import requests
import os
import csv

def download_photo(ic, output_folder="photos"):
    os.makedirs(output_folder, exist_ok=True)

    url = f"https://academic.utm.my/UGStudent/PhotoStudent.ashx?nokp={ic}"
    res = requests.get(url)

    if res.status_code == 200 and len(res.content) > 100:

        filepath = os.path.join(output_folder, f"{ic}.jpg")
        with open(filepath, "wb") as f:
            f.write(res.content)
        print(f"OK Downloaded {ic}.jpg")
        return filepath
    else:
        print(f"X Not found: {ic}")
        return None

def batch_download(prefix, start, end, output_folder="photos", csv_file="results.csv"):

    with open(csv_file, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["IC", "Status", "Filepath"])

        for num in range(start, end + 1):
            ic = f"{prefix}{num}" 
            filepath = download_photo(ic, output_folder)

            if filepath:
                writer.writerow([ic, "Downloaded", filepath])
            else:
                writer.writerow([ic, "Not Found", ""])

            ###  stop if too many failing in a raw
            if not filepath and num > start + 300:
                print("Too many missing ICs, stopping batch.")
                break

if __name__ == "__main__":

    prefix = ["202403M", "202410M", "202503M"]   # here so can be adjusted for the batch
    folders_name = ["2024/03", "2024/10", "2025/03"]

    start = 10001
    end = 10500  

    for pre, name in zip(prefix, folders_name):
        batch_download(pre, start, end, output_folder=name)
