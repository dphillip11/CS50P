
filename = input("file name: ").lower().strip()
try:
    filename, suffix = filename.rsplit(sep = ".", maxsplit = 1)
except:
    suffix = " "

match suffix:

    case "gif" |  "jpeg" | "png" :
        print(f"image/{suffix}")

    case "jpg":
        print("image/jpeg")

    case "txt":
        print("text/plain")

    case "zip" | "pdf":
        print(f"application/{suffix}")

    case _:
        print("application/octet-stream")
