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
    # def cek2Lebih(self,koor,lawan,ada):
    #     buatngecek = 1
    #     listcek2lebih = [["atas",0],["bawah",0],["kanan",0],["kiri",0],["serongkananatas",0],["serongkiriatas",0],["serongkananbawah",0],["serongkiribawah",0]]
    #     while(buatngecek<=4):
    #         if([koor[0]+buatngecek,koor[1]] in lawan and buatngecek-listcek2lebih[0][1]==1):
    #             if([koor[0]+buatngecek+1,koor[1]] not in lawan and [koor[0]+buatngecek+1,koor[1]] in ada):
    #                 listcek2lebih[0][1]=0
    #             else:
    #                 listcek2lebih[0][1]+=1
    #         if([koor[0]-buatngecek,koor[1]] in lawan and buatngecek-listcek2lebih[1][1]==1):
    #             if([koor[0]-buatngecek-1,koor[1]] not in lawan and [koor[0]-buatngecek-1,koor[1]] in ada):
    #                 listcek2lebih[1][1]=0
    #             else:
    #                 listcek2lebih[1][1]+=1
    #         if([koor[0],koor[1]+buatngecek] in lawan and buatngecek-listcek2lebih[2][1]==1):
    #             if([koor[0],koor[1]+buatngecek+1] not in lawan and [koor[0],koor[1]+buatngecek+1] in ada):
    #                 listcek2lebih[2][1]=0
    #             else:
    #                 listcek2lebih[2][1]+=1
    #         if([koor[0],koor[1]-buatngecek] in lawan and buatngecek-listcek2lebih[3][1]==1):
    #             if([koor[0],koor[1]-buatngecek-1] not in lawan and [koor[0],koor[1]-buatngecek-1] in ada):
    #                 listcek2lebih[3][1]=0
    #             else:
    #                 listcek2lebih[3][1]+=1
    #         if([koor[0]+buatngecek,koor[1]+buatngecek] in lawan and buatngecek-listcek2lebih[4][1]==1):
    #             if([koor[0]+buatngecek+1,koor[1]+buatngecek+1] not in lawan and [koor[0]+buatngecek+1,koor[1]+buatngecek+1] in ada):
    #                 listcek2lebih[4][1]=0
    #             else:
    #                 listcek2lebih[4][1]+=1
    #         if([koor[0]+buatngecek,koor[1]-buatngecek] in lawan and buatngecek-listcek2lebih[5][1]==1):
    #             if([koor[0]+buatngecek+1,koor[1]-buatngecek-1] not in lawan and [koor[0]+buatngecek+1,koor[1]-buatngecek-1] in ada):
    #                 listcek2lebih[5][1]=0
    #             else:
    #                 listcek2lebih[5][1]+=1
    #         if([koor[0]-buatngecek,koor[1]+buatngecek] in lawan and buatngecek-listcek2lebih[6][1]==1):
    #             if([koor[0]-buatngecek-1,koor[1]+buatngecek+1] not in lawan and [koor[0]-buatngecek-1,koor[1]+buatngecek+1] in ada):
    #                 listcek2lebih[6][1]=0
    #             else:
    #                 listcek2lebih[6][1]+=1
    #         if([koor[0]-buatngecek,koor[1]-buatngecek] in lawan and buatngecek-listcek2lebih[7][1]==1):
    #             if([koor[0]-buatngecek-1,koor[1]-buatngecek-1] not in lawan and [koor[0]-buatngecek-1,koor[1]-buatngecek-1] in ada):
    #                 listcek2lebih[7][1]=0
    #             else:
    #                 listcek2lebih[7][1]+=1
    #         buatngecek+=1
    #     listcek2lebih.sort(key=lambda x: x[1])
    #     nantidicek = False
    #     if(listcek2lebih[7][1]>=1):
    #         nantidicek = True
    #     return listcek2lebih,nantidicek

             



    def get_input(self, board : Board) -> str:
        """
            Parameter board merepresentasikan papan permainan. Objek board memiliki beberapa
            atribut penting yang dapat menjadi acuan strategi.
            - board.height : int (x) -> panjang papan
            - board.width : int (y) -> lebar papan
            Koordinat 0,0 terletak pada kiri bawah

            [x,0] [x,1] [x,2] . . . [x,y]                               
            . . . . . . . . . . . . . . .  namun perlu diketahui        Contoh 4x4: 
            . . . . . . . . . . . . . . .  bahwa secara internal        11 12 13 14 15
            . . . . . . . . . . . . . . .  sel-sel disimpan dengan  =>  10 11 12 13 14
            [2,0] [2,1] [2,2] . . . [2,y]  barisan interger dimana      5  6  7  8  9
            [1,0] [1,1] [1,2] . . . [1,y]  kiri bawah adalah nol        0  1  2  3  4
            [0,0] [0,1] [0,2] . . . [0,y]          
                                 
            - board.states : dict -> Kondisi papan. 
            Key dari states adalah integer sel (0,1,..., x*y)
            Value adalah integer 1 atau 2:
            -> 1 artinya sudah diisi player 1
            -> 2 artinya sudah diisi player 2

            TODO: Tentukan x,y secara greedy. Kembalian adalah sebuah string "x,y"
        """
        #WIDTH BUAT KESAMPING
        #HEIGHT BUAT KEATAS BAWAH
        #Y ITU YANG ATAS
        #X ITU YANG SAMPING
        """
       0       1       2       3       4       5       6       7       8       9      10

   4   _       _       _       _       _       _       _       _       _       _       _


   3   _       _       _       _       _       _       _       _       _       _       _


   2   _       _       _       _       _       O       _       _       _       _       _


   1   _       _       X       _       _       _       _       _       _       _       _


   0   _       _       _       _       _       _       _       _       _       _       _
   """
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
            for i in range(len(listlawanbaru)):
                ngecekantara,kasusantara = self.cekantara(listlawanbaru[i],listlawanbaru,udahadabaru)
                # cek2lebih,dicek = self.cek2Lebih(listlawanbaru[i],listlawanbaru,udahadabaru)
                # print(listlawanbaru[i],":",cek2lebih)
                # print(dicek)
                # if(dicek):
                #     for i in range(len(cek2lebih)-1,-1,-1):
                #         if(cek2lebih[i][0]=="atas" and [listlawanbaru[i][0]+cek2lebih[i][1]+1,listlawanbaru[i][1]] not in udahadabaru):
                #             if(listlawanbaru[i][0]+cek2lebih[i][1]+1<board.height):
                #                 x = listlawanbaru[i][0]+cek2lebih[i][1]+1
                #                 y = listlawanbaru[i][1]
                #                 break
                #         elif(cek2lebih[i][0]=="bawah" and [listlawanbaru[i][0]-cek2lebih[i][1]-1,listlawanbaru[i][1]] not in udahadabaru):
                #             if(listlawanbaru[i][0]-cek2lebih[i][1]-1>=0):
                #                 x = listlawanbaru[i][0]-cek2lebih[i][1]-1
                #                 y = listlawanbaru[i][1]
                #                 break
                #         elif(cek2lebih[i][0]=="kanan" and [listlawanbaru[i][0],listlawanbaru[i][1]+cek2lebih[i][1]+1] not in udahadabaru):
                #             if(listlawanbaru[i][1]+cek2lebih[i][1]+1<board.width):
                #                 x = listlawanbaru[i][0]
                #                 y = listlawanbaru[i][1]+cek2lebih[i][1]+1
                #                 break
                #         elif(cek2lebih[i][0]=="kiri" and [listlawanbaru[i][0],listlawanbaru[i][1]-cek2lebih[i][1]-1] not in udahadabaru):
                #             if(listlawanbaru[i][1]-cek2lebih[i][1]-1>=0):
                #                 x = listlawanbaru[i][0]
                #                 y = listlawanbaru[i][1]-cek2lebih[i][1]-1
                #                 break
                #         elif(cek2lebih[i][0]=="serongkananatas" and [listlawanbaru[i][0]+cek2lebih[i][1]+1,listlawanbaru[i][1]+cek2lebih[i][1]+1] not in udahadabaru):
                #             if(listlawanbaru[i][0]+cek2lebih[i][1]+1<board.height and listlawanbaru[i][1]+cek2lebih[i][1]+1<board.width):
                #                 x = listlawanbaru[i][0]+cek2lebih[i][1]+1
                #                 y = listlawanbaru[i][1]+cek2lebih[i][1]+1
                #                 break
                #         elif(cek2lebih[i][0]=="serongkiriatas" and [listlawanbaru[i][0]+cek2lebih[i][1]+1,listlawanbaru[i][1]-cek2lebih[i][1]-1] not in udahadabaru):
                #             if(listlawanbaru[i][0]+cek2lebih[i][1]+1<board.height and listlawanbaru[i][1]-cek2lebih[i][1]-1>=0):
                #                 x = listlawanbaru[i][0]+cek2lebih[i][1]+1
                #                 y = listlawanbaru[i][1]-cek2lebih[i][1]-1
                #                 break
                #         elif(cek2lebih[i][0]=="serongkananbawah" and [listlawanbaru[i][0]-cek2lebih[i][1]-1,listlawanbaru[i][1]+cek2lebih[i][1]+1] not in udahadabaru):
                #             if(listlawanbaru[i][0]-cek2lebih[i][1]-1>=0 and listlawanbaru[i][1]+cek2lebih[i][1]+1<board.width):
                #                 x = listlawanbaru[i][0]-cek2lebih[i][1]-1
                #                 y = listlawanbaru[i][1]+cek2lebih[i][1]+1
                #                 break
                #         elif(cek2lebih[i][0]=="serongkiribawah" and [listlawanbaru[i][0]-cek2lebih[i][1]-1,listlawanbaru[i][1]-cek2lebih[i][1]-1] not in udahadabaru):
                #             if(listlawanbaru[i][0]-cek2lebih[i][1]-1>=0 and listlawanbaru[i][1]-cek2lebih[i][1]-1>=0):
                #                 x = listlawanbaru[i][0]-cek2lebih[i][1]-1
                #                 y = listlawanbaru[i][1]-cek2lebih[i][1]-1
                #                 break
                #         elif(ngecekantara):
                #             x = kasusantara[0]
                #             y = kasusantara[1]
                #             break
                if(ngecekantara):
                    x = kasusantara[0]
                    y = kasusantara[1]
                    break
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
                            

                        
        return f"{x},{y}"