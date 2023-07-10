import random
from game import Board
import globals as globals

class Bot13521159(object):
    """
    Bot player
    """

    def __init__(self):
        self.player = None

        """
            TODO: Ganti dengan NIM kalian
        """
        self.NIM = "13521159"

    def set_player_ind(self, p):
        self.player = p

    def get_action(self, board, return_var):

        try:
            location = self.get_input(board)
            if isinstance(location, str):  # for python3
                location = [int(n, 10) for n in location.split(",")]
            move = board.location_to_move(location)
        except Exception as e:
            move = -1

        while move == -1 or move not in board.availables:
            if globals.stop_threads:
                return
            try:
                location = self.get_input(board)
                if isinstance(location, str):  # for python3
                    location = [int(n, 10) for n in location.split(",")]
                move = board.location_to_move(location)
            except Exception as e:
                move = -1
        return_var.append(move) 

    def __str__(self):
        return "{} a.k.a Player {}".format(self.NIM,self.player)
    

    def ubahkekoordinat(self, list, lebar):
        listbaru = []
        for i in list:
            x = i//lebar
            y = i%lebar
            listbaru.append([x,y])
        
        return listbaru
    def cekantara(self,koor,lawan,ada):
        atas = [koor[0]+2,koor[1]]
        bawah = [koor[0]-2,koor[1]]
        kanan = [koor[0],koor[1]+2]
        kiri = [koor[0],koor[1]-2]
        serongkananatas = [koor[0]+2,koor[1]+2]
        serongkiriatas = [koor[0]+2,koor[1]-2]
        serongkananbawah = [koor[0]-2,koor[1]+2]
        serongkiribawah = [koor[0]-2,koor[1]-2]
        atastengah = [koor[0]+1,koor[1]]
        bawahtengah = [koor[0]-1,koor[1]]
        kanantengah = [koor[0],koor[1]+1]
        kiritengah = [koor[0],koor[1]-1]
        serongkananatastengah = [koor[0]+1,koor[1]+1]
        serongkiriatastengah = [koor[0]+1,koor[1]-1]
        serongkananbawahtengah = [koor[0]-1,koor[1]+1]
        serongkiribawahtengah = [koor[0]-1,koor[1]-1]
        if(atas in lawan and atastengah not in ada):
            return True,atastengah
        elif(bawah in lawan and bawahtengah not in ada):
            return True,bawahtengah
        elif(kanan in lawan and kanantengah not in ada):
            return True,kanantengah
        elif(kiri in lawan and kiritengah not in ada):
            return True,kiritengah
        elif(serongkananatas in lawan and serongkananatastengah not in ada):
            return True,serongkananatastengah
        elif(serongkiriatas in lawan and serongkiriatastengah not in ada):
            return True,serongkiriatastengah
        elif(serongkananbawah in lawan and serongkananbawahtengah not in ada):
            return True,serongkananbawahtengah
        elif(serongkiribawah in lawan and serongkiribawahtengah not in ada):
            return True,serongkiribawahtengah
        else:
            return False,-1
    def cek2Lebih(self,koor,lawan,ada,height,width):
        listcek2lebih = [["atas",0],["bawah",0],["kanan",0],["kiri",0],["serongkananatas",0],["serongkiriatas",0],["serongkananbawah",0],["serongkiribawah",0]]
        for i in range(1,5):
            if([koor[0]+i,koor[1]] in lawan):
                listcek2lebih[0][1]+=1
            elif([koor[0]+i,koor[1]] not in lawan ):
                if([koor[0]+i,koor[1]] not in ada and koor[0]+i<height):
                    break
                elif([koor[0]+i,koor[1]] in ada or koor[0]+i>=height):
                    listcek2lebih[0][1]=0
                    break
        for i in range(1,5):
            if([koor[0]-i,koor[1]] in lawan):
                listcek2lebih[1][1]+=1
            elif([koor[0]-i,koor[1]] not in lawan ):
                if([koor[0]-i,koor[1]] not in ada and koor[0]-i>=0):
                    break
                elif([koor[0]-i,koor[1]] in ada or koor[0]-i<0):
                    listcek2lebih[1][1]=0
                    break
        for i in range(1,5):
            if([koor[0],koor[1]+i] in lawan):
                listcek2lebih[2][1]+=1
            elif([koor[0],koor[1]+i] not in lawan ):
                if([koor[0],koor[1]+i] not in ada and koor[1]+i<width):
                    break
                elif([koor[0],koor[1]+i] in ada or koor[1]+i>=width):
                    listcek2lebih[2][1]=0
                    break
        for i in range(1,5):
            if([koor[0],koor[1]-i] in lawan):
                listcek2lebih[3][1]+=1
            elif([koor[0],koor[1]-i] not in lawan ):
                if([koor[0],koor[1]-i] not in ada and koor[1]-i>=0):
                    break
                elif([koor[0],koor[1]-i] in ada or koor[1]-i<0):
                    listcek2lebih[3][1]=0
                    break
        for i in range(1,5):
            if([koor[0]+i,koor[1]+i] in lawan):
                listcek2lebih[4][1]+=1
            elif([koor[0]+i,koor[1]+i] not in lawan ):
                if([koor[0]+i,koor[1]+i] not in ada and koor[0]+i<height and koor[1]+i<width):
                    break
                elif([koor[0]+i,koor[1]+i] in ada or koor[0]+i>=height or koor[1]+i>=width):
                    listcek2lebih[4][1]=0
                    break
        for i in range(1,5):
            if([koor[0]+i,koor[1]-i] in lawan):
                listcek2lebih[5][1]+=1
            elif([koor[0]+i,koor[1]-i] not in lawan ):
                if([koor[0]+i,koor[1]-i] not in ada and koor[0]+i<height and koor[1]-i>=0):
                    break
                elif([koor[0]+i,koor[1]-i] in ada or koor[0]+i>=height or koor[1]-i<0):
                    listcek2lebih[5][1]=0
                    break
        for i in range(1,5):
            if([koor[0]-i,koor[1]+i] in lawan):
                listcek2lebih[6][1]+=1
            elif([koor[0]-i,koor[1]+i] not in lawan ):
                if([koor[0]-i,koor[1]+i] not in ada and koor[0]-i>=0 and koor[1]+i<width):
                    break
                elif([koor[0]-i,koor[1]+i] in ada or koor[0]-i<0 or koor[1]+i>=width):
                    listcek2lebih[6][1]=0
                    break
        for i in range(1,5):
            if([koor[0]-i,koor[1]-i] in lawan):
                listcek2lebih[7][1]+=1
            elif([koor[0]-i,koor[1]-i] not in lawan ):
                if([koor[0]-i,koor[1]-i] not in ada and koor[0]-i>=0 and koor[1]-i>=0):
                    break
                elif([koor[0]-i,koor[1]-i] in ada or koor[0]-i<0 or koor[1]-i<0):
                    listcek2lebih[7][1]=0
                    break
        return listcek2lebih

        
             



    def get_input(self, board : Board) -> str:
        if(board.states == {} or board.states.get(board.height//2*board.width+board.width//2,-1) == -1):
            y = board.width//2
            x = board.height//2
        else:
            listlawan = []
            listkita = []
            for k in range(board.height*board.width):
                if(board.states.get(k,-1) == self.player):
                    listkita.append(k)
                elif(board.states.get(k,-1) != self.player and board.states.get(k,-1) != -1):
                    listlawan.append(k)
            udahada = list(board.states.keys())
            listlawan.sort()
            listlawanbaru = self.ubahkekoordinat(listlawan,board.width)
            listkitabaru =  self.ubahkekoordinat(listkita,board.width)
            udahadabaru = self.ubahkekoordinat(udahada,board.width)
            cek2lebih = []
            for i in range(len(listlawanbaru)):
                ngecekantara,kasusantara = self.cekantara(listlawanbaru[i],listlawanbaru,udahadabaru)
                test = self.cek2Lebih(listlawanbaru[i],listlawanbaru,udahadabaru,board.height,board.width)
                test.sort(key=lambda x: x[1])
                # print(listlawanbaru[i],test)
                if(test[7][1]>0):
                    cek2lebih.append([listlawanbaru[i],test[7]])
                if(ngecekantara):
                    x = kasusantara[0]
                    y = kasusantara[1]
                    
                else:
                    if([0,0] not in udahadabaru):
                        x = 0
                        y = 0
                    elif([0,board.width-1] not in udahadabaru):
                        x = 0
                        y = board.width-1
                    elif([board.height-1,0] not in udahadabaru):
                        x = board.height-1
                        y = 0
                    elif([board.height-1,board.width-1] not in udahadabaru):
                        x = board.height-1
                        y = board.width-1
                    else:
                        countmin = 0
                        while True:
                            randomcek = random.randint(0,len(listkitabaru)-1)
                            koorcek = listkitabaru[randomcek]
                            countmin+=1
                            if(koorcek[0]+1<board.height and [koorcek[0]+1,koorcek[1]] not in udahadabaru):
                                x = koorcek[0]+1
                                y = koorcek[1]
                                break
                            elif(koorcek[0]-1>=0 and [koorcek[0]-1,koorcek[1]] not in udahadabaru):
                                x = koorcek[0]-1
                                y = koorcek[1]
                                break
                            elif(koorcek[1]+1<board.width and [koorcek[0],koorcek[1]+1] not in udahadabaru):
                                x = koorcek[0]
                                y = koorcek[1]+1
                                break
                            elif(koorcek[1]-1>=0 and [koorcek[0],koorcek[1]-1] not in udahadabaru):
                                x = koorcek[0]
                                y = koorcek[1]-1
                                break
                            elif(koorcek[0]+1<board.height and koorcek[1]+1<board.width and [koorcek[0]+1,koorcek[1]+1] not in udahadabaru):
                                x = koorcek[0]+1
                                y = koorcek[1]+1
                                break
                            elif(koorcek[0]+1<board.height and koorcek[1]-1>=0 and [koorcek[0]+1,koorcek[1]-1] not in udahadabaru):
                                x = koorcek[0]+1
                                y = koorcek[1]-1
                                break
                            elif(koorcek[0]-1>=0 and koorcek[1]+1<board.width and [koorcek[0]-1,koorcek[1]+1] not in udahadabaru):
                                x = koorcek[0]-1
                                y = koorcek[1]+1
                                break
                            elif(koorcek[0]-1>=0 and koorcek[1]-1>=0 and [koorcek[0]-1,koorcek[1]-1] not in udahadabaru):
                                x = koorcek[0]-1
                                y = koorcek[1]-1
                                break
                            else:
                                if(countmin>=30):
                                    x = random.randint(0,board.height-1)
                                    y = random.randint(0,board.width-1)
                                    break
                                else:
                                    continue
            for j in range(len(listkitabaru)):
                cek2lebihkitabaru = self.cek2Lebih(listkitabaru[j],listkitabaru,udahadabaru,board.height,board.width)
                cek2lebihkitabaru.sort(key=lambda x: x[1])
                if(cek2lebihkitabaru[7][1]>0):
                    cek2lebih.append([listkitabaru[j],cek2lebihkitabaru[7]])
                            
            cek2lebih.sort(key=lambda x: x[1][1])
            if(cek2lebih!=[]):
                if(cek2lebih[len(cek2lebih)-1][1][0] == "atas"):
                    x = cek2lebih[len(cek2lebih)-1][0][0]+cek2lebih[len(cek2lebih)-1][1][1]+1
                    y = cek2lebih[len(cek2lebih)-1][0][1]
                elif(cek2lebih[len(cek2lebih)-1][1][0] == "bawah"):
                    x = cek2lebih[len(cek2lebih)-1][0][0]-cek2lebih[len(cek2lebih)-1][1][1]-1
                    y = cek2lebih[len(cek2lebih)-1][0][1]
                elif(cek2lebih[len(cek2lebih)-1][1][0] == "kanan"):
                    x = cek2lebih[len(cek2lebih)-1][0][0]
                    y = cek2lebih[len(cek2lebih)-1][0][1]+cek2lebih[len(cek2lebih)-1][1][1]+1
                elif(cek2lebih[len(cek2lebih)-1][1][0] == "kiri"):
                    x = cek2lebih[len(cek2lebih)-1][0][0]
                    y = cek2lebih[len(cek2lebih)-1][0][1]-cek2lebih[len(cek2lebih)-1][1][1]-1
                elif(cek2lebih[len(cek2lebih)-1][1][0] == "serongkananatas"):
                    x = cek2lebih[len(cek2lebih)-1][0][0]+cek2lebih[len(cek2lebih)-1][1][1]+1
                    y = cek2lebih[len(cek2lebih)-1][0][1]+cek2lebih[len(cek2lebih)-1][1][1]+1
                elif(cek2lebih[len(cek2lebih)-1][1][0] == "serongkiriatas"):
                    x = cek2lebih[len(cek2lebih)-1][0][0]+cek2lebih[len(cek2lebih)-1][1][1]+1
                    y = cek2lebih[len(cek2lebih)-1][0][1]-cek2lebih[len(cek2lebih)-1][1][1]-1
                elif(cek2lebih[len(cek2lebih)-1][1][0] == "serongkananbawah"):
                    x = cek2lebih[len(cek2lebih)-1][0][0]-cek2lebih[len(cek2lebih)-1][1][1]-1
                    y = cek2lebih[len(cek2lebih)-1][0][1]+cek2lebih[len(cek2lebih)-1][1][1]+1
                elif(cek2lebih[len(cek2lebih)-1][1][0] == "serongkiribawah"):
                    x = cek2lebih[len(cek2lebih)-1][0][0]-cek2lebih[len(cek2lebih)-1][1][1]-1
                    y = cek2lebih[len(cek2lebih)-1][0][1]-cek2lebih[len(cek2lebih)-1][1][1]-1


                        
        return f"{x},{y}"