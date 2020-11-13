def cutPhotoPath(photopath):
    fullpath=photopath.split("\\")
    le=len(fullpath)
    relativepath="D:\RICS2016\KAJIADOKRBSHAPEFILES\PHOTOS"
    finalpath=  relativepath+"\\"+fullpath[le-2]+"\\"+fullpath[le-1]
    return finalpath