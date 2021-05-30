
from tkinter import*
from tkinter import ttk
import sqlite3
from tkinter import messagebox

class Enregistrement:
    def __init__(self,root):
        self.root=root
        self.root.title("FSS-TPME")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        

        title=Label(self.root,text="Liste de divers activités de Djibouti ville",bd=10,relief=GROOVE,font=("times new roman",30,"bold"),bg="yellow",fg="red")
        title.pack(side=TOP,fill=X)

        ########### Les variables ##############
        self.No_var=StringVar()
        self.nom_var=StringVar()
        self.adresse_var=StringVar()
        self.activite_var=StringVar()
        self.genre_var=StringVar()
        self.cni_var=StringVar()
        self.contact_var=StringVar()
        self.montant_var=IntVar()

        self.search_by=StringVar()
        self.search_txt=StringVar()

        ##### Manage frame ######################

        Manage_frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        Manage_frame.place(x=20,y=100,width=500,height=600)

        m_title=Label(Manage_frame,text="Gestion de données",bg="crimson",fg="white",font=("time new roman",20,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)

        #No
        lb1_No=Label(Manage_frame,text="No",bg="crimson",fg="white",font=("time new roman",15,"bold"))
        lb1_No.grid(row=1,column=0,pady=10,padx=20,sticky="w")
        
        txt_No=Entry(Manage_frame,textvariable=self.No_var,bd=5,relief=GROOVE,font=("time new roman",13,"bold"))
        txt_No.grid(row=1,column=1,pady=10,padx=20,sticky="w")

        # NOM
        lb1_nom=Label(Manage_frame,text="Nom",bg="crimson",fg="white",font=("time new roman",15,"bold"))
        lb1_nom.grid(row=2,column=0,pady=10,padx=20,sticky="w")
        
        txt_nom=Entry(Manage_frame,textvariable=self.nom_var,bd=5,relief=GROOVE,font=("time new roman",13,"bold"))
        txt_nom.grid(row=2,column=1,pady=10,padx=20,sticky="w")

        # Adresse
        lb1_adresse=Label(Manage_frame,text="Adresse",bg="crimson",fg="white",font=("time new roman",15,"bold"))
        lb1_adresse.grid(row=3,column=0,pady=10,padx=20,sticky="w")
        
        txt_adresse=Entry(Manage_frame,textvariable=self.adresse_var,bd=5,relief=GROOVE,font=("time new roman",13,"bold"))
        txt_adresse.grid(row=3,column=1,pady=10,padx=20,sticky="w")

        # Activité
        lb1_activite=Label(Manage_frame,text="Activité",bg="crimson",fg="white",font=("time new roman",15,"bold"))
        lb1_activite.grid(row=4,column=0,pady=10,padx=20,sticky="w")
        
        txt_adresse=Entry(Manage_frame,textvariable=self.activite_var,bd=5,relief=GROOVE,font=("time new roman",13,"bold"))
        txt_adresse.grid(row=4,column=1,pady=10,padx=20,sticky="w")

        #Genre
        lb1_genre=Label(Manage_frame,text="Genre",bg="crimson",fg="white",font=("time new roman",15,"bold"))
        lb1_genre.grid(row=5,column=0,pady=10,padx=20,sticky="w")

        combo_genre=ttk.Combobox(Manage_frame,textvariable=self.genre_var,font=("time new roman",13,"bold"),state='readonly')
        combo_genre['values']=("Masculin","Feminin","Autre")
        combo_genre.grid(row=5,column=1,padx=20,pady=10)
        # No CNI
        lb1_CNI=Label(Manage_frame,text="N°CNI",bg="crimson",fg="white",font=("time new roman",15,"bold"))
        lb1_CNI.grid(row=6,column=0,pady=10,padx=20,sticky="w")
        
        txt_CNI=Entry(Manage_frame,textvariable=self.cni_var,bd=5,relief=GROOVE,font=("time new roman",13,"bold"))
        txt_CNI.grid(row=6,column=1,pady=10,padx=20,sticky="w")

        # No de N°Téléphone
        lb1_contact=Label(Manage_frame,text="N°Téléphone",bg="crimson",fg="white",font=("time new roman",15,"bold"))
        lb1_contact.grid(row=7,column=0,pady=10,padx=20,sticky="w")
        
        txt_contact=Entry(Manage_frame,textvariable=self.contact_var,bd=5,relief=GROOVE,font=("time new roman",13,"bold"))
        txt_contact.grid(row=7,column=1,pady=0,padx=20,sticky="w")

        # Montant
        lb1_montant = Label(Manage_frame,text="Montant",bg="crimson",fg="white",font=("time new roman",15,"bold"))
        lb1_montant.grid(row=8,column=0,pady=10,padx=20,sticky="w")
        
        txt_montant=Entry(Manage_frame,textvariable=self.montant_var,bd=5,relief=GROOVE,font=("time new roman",13,"bold"))
        txt_montant.grid(row=8,column=1,pady=0,padx=20,sticky="w")


        ##### Button Frame #########
        btn_frame=Frame(Manage_frame,bd=4,relief=RIDGE,bg="crimson")
        btn_frame.place(x=15,y=520,width=460)

        Addbtn=Button(btn_frame,text="Ajouter",width=8,command=self.ajouter).grid(row=0,column=0,padx=10,pady=10)
        updatebtn=Button(btn_frame,text="Modifier",width=8,command=self.modifier_data).grid(row=0,column=1,padx=10,pady=10)
        deletebtn=Button(btn_frame,text="Supprimer",width=8,command=self.supprimer).grid(row=0,column=2,padx=10,pady=10)
        clearbtn=Button(btn_frame,text="Effacer",width=8,command=self.clear).grid(row=0,column=3,padx=10,pady=10)


        ##### Detail frame ######################
        Detail_frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        Detail_frame.place(x=550,y=100,width=740,height=600)

        lb1_recherche=Label(Detail_frame,text="Rechercher",bg="crimson",fg="white",font=("time new roman",13,"bold"))
        lb1_recherche.grid(row=0,column=0,pady=10,padx=20,sticky="w")

        combo_recherche=ttk.Combobox(Detail_frame,textvariable=self.search_by,width=10,font=("time new roman",11,"bold"),state='readonly')
        combo_recherche['values']=("No","Nom","N°Téléphone")
        combo_recherche.grid(row=0,column=1,padx=20,pady=10)

        txt_recherche=Entry(Detail_frame,textvariable=self.search_txt,width=20,bd=5,relief=GROOVE,font=("time new roman",10,"bold"))
        txt_recherche.grid(row=0,column=2,pady=10,padx=20,sticky="w")

        recherchebtn=Button(Detail_frame,text="Rechercher",width=6,pady=5,command=self.search).grid(row=0,column=3,padx=10,pady=10)
        showallbtn=Button(Detail_frame,text="Voir tout",width=5,pady=5,command=self.fetch_data).grid(row=0,column=4,padx=10,pady=10)

        ############ Tableau Frame ##############"
        Tabel_frame=Frame(Detail_frame,bd=4,relief=RIDGE,bg="crimson")
        Tabel_frame.place(x=10,y=70,width=720,height=520)

        scroll_x=Scrollbar(Tabel_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Tabel_frame,orient=VERTICAL)
        self.manage_table=ttk.Treeview(Tabel_frame,columns=("No","Nom","Adresse","Activité","Genre","CNI","N°Téléphone","Montant"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.manage_table.xview)
        scroll_y.config(command=self.manage_table.yview)
        self.manage_table.heading("No",text="No")
        self.manage_table.heading("Nom",text="Nom")
        self.manage_table.heading("Adresse",text="Adresse")
        self.manage_table.heading("Activité",text="Activité")
        self.manage_table.heading("Genre",text="Genre")
        self.manage_table.heading("CNI",text="CNI")
        self.manage_table.heading("N°Téléphone",text="N°Téléphone")
        self.manage_table.heading("Montant",text="Montant")
        self.manage_table['show']='headings'
        self.manage_table.column("No",width=70)
        self.manage_table.column("Nom",width=150)
        self.manage_table.column("Adresse",width=100)
        self.manage_table.column("Activité",width=150)
        self.manage_table.column("Genre",width=70)
        self.manage_table.column("CNI",width=70)
        self.manage_table.column("N°Téléphone",width=100)
        self.manage_table.column("Montant",width=70)
        self.manage_table.pack(fill=BOTH,expand=1)
        self.manage_table.bind("<ButtonRelease-1>",self.get_cursor)

        self.fetch_data()

    
    def ajouter(self):
        if self.No_var.get()=="" or self.nom_var.get()=="":
            messagebox.showerror("Erreur","tous les cases doivent etre remplit merci")
        else:
            con=sqlite3.connect('New_work.db')
            cur=con.cursor()
            n=self.No_var.get()
            nom=self.nom_var.get()
            ad=self.adresse_var.get()
            ac=self.activite_var.get()
            genre=self.genre_var.get()
            cni=self.cni_var.get()
            contact=self.contact_var.get()
            montant=self.montant_var.get()
            cur.execute("insert into Djibouti values(?,?,?,?,?,?,?,?)",(n,nom,ad,ac,genre,cni,contact,montant))                                           
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Succès","L'enregistrement a été inséré")

    def fetch_data(self):
        con=sqlite3.connect('New_work.db')
        cur=con.cursor()
        cur.execute("select * from Djibouti")
        rows=cur.fetchall()
        if len(rows)!=0:
                self.manage_table.delete(*self.manage_table.get_children())
                for row in rows:
                        self.manage_table.insert('',END,values=row)
                con.commit()
        con.close()

    def clear(self):
        self.No_var.set("")
        self.nom_var.set("")
        self.adresse_var.set("")
        self.activite_var.set("")
        self.genre_var.set("")
        self.cni_var.set("")
        self.contact_var.set("")
        self.montant_var.set("")

    def get_cursor(self,ev):
        curosor_row=self.manage_table.focus()
        contents=self.manage_table.item(curosor_row)
        row=contents['values']
        self.No_var.set(row[0])
        self.nom_var.set(row[1])
        self.adresse_var.set(row[2])
        self.activite_var.set(row[3])
        self.genre_var.set(row[4])
        self.cni_var.set(row[5])
        self.contact_var.set(row[6])
        self.montant_var.set(row[7])

    def modifier_data(self):
        con=sqlite3.connect('New_work.db')
        cur=con.cursor()
        n=self.No_var.get()
        nom=self.nom_var.get()
        ad=self.adresse_var.get()
        ac=self.activite_var.get()
        genre=self.genre_var.get()
        cni=self.cni_var.get()
        contact=self.contact_var.get()
        montant=self.montant_var.get()
        cur.execute("update Djibouti set Nom=?,Adresse=?,Activité=?,Genre=?,N°CNI=?,N°Téléphone=?,Montant=? where No=?",(nom,ad,ac,genre,cni,contact,montant,n))                                           
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()


    def supprimer(self):
        con=sqlite3.connect('New_work.db')
        cur=con.cursor()
        cur.execute("delete from Djibouti where No=?",self.No_var.get())
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

        
    def search(self):
        try: 
            con=sqlite3.connect('New_work.db')
            cur=con.cursor()
            sql="select * from Djibouti where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'"
            cur.execute(sql)
            rows=cur.fetchall()
            if len(rows)!=0:
                    self.manage_table.delete(*self.manage_table.get_children())
                    for row in rows:
                            self.manage_table.insert('',END,values=row)
                    con.commit()
            con.close()

        except:
            messagebox.show('No Data','No found')
            self.clear()

    

root=Tk()
obj=Enregistrement(root)
root.mainloop()
