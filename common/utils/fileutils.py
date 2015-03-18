__company__ = 'Boulder Environmental Sciences and Technology'
__project__ = ''
__author__ = 'Y. Shao'
__created__ = '2/24/2015' '1:44 PM'

def fetch_archive():

    larc=sorted(larc,key=name)
    larc=find_range(larc)

    fetch(larc)
    decompress(larc)


if __name__ == '__main__':
    ""
