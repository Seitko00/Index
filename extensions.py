file_name = input("fine name: ").strip().lower()

types = {
    ".gif" : "image/gif",
    ".jpg" : "image/jpeg",
    ".jpeg" : "image/jpeg",
    ".png" : "image/png",
    "pdf" : "application/pdf",
    ".txt" : "text/plain",
    ".zip" : "application/zip"
}

for ext, media in types.items():
    if file_name.endswith(ext):
        print(media)
        break
else:
        print("application/octet-stream")
