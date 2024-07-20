import requests
import sessioncontroller


def getLatest() -> list:
    res = sessioncontroller.get(f'Items/Latest', {"includeItemTypes": "MusicAlbum", "limit": 10})
    return res.json()


def getLibs() -> list:
    res = sessioncontroller.get('UserViews')
    reslist = []
    try:
        for item in res.json()['items']:
            if item['ConnectionType'] == 'music':
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
    res = sessioncontroller.get(f'Items?parentId={ItemId}&recursive=true&includeItemTypes=MusicAlbum')
    return res.json()['Items']


def getItemDetails(ItemId: str) -> dict:
    res = sessioncontroller.get(f'Items/{ItemId}')
    return res.json()


def getAlbumTracks(AlbumId: str) -> list:
    res = sessioncontroller.get(f'Items?parentId={AlbumId}')
    return res.json()


def getImageUrl(ItemId: str) -> str:
    return f'{sessioncontroller.serverIp}/Items/{ItemId}/Images/Primary/0'
