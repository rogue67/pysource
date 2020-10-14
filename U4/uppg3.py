import requests
import os
from time import perf_counter as pc
import concurrent.futures as future

imgs = [
    "http://www.it.uu.se/edu/course/homepage/prog2/h20/docs/assignments/helpfiles/img/1.jpg",
    "http://www.it.uu.se/edu/course/homepage/prog2/h20/docs/assignments/helpfiles/img/2.jpg",
    "http://www.it.uu.se/edu/course/homepage/prog2/h20/docs/assignments/helpfiles/img/3.jpg",
    "http://www.it.uu.se/edu/course/homepage/prog2/h20/docs/assignments/helpfiles/img/4.jpg",
    "http://www.it.uu.se/edu/course/homepage/prog2/h20/docs/assignments/helpfiles/img/5.jpg",
    "http://www.it.uu.se/edu/course/homepage/prog2/h20/docs/assignments/helpfiles/img/6.jpg",
    "http://www.it.uu.se/edu/course/homepage/prog2/h20/docs/assignments/helpfiles/img/7.jpg",
    "http://www.it.uu.se/edu/course/homepage/prog2/h20/docs/assignments/helpfiles/img/8.jpg",
    "http://www.it.uu.se/edu/course/homepage/prog2/h20/docs/assignments/helpfiles/img/9.jpg",
    "http://www.it.uu.se/edu/course/homepage/prog2/h20/docs/assignments/helpfiles/img/10.jpg",
    "http://www.it.uu.se/edu/course/homepage/prog2/h20/docs/assignments/helpfiles/img/11.jpg",
    "http://www.it.uu.se/edu/course/homepage/prog2/h20/docs/assignments/helpfiles/img/12.jpg",
    "http://www.it.uu.se/edu/course/homepage/prog2/h20/docs/assignments/helpfiles/img/13.jpg",
    "http://www.it.uu.se/edu/course/homepage/prog2/h20/docs/assignments/helpfiles/img/14.jpg",
    "http://www.it.uu.se/edu/course/homepage/prog2/h20/docs/assignments/helpfiles/img/15.jpg"
]

def download(url):
    try:
        file = requests.get(url).content
        with open("img.jpg", "wb") as f:
            f.write(file)
        size = round(os.path.getsize("img.jpg") / 1_000_000, 2)
        print("Downloaded file ({} MB)".format(size))
    except:
        print("filen gick ej att hämta")
    

if __name__ == "__main__":
    start = pc()
    for item in imgs:
        download(item)
    print("tidsåtgång för seriell nedladdning: {}".format(pc() - start) )

    start = pc()
    with future.ThreadPoolExecutor() as ex:
        ex.map(download, imgs)
    end = pc()
    print(f"Tidsåtgång för paralell nedladdning {round(end-start, 2)} seconds") 
   