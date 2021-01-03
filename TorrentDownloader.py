import requests
import subprocess
import sys

# from operator import itemgetter
def main():
    movie_name=input("Enter the movie name which you want to stream \n")
    # you can make use of this free torrent api ,he also have few other apis which are absolutely free
    base_url=f"https://api.sumanjay.cf/torrent/?query={movie_name}"
    torrent_results=requests.get(base_url).json()
    index=1
    magnet=[]
    val=1
    #get all the movies/shows you would like to download
    for result in torrent_results:
        if 'movie' in result['type'].lower():
            print(index,"-->",result['name'],"------------->",result['size'])
            index+=1
            magnet.append(result['magnet'])
    print("\n\n")
    # choose your preferred size and title by the index numbers shown above

    choice=int(input("Enter the index number of the movie you want to watch"))
    magnet_link= magnet[choice-1]

    download=False
    #choose one to download and other to stream online  in webpage or VLC
    users_choice=int(input("Enter 1 to download or 2 to stream "))

    if users_choice==1:
         #downloading
         download=True
    elif users_choice==2:
        download=False
        #wait bro lemme open VLC for you,man it;s kind of not supporting in my laptop ,you can check in your systems.
    else:
        print("Bhai ! maaro mujhe maaro ,can't you fucking choose betweeen 2 numbers")
    handler(magnet_link,download)


def handler(magnet_link,download):
    cmd=[]
    cmd.append("webtorrent")
    cmd.append(magnet_link)
    if  not download:
        cmd.append("--vlc")    
    if sys.platform.startswith("win"):
        subprocess.call(cmd,shell=True)
main()       


# code by Bille Giriteja (@giriteja94495)
