from tkinter import *
from tkinter import messagebox,ttk
import tempfile
import random #pour la facture
from time import strftime
from PIL import ImageTk,Image
import os#imprime

class SuperMarche:
    def __init__(self, root):
        self.root=root
        self.root.title("Super Marché")
        self.root.geometry("1920x1040+0+0")#-------------taille de la fenetre quant elle saffiche"

        title=Label(self.root,text="Super Marché Soulaima jaidane",font=("Algerian",45),bg="cyan",fg="black" )
        title.pack(side=TOP,fill=X)#------------bechh l title Super Marché Soulaima jaidane yatla3 men fou9

        def heure():#--------------fonction heure instantané
            heur=strftime("%H:%M:%S")
            lblheure.config(text=heur)
            lblheure.after(1000,heure)

        lblheure=Label(self.root,text="HH:MM:SS",font=("times new roman",15,"bold"),bg="cyan",fg="black")
        lblheure.place(x=0,y=25,width=120,height=45)#----------pour le background de l'heure

        heure()

        #---declaration des variables --------
        self.c_nom=StringVar()
        self.c_phon=StringVar()

        self.n_factu=StringVar()
        z=random.randint(1000,9999)#car laa facture est random
        self.n_factu.set(z)

        self.c_email=StringVar()
        self.rech_factu=StringVar()
        self.produit=StringVar()
        self.qte=IntVar()
        self.prix=IntVar()
        self.totalbrute=StringVar()
        self.taxe=StringVar()
        self.totalnet=StringVar()

        #__LISTE CATEGORIE
        self.list_categorie=["Selection","Vetement","Soin","Télephone"]

        #__LISTE SOUS CATEGORIE VETEMENT
        self.list_souscategorieVetemnt=["Pantalon","T-Shirt","Robe"]

        self.pantalon=["Levis","Bershka","Pull&Bear"]
        self.price_levis=50000
        self.price_Bershka=10000
        self.price_PullBear=30000

        self.t_shirt=["Polo","Zara","Jack&Jones"]
        self.price_polo=22500
        self.price_Zara=23550
        self.price_jack_jones=39600

        self.Robe=["Jennyfer","Massimo Dutti","Stradivarius"]
        self.price_Jennyferd=59900
        self.price_Massimo_Dutti=69800
        self.price_Stradivarius=97000

        #__LISTE SOUS CATEGORIE Soin
        
        self.list_souscategoriestyle=["Bath Soap","Créme","Huile de cheveux"]

        self.bath_soap = ["LiveBuy", "Lux", "Santoor", "Pearl"]
        self.price_livebuy = 500
        self.price_lux = 2400
        self.price_santoor = 1450
        self.price_pearl = 2100

        self.creme = ["Fair&Lovely", "Ponds", "Olay", "Garnier"]
        self.price_fair = 1560
        self.price_pond = 1410
        self.price_olay = 4530
        self.price_garnier = 1250

        self.huile = ["Parachute", "Jasmin", "Bajaj"]
        self.price_parachute = 1450
        self.price_jasmin = 2308
        self.price_bajaj = 1500

        #__LISTE SOUS CATEGORIE Telephone

        self.list_souscategorietel = ['Iphone', 'Samsung', 'Huawei', 'Techno']

        self.Iphone = ['Iphone X', 'Iphone 11', 'Iphone 12']
        self.price_ix = 14500
        self.price_i11 = 16500
        self.price_i12 = 193000

        self.samsung = ['Samsung M16', 'Samsung MI2', 'Samsung M21']
        self.price_sm16 = 111560
        self.price_sm12 = 112560
        self.price_sm21 = 230608

        self.huawei = ['Huawei Y9S', 'Huawei Pg', 'Huawei Mate']
        self.price_y9s = 18000
        self.price_p8 = 28000
        self.price_mate = 29600

        self.techno = ['Techno Com11', 'Techno Com12', 'Techno Com13']
        self.price_com11 = 23608
        self.price_com12 = 29200
        self.price_com13 = 35600


        Main_Frame=Frame(self.root,bd=2,relief=GROOVE,bg='white')#-----la partie background
        Main_Frame.place(x=10,y=100,width=1890,height=920)

        #----------CLIENT
        client_frame=LabelFrame(Main_Frame,text="Client",font=("times new roman",15),bg="white")
        client_frame.place(x=10,y=5,width=350,height=150)

        self.lbl_contact=Label(client_frame,text='Telephone',font=("times new roman",15,"bold"),bg="white")#----MOT CONTACT
        self.lbl_contact.grid(row=0,column=0,sticky=W,padx=5,pady=2)
        
        self.lbl_nomclient=Label(client_frame,text='Nom Client',font=("times new roman",15,"bold"),bg="white")#----MOT nom client row 1
        self.lbl_nomclient.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.lbl_email=Label(client_frame,text='Email',font=("times new roman",15,"bold"),bg="white")#----MOT EMAIL ROW 2
        self.lbl_email.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        #----CHAMP INPUT-----

        self.txt_contact=ttk.Entry(client_frame,textvariable=self.c_phon,font=("times new roman",15))
        self.txt_contact.grid(row=0,column=1,sticky=W,padx=5,pady=2)

        self.txt_nomclient = ttk.Entry(client_frame, textvariable=self.c_nom, font=("times new roman", 15))
        self.txt_nomclient.grid(row=1,column=1,sticky=W,padx=5,pady=2)

        self.txt_email = ttk.Entry(client_frame, textvariable=self.c_email, font=("times new roman", 15))
        self.txt_email.grid(row=2,column=1,sticky=W,padx=5,pady=2)

        #----PRODUITS-----

        produit_frame=LabelFrame(Main_Frame,text="produit",font=("times new roman",15),bg="white")
        produit_frame.place(x=380,y=5,width=620,height=150)

        self.lbl_categori=Label(produit_frame,text="Selectionné Catégorie",font=("times new roman",15,"bold"),bg="white")
        self.lbl_categori.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.lbl_souscategori=Label(produit_frame,text="Sous Catégorie",font=("times new roman",15,"bold"),bg="white")
        self.lbl_souscategori.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.lbl_nomproduit=Label(produit_frame,text="Nom Produit",font=("times new roman",15,"bold"),bg="white")
        self.lbl_nomproduit.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.lbl_prix=Label(produit_frame,text="Prix",font=("times new roman",15,"bold"),bg="white")
        self.lbl_prix.grid(row=0,column=2,sticky=W,padx=5,pady=2)

        self.lbl_qte=Label(produit_frame,text="Quantité",font=("times new roman",15,"bold"),bg="white")
        self.lbl_qte.grid(row=1,column=2,sticky=W,padx=5,pady=2)

        self.txt_categorie=ttk.Combobox(produit_frame,font=("times new roman",10),values=self.list_categorie,width=24,state="readonly")
        self.txt_categorie.grid(row=0,column=1,sticky=W,padx=5,pady=2)
        self.txt_categorie.current(0)#---BECH TDHAHARLI KELMET SELECTIONNER MATO93ODCH FERGHA L CHAMP
        self.txt_categorie.bind("<<ComboboxSelected>>",self.fonctionCategorie)

        self.txt_souscategorie=ttk.Combobox(produit_frame,font=("times new roman",10),values=[""],width=24,state="readonly")
        self.txt_souscategorie.grid(row=1,column=1,sticky=W,padx=5,pady=2)
        self.txt_souscategorie.current(0)
        self.txt_souscategorie.bind("<<ComboboxSelected>>",self.fonctionsousCtegorie)


        self.txt_nomproduit=ttk.Combobox(produit_frame,font=("times new roman",10),textvariable=self.produit,width=24,state="readonly")
        self.txt_nomproduit.grid(row=2,column=1,sticky=W,padx=5,pady=2)
        self.txt_nomproduit.bind("<<ComboboxSelected>>",self.fonctionnomproduit)


        self.txt_prix=ttk.Combobox(produit_frame,font=("times new roman",10),textvariable=self.prix,width=20,state="readonly")
        self.txt_prix.grid(row=0,column=3,sticky=W,padx=5,pady=2)

        self.txt_qte=ttk.Entry(produit_frame,font=("times new roman",10),textvariable=self.qte,width=20)
        self.txt_qte.grid(row=1,column=3,sticky=W,padx=5,pady=2)

        #----RECHERCHE-------

        recher_Frame=Frame(Main_Frame,bd=2,bg="white")
        recher_Frame.place(x=1000,y=10,width=1000,height=70)

        self.lbl_recherche=Label(recher_Frame,text="N facture",font=("times new roman",23,"bold"),bg='white')
        self.lbl_recherche.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.txt_recherche=ttk.Entry(recher_Frame,textvariable=self.rech_factu,font=("times new roman",23),width=15)
        self.txt_recherche.grid(row=0,column=1,sticky=W,padx=5,pady=2)

        self.btn_recherch=Button(recher_Frame,text="Rechercher",command=self.rechercher,height=2,font=("times new roman",12),bg="yellow",width=11,cursor="hand2")
        self.btn_recherch.grid(row=0,column=2)

        #----ESPACE FACTURE-------

        facture_label=LabelFrame(Main_Frame,text="Facture",font=("times new roman",15,"bold"),bg="white")
        facture_label.place(x=1005,y=80,width=500,height=438)

        scroll_y=Scrollbar(facture_label,orient=VERTICAL)
        self.textarea=Text(facture_label,yscrollcommand=scroll_y.set,font=("time new roman",15,"bold"),bg="white",fg="blue")
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        #----FOOTER--------
        enbas_frame=LabelFrame(Main_Frame,text="Boutton",font=("times new roman",15),bg="white")
        enbas_frame.place(x=0,y=520,width=1880,height=300)

        self.lbl_totalbrute=Label(enbas_frame,text="Total brute",font=("times new roman",18,"bold"),bg="white")
        self.lbl_totalbrute.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.lbl_taxe=Label(enbas_frame,text="Taxe",font=("times new roman",18,"bold"),bg="white")
        self.lbl_taxe.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.lbl_totalnet=Label(enbas_frame,text="Total Net",font=("times new roman",18,"bold"),bg="white")
        self.lbl_totalnet.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.txt_totalbrute=ttk.Entry(enbas_frame,textvariable=self.totalbrute,font=("times new roman",20),width=10,state="readonly")
        self.txt_totalbrute.grid(row=0,column=1,sticky=W,padx=5,pady=2)

        self.txt_taxe=ttk.Entry(enbas_frame,textvariable=self.taxe,font=("times new roman",20),width=10,state="readonly")
        self.txt_taxe.grid(row=1,column=1,sticky=W,padx=5,pady=2)

        self.txt_totalnet=ttk.Entry(enbas_frame,textvariable=self.totalnet,font=("times new roman",20),width=10,state="readonly")
        self.txt_totalnet.grid(row=2,column=1,sticky=W,padx=5,pady=2)

        #-----------IMAGE--------------

        # ouvrir l'image
        image = Image.open("C:/Users/Soulaima/Desktop/projetpython/Super_marche/image/bean.jpg")

        # redimensionner l'image
        new_size = (490, 350)
        image = image.resize(new_size, Image.ANTIALIAS)

        # convertir l'image en PhotoImage
        self.imge1 = ImageTk.PhotoImage(image)

        # afficher l'image dans le Label
        self.lbl_image1 = Label(image=self.imge1)
        self.lbl_image1.place(x=20, y=265)

        # ouvrir la deuxième image
        image2 = Image.open("C:/Users/Soulaima/Desktop/projetpython/Super_marche/image/test2.jpg")

        # redimensionner l'image
        new_size = (490, 350)
        image2 = image2.resize(new_size, Image.ANTIALIAS)

        # convertir l'image en PhotoImage
        self.imge2 = ImageTk.PhotoImage(image2)

        # afficher l'image dans le Label
        self.lbl_image2 = Label(image=self.imge2)
        self.lbl_image2.place(x=520, y=265)


        #-----------BOUTON-------
        btn_Frame=Frame(enbas_frame,bd=2,bg="white")
        btn_Frame.place(x=310,y=20)

        self.ajoutPanier=Button(btn_Frame,text="Ajouter Card",command=self.ajouter ,height=2,font=("times new roman",15,"bold"),bg="yellow",width=15,cursor="hand2")
        self.ajoutPanier.grid(row=0,column=0)

        self.genere=Button(btn_Frame,text="Généré",command=self.genererFacture,height=2,font=("times new roman",15,"bold"),bg="pink",width=15,cursor="hand2")
        self.genere.grid(row=0,column=1)

        self.sauvegarde=Button(btn_Frame,text="Sauvegarde Facture",command=self.sauvegarder,height=2,font=("times new roman",15,"bold"),bg="green",width=15,cursor="hand2")
        self.sauvegarde.grid(row=0,column=2)

        self.imprime=Button(btn_Frame,text="Imprimer",command=self.imprimer,height=2,font=("times new roman",15,"bold"),bg="orange",width=15,cursor="hand2")
        self.imprime.grid(row=0,column=3)

        self.reini=Button(btn_Frame,text="Reinitialiser",command=self.rein,height=2,font=("times new roman",15,"bold"),bg="red",width=15,cursor="hand2")
        self.reini.grid(row=0,column=4)

        

        self.Bienvenu()

        self.l=[]




        #-----------FONCTIONS --------

    def Bienvenu(self):
      self.textarea.delete(1.0,END)
      self.textarea.insert(END,"\tBienvenu Chez Super Marché Soulaima")
      self.textarea.insert(END,f"\n\nNuméro Facture : {self.n_factu.get()}")
      self.textarea.insert(END,f"\nNom Client : {self.c_nom.get()}")
      self.textarea.insert(END,f"\nTélephone : {self.c_phon.get()}")
      self.textarea.insert(END,f"\nEmail : {self.c_email.get()}")

      
      self.textarea.insert(END,f"\n**********************************************************")
      self.textarea.insert(END,f"\nProduits\t\tQTE\t\tPrix")
      self.textarea.insert(END,f"\n**********************************************************")





    def ajouter(self):
        self.n=self.prix.get()
        self.m=self.qte.get()*self.n
        self.l.append(self.m)#append pour ajouter a la fin de la liste
        if self.produit.get()=="":
            messagebox.showerror("Erreur","Selectionnez un produit")
        else:
            self.textarea.insert(END,f"\n{self.produit.get()}\t\t{self.qte.get()}\t\t{self.m}")
            self.totalbrute.set(str("%.2f DT"%(sum(self.l))))
            self.taxe.set(str("%.2f DT"%((((sum(self.l)) - (self.prix.get())) * 1 )/ 100)))#taxe bech nahi menou 0.1
            self.totalnet.set(str("%.2f DT" % (((sum(self.l)) + ((((sum(self.l)) - (self.prix.get())) * 1) / 100)))))


    def genererFacture(self):
        if self.produit.get()=="":
            messagebox.showerror("Erreur","Ajouter d'abord un produit")
        else:
            text=self.textarea.get(10.0,(10.0+float(len(self.l))))  #partie facture generer
            self.Bienvenu()
            text=self.textarea.insert(END,text)
            self.textarea.insert(END,f"\n**********************************************************")
            self.textarea.insert(END,f"\nTotal brute : \t\t\t{self.totalbrute.get()}")
            self.textarea.insert(END,f"\nTotal Taxe : \t\t\t{self.taxe.get()}")
            self.textarea.insert(END,f"\nTotal Net : \t\t\t{self.totalnet.get()}")

    def imprimer(self):
        fichier=tempfile.mktemp(".txt")
        open(fichier,"w").write(self.textarea.get("1.0",END))
        os.startfile(fichier,"print")




    def rechercher(self):
     trouver="non"
     for i in os.listdir("C:/Users/Soulaima/Desktop/projetpython/Facture/"):
        if i.split(".")[0]==self.rech_factu.get():
            f1=open(f"C:/Users/Soulaima/Desktop/projetpython/Facture/{i}","r")
            self.textarea.delete(1.0,END)
            for d in f1:
                self.textarea.insert(END,d)
                f1.close
                trouver="oui"
     if trouver=="non":
         messagebox.showerror("Erreur","La facture n'existe pas")

    def rein(self):
        self.textarea.delete(1.0,END)
        self.c_nom.set("")
        self.c_phon.set("")  
        self.c_email.set("")  
        x=random.randint(1000,9999)
        self.n_factu.set(str(x))
        self.rech_factu.set("")
        self.produit.set("")
        self.prix.set(0)
        self.qte.set(0)
        self.l=[0]
        self.totalbrute.set("")
        self.taxe.set("")
        self.totalnet.set("")
        self.Bienvenu()


  








    def sauvegarder(self):
        op=messagebox.askyesno("Sauvegarder","Voulez-vous sauvegarder la facture?" )
        if op==True:
            self.donneFacture=self.textarea.get(1.0,END)
            f1=open("C:/Users/Soulaima/Desktop/projetpython/Facture/"+str(self.n_factu.get())+".txt","w")
            f1.write(self.donneFacture)
            messagebox.showinfo("Sauvegarder",f"La facture numéro{self.n_factu.get()} a été enregistré avec succés")
            f1.close()







    def fonctionCategorie(self,event=""):
        if self.txt_categorie.get()=="Vetement":
            self.txt_souscategorie.config(values=self.list_souscategorieVetemnt)
            self.txt_souscategorie.current(0)

        if self.txt_categorie.get()=="Soin":
            self.txt_souscategorie.config(values=self.list_souscategoriestyle)
            self.txt_souscategorie.current(0)    


        if self.txt_categorie.get()=="Télephone":
            self.txt_souscategorie.config(values=self.list_souscategorietel)
            self.txt_souscategorie.current(0)    


            #-----------FONCTIONS SOUS CATEGORIE



    def fonctionsousCtegorie(self,even=""):
        #-----vetement
         if self.txt_souscategorie.get()=="Pantalon":
             self.txt_nomproduit.config(values=self.pantalon)
             self.txt_nomproduit.current(0)

         if self.txt_souscategorie.get() == "T-Shirt":
            self.txt_nomproduit.config(values=self.t_shirt)
            self.txt_nomproduit.current(0)
            
         if self.txt_souscategorie.get() == "Robe":
            self.txt_nomproduit.config(values=self.Robe)
            self.txt_nomproduit.current(0)

         #-----Soin

         if self.txt_souscategorie.get() == "Bath Soap":
          self.txt_nomproduit.config(values=self.bath_soap)
          self.txt_nomproduit.current(0)

         if self.txt_souscategorie.get() == "Créme":
            self.txt_nomproduit.config(values=self.creme)
            self.txt_nomproduit.current(0)

         if self.txt_souscategorie.get() == "Huile de cheveux":
            self.txt_nomproduit.config(values=self.huile)
            self.txt_nomproduit.current(0)

         #-----Telephone

         if self.txt_souscategorie.get() == "Iphone":#--------------TXT CAR C LE CONTENU
            self.txt_nomproduit.config(values=self.Iphone)
            self.txt_nomproduit.current(0)

         if self.txt_souscategorie.get() == "Samsung":
            self.txt_nomproduit.config(values=self.samsung)
            self.txt_nomproduit.current(0)

         if self.txt_souscategorie.get() == "Huawei":
            self.txt_nomproduit.config(values=self.huawei)
            self.txt_nomproduit.current(0)    

         if self.txt_souscategorie.get() == "Techno":
            self.txt_nomproduit.config(values=self.techno)
            self.txt_nomproduit.current(0)

         

                    #-----------FONCTIONS PRODUIT


    def fonctionnomproduit(self,even=""):

        if self.txt_nomproduit.get() == "Levis":
            self.txt_prix.config(values=self.price_levis)
            self.txt_prix.current(0) 
            self.qte.set(1)#valeur par defaut tet7at fel quantité

        if self.txt_nomproduit.get() == "Bershka":
            self.txt_prix.config(values=self.price_Bershka)
            self.txt_prix.current(0) 
            self.qte.set(1)

        if self.txt_nomproduit.get() == "Jack&Jones":
            self.txt_prix.config(values=self.price_jack_jones)
            self.txt_prix.current(0) 
            self.qte.set(1)   
        
        if self.txt_nomproduit.get() == "Pull&Bear":
            self.txt_prix.config(values=self.price_PullBear)
            self.txt_prix.current(0) 
            self.qte.set(1)

        if self.txt_nomproduit.get() == "Polo":
            self.txt_prix.config(values=self.price_polo)
            self.txt_prix.current(0) 
            self.qte.set(1)  

        if self.txt_nomproduit.get() == "Zara":
            self.txt_prix.config(values=self.price_Zara)
            self.txt_prix.current(0) 
            self.qte.set(1) 
        
        if self.txt_nomproduit.get() == "Jennyfer":
            self.txt_prix.config(values=self.price_Jennyferd)
            self.txt_prix.current(0) 
            self.qte.set(1) 

        if self.txt_nomproduit.get() == "Massimo Dutti":
            self.txt_prix.config(values=self.price_Massimo_Dutti)
            self.txt_prix.current(0) 
            self.qte.set(1)
        
        if self.txt_nomproduit.get() == "Stradivarius":
            self.txt_prix.config(values=self.price_Stradivarius)
            self.txt_prix.current(0) 
            self.qte.set(1)

        if self.txt_nomproduit.get() == "LiveBuy":
            self.txt_prix.config(values=self.price_livebuy)
            self.txt_prix.current(0) 
            self.qte.set(1)

        if self.txt_nomproduit.get() == "Lux":
            self.txt_prix.config(values=self.price_lux)
            self.txt_prix.current(0) 
            self.qte.set(1)

        if self.txt_nomproduit.get() == "Santoor":
            self.txt_prix.config(values=self.price_santoor)
            self.txt_prix.current(0) 
            self.qte.set(1)

        if self.txt_nomproduit.get() == "Pearl":
            self.txt_prix.config(values=self.price_pearl)
            self.txt_prix.current(0) 
            self.qte.set(1)

        if self.txt_nomproduit.get() == "Fair&Lovely":
            self.txt_prix.config(values=self.price_fair)
            self.txt_prix.current(0) 
            self.qte.set(1)

        if self.txt_nomproduit.get() == "Ponds":
            self.txt_prix.config(values=self.price_pond)
            self.txt_prix.current(0) 
            self.qte.set(1)

        if self.txt_nomproduit.get() == "Olay":
            self.txt_prix.config(values=self.price_olay)
            self.txt_prix.current(0) 
            self.qte.set(1)

        if self.txt_nomproduit.get() == "Garnier":
            self.txt_prix.config(values=self.price_garnier)
            self.txt_prix.current(0) 
            self.qte.set(1)

        if self.txt_nomproduit.get() == "Parachute":
            self.txt_prix.config(values=self.price_parachute)
            self.txt_prix.current(0) 
            self.qte.set(1)

        if self.txt_nomproduit.get() == "Jasmin":
            self.txt_prix.config(values=self.price_jasmin)
            self.txt_prix.current(0) 
            self.qte.set(1)

        if self.txt_nomproduit.get() == "Bajaj":
            self.txt_prix.config(values=self.price_bajaj)
            self.txt_prix.current(0) 
            self.qte.set(1)

        if self.txt_nomproduit.get() == "Iphone X":
            self.txt_prix.config(values=self.price_ix)
            self.txt_prix.current(0) 
            self.qte.set(1)

        if self.txt_nomproduit.get() == "Samsung M16":
            self.txt_prix.config(values=self.price_sm16)
            self.txt_prix.current(0) 
            self.qte.set(1)

        if self.txt_nomproduit.get() == "Samsung MI2":
            self.txt_prix.config(values=self.price_sm12)
            self.txt_prix.current(0) 
            self.qte.set(1)

        if self.txt_nomproduit.get() == "Iphone 11":
            self.txt_prix.config(values=self.price_i11)
            self.txt_prix.current(0) 
            self.qte.set(1)

        if self.txt_nomproduit.get() == "Samsung M21":
            self.txt_prix.config(values=self.price_sm21)
            self.txt_prix.current(0) 
            self.qte.set(1)

        if self.txt_nomproduit.get() == "Huawei Y9S":
            self.txt_prix.config(values=self.price_y9s)
            self.txt_prix.current(0) 
            self.qte.set(1)

        if self.txt_nomproduit.get() == "Huawei Pg":
            self.txt_prix.config(values=self.price_p8)
            self.txt_prix.current(0) 
            self.qte.set(1)

        if self.txt_nomproduit.get() == "Iphone 12":
            self.txt_prix.config(values=self.price_i12)
            self.txt_prix.current(0) 
            self.qte.set(1)

        if self.txt_nomproduit.get() == "Huawei Mate":
            self.txt_prix.config(values=self.price_mate)
            self.txt_prix.current(0) 
            self.qte.set(1)

        if self.txt_nomproduit.get() == "Techno Com11":
            self.txt_prix.config(values=self.price_com11)
            self.txt_prix.current(0) 
            self.qte.set(1)

        if self.txt_nomproduit.get() == "Techno Com12":
            self.txt_prix.config(values=self.price_com12)
            self.txt_prix.current(0) 
            self.qte.set(1)

        if self.txt_nomproduit.get() == "Techno Com13":
            self.txt_prix.config(values=self.price_com13)
            self.txt_prix.current(0) 
            self.qte.set(1)

if __name__ == "__main__":
    root = Tk()
    obj = SuperMarche(root)
    root.mainloop()




