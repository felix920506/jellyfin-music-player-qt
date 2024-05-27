import requests
import sessioncontroller


def getLatest() -> list:
    pass


def getLibs() -> list:
    res = sessioncontroller.get('UserViews')
    reslist = []
    try:
        for item in res.json()['items']:
            entry = {
                'Id': item['Id'],
                'Name': item['Name'],
                'Image': getImageUrl(item['Id'])
            }
            reslist.append(entry)

    except:
        reslist = []

    return reslist

def getLibAlbums(ItemId: str) -> list:


def getAlbumInfo(ItemId: str) -> dict:
    pass


def getTrackInfo(ItemId: str) -> dict:
    pass


def getImageUrl(ItemId: str) -> str:
    pass