from ClientUpdate import DVUpload

DV = DVUpload("diago1234","Diagogoogle$4","https://revmediciego.sld.cu/index.php/mediciego/")
DV.login()
DV.make_repo()
DV.upload("thumb.png")