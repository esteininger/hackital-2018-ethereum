class Google:
    def __init__(self):
        pass

    def getFAQs(self):
        spreadsheetID = '1Lu-ph3_mNysCfFbQB2YCIghgfyqFka1fm50HSNcK-mU'
        metaID = '1Lu-ph3_mNysCfFbQB2YCIghgfyqFka1fm50HSNcK-mU'
        url = 'https://sheets.googleapis.com/v4/spreadsheets/'+spreadsheetID+'/developerMetadata/'+metaID
        return url
