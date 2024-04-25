from google_images_download import google_images_download

def download_images(query, limit):
    response = google_images_download.googleimagesdownload()
    arguments = {"keywords": query, "limit": limit, "print_urls": True}
    paths = response.download(arguments)
    print(paths)

if __name__ == "__main__":
    query = input("Enter your search query: ")
    limit = int(input("Enter the number of images to download: "))
    download_images(query, limit)
