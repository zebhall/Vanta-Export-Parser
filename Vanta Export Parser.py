#   Vanta Export Parser v0.1 by ZH (13/04/2021)

import csv

crmPrefix = "OREAS {}"

values_Ag = [" "," "," "]
values_Al = [" "," "," "]
values_As = [" "," "," "]
values_Au = [" "," "," "]
values_B = [" "," "," "]
values_Ba = [" "," "," "]
values_Be = [" "," "," "]
values_Bi = [" "," "," "]
values_C = [" "," "," "]
values_Ca = [" "," "," "]
values_Cd = [" "," "," "]
values_Ce = [" "," "," "]
values_Cl = [" "," "," "]
values_Co = [" "," "," "]
values_Cr = [" "," "," "]
values_Cs = [" "," "," "]
values_Cu = [" "," "," "]
values_Dy = [" "," "," "]
values_Er = [" "," "," "]
values_Eu = [" "," "," "]
values_Fe = [" "," "," "]
values_Ga = [" "," "," "]
values_Gd = [" "," "," "]
values_Ge = [" "," "," "]
values_Hf = [" "," "," "]
values_Hg = [" "," "," "]
values_Ho = [" "," "," "]
values_In = [" "," "," "]
values_Ir = [" "," "," "]
values_K = [" "," "," "]
values_La = [" "," "," "]
values_Li = [" "," "," "]
values_Lu = [" "," "," "]
values_Mg = [" "," "," "]
values_Mn = [" "," "," "]
values_Mo = [" "," "," "]
values_Na = [" "," "," "]
values_Nb = [" "," "," "]
values_Nd = [" "," "," "]
values_Ni = [" "," "," "]
values_Os = [" "," "," "]
values_P = [" "," "," "]
values_Pb = [" "," "," "]
values_Pd = [" "," "," "]
values_Pr = [" "," "," "]
values_Pt = [" "," "," "]
values_Rb = [" "," "," "]
values_Re = [" "," "," "]
values_Rh = [" "," "," "]
values_Ru = [" "," "," "]
values_S = [" "," "," "]
values_Sb = [" "," "," "]
values_Sc = [" "," "," "]
values_Se = [" "," "," "]
values_Si = [" "," "," "]
values_Sm = [" "," "," "]
values_Sn = [" "," "," "]
values_Sr = [" "," "," "]
values_Ta = [" "," "," "]
values_Tb = [" "," "," "]
values_Te = [" "," "," "]
values_Th = [" "," "," "]
values_Ti = [" "," "," "]
values_Tl = [" "," "," "]
values_Tm = [" "," "," "]
values_U = [" "," "," "]
values_V = [" "," "," "]
values_W = [" "," "," "]
values_Y = [" "," "," "]
values_Yb = [" "," "," "]
values_Zn = [" "," "," "]
values_Zr = [" "," "," "]
values_Geology = [" "," "]
spacer = [" "," "," "," "," "]
outputArray = [] 

def getInput():                             # Gets user input and fills related variables accordingly

    global exportName
    exportName = input("Vanta Export file name (including extension):")
    print("Formatting Information for", crmID)


def fillValues(crm):                        # Fills all 'values' lists with the converted data scraped from catalogue then fills the outputArray list
    
    with open(exportName, mode='r') as oreas_file:            #opens oreas catalogue file as a csv dictionary for improved lookup
        reader = csv.DictReader(oreas_file, delimiter=',')
        for row in reader:
            if row["CRM ID"] == crm and len(values_Geology) == 2:                #checks that geology values haven't been written to yet
                values_Geology.insert(0, row["Matrix"])                            #puts matrix from catalogue into geology values
                values_Geology.insert(1, row["Mineralisation Style"])              #puts mineralisation from catalogue into geology values

    with open(exportName, mode='r') as oreas_file:
        reader = csv.DictReader(oreas_file, delimiter=',')
        for row in reader:
            if row["CRM ID"] == crm:

                if row["Element"] == "Silver, Ag" and len(values_Ag) == 3:      
                    if row["Unit"] == "ppm":
                        values_Ag.insert(0, row["Certified Value"])                  
                        values_Ag.insert(1, row["1SD"])
                        values_Ag.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "ppb":
                        try:
                            values_Ag.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Ag.insert(1, (float(row["1SD"])*0.001))
                            values_Ag.insert(2, row["Analysis Method"])
                        except:
                            values_Ag.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Ag.insert(1, row["1SD"])
                            values_Ag.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "wt.%":
                        try:
                            values_Ag.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Ag.insert(1, (float(row["1SD"])*10000))
                            values_Ag.insert(2, row["Analysis Method"])
                        except:
                            values_Ag.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Ag.insert(1, row["1SD"])
                            values_Ag.insert(2, row["Analysis Method"])
            
                elif row["Element"] == "Aluminium, Al" and len(values_Al) == 3:      
                    if row["Unit"] == "ppm":
                        values_Al.insert(0, row["Certified Value"])                  
                        values_Al.insert(1, row["1SD"])
                        values_Al.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "ppb":
                        try:
                            values_Al.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Al.insert(1, (float(row["1SD"])*0.001))
                            values_Al.insert(2, row["Analysis Method"])
                        except:
                            values_Al.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Al.insert(1, row["1SD"])
                            values_Al.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "wt.%":
                        try:
                            values_Al.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Al.insert(1, (float(row["1SD"])*10000))
                            values_Al.insert(2, row["Analysis Method"])
                        except:
                            values_Al.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Al.insert(1, row["1SD"])
                            values_Al.insert(2, row["Analysis Method"])

                elif row["Element"] == "Arsenic, As" and len(values_As) == 3:      
                    if row["Unit"] == "ppm":
                        values_As.insert(0, row["Certified Value"])                  
                        values_As.insert(1, row["1SD"])
                        values_As.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "ppb":
                        try:
                            values_As.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_As.insert(1, (float(row["1SD"])*0.001))
                            values_As.insert(2, row["Analysis Method"])
                        except:
                            values_As.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_As.insert(1, row["1SD"])
                            values_As.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "wt.%":
                        try:
                            values_As.insert(0, (float(row["Certified Value"])*10000))                  
                            values_As.insert(1, (float(row["1SD"])*10000))
                            values_As.insert(2, row["Analysis Method"])
                        except:
                            values_As.insert(0, (float(row["Certified Value"])*10000))                  
                            values_As.insert(1, row["1SD"])
                            values_As.insert(2, row["Analysis Method"])

                elif row["Element"] == "Gold, Au" and len(values_Au) == 3:      
                    if row["Unit"] == "ppm":
                        values_Au.insert(0, row["Certified Value"])                  
                        values_Au.insert(1, row["1SD"])
                        values_Au.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "ppb":
                        try:
                            values_Au.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Au.insert(1, (float(row["1SD"])*0.001))
                            values_Au.insert(2, row["Analysis Method"])
                        except:
                            values_Au.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Au.insert(1, row["1SD"])
                            values_Au.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "wt.%":
                        try:
                            values_Au.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Au.insert(1, (float(row["1SD"])*10000))
                            values_Au.insert(2, row["Analysis Method"])
                        except:
                            values_Au.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Au.insert(1, row["1SD"])
                            values_Au.insert(2, row["Analysis Method"])

                elif row["Element"] == "Boron, B" and len(values_B) == 3:      
                    if row["Unit"] == "ppm":
                        values_B.insert(0, row["Certified Value"])                  
                        values_B.insert(1, row["1SD"])
                        values_B.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "ppb":
                        try:
                            values_B.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_B.insert(1, (float(row["1SD"])*0.001))
                            values_B.insert(2, row["Analysis Method"])
                        except:
                            values_B.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_B.insert(1, row["1SD"])
                            values_B.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "wt.%":
                        try:
                            values_B.insert(0, (float(row["Certified Value"])*10000))                  
                            values_B.insert(1, (float(row["1SD"])*10000))
                            values_B.insert(2, row["Analysis Method"])
                        except:
                            values_B.insert(0, (float(row["Certified Value"])*10000))                  
                            values_B.insert(1, row["1SD"])
                            values_B.insert(2, row["Analysis Method"])

                elif row["Element"] == "Barium, Ba" and len(values_Ba) == 3:      
                    if row["Unit"] == "ppm":
                        values_Ba.insert(0, row["Certified Value"])                  
                        values_Ba.insert(1, row["1SD"])
                        values_Ba.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "ppb":
                        try:
                            values_Ba.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Ba.insert(1, (float(row["1SD"])*0.001))
                            values_Ba.insert(2, row["Analysis Method"])
                        except:
                            values_Ba.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Ba.insert(1, row["1SD"])
                            values_Ba.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "wt.%":
                        try:
                            values_Ba.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Ba.insert(1, (float(row["1SD"])*10000))
                            values_Ba.insert(2, row["Analysis Method"])
                        except:
                            values_Ba.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Ba.insert(1, row["1SD"])
                            values_Ba.insert(2, row["Analysis Method"])

                elif row["Element"] == "Beryllium, Be" and len(values_Be) == 3:
                    if row["Unit"] == "ppm":
                        values_Be.insert(0, row["Certified Value"])                  
                        values_Be.insert(1, row["1SD"])
                        values_Be.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "ppb":
                        try:
                            values_Be.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Be.insert(1, (float(row["1SD"])*0.001))
                            values_Be.insert(2, row["Analysis Method"])
                        except:
                            values_Be.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Be.insert(1, row["1SD"])
                            values_Be.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "wt.%":
                        try:
                            values_Be.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Be.insert(1, (float(row["1SD"])*10000))
                            values_Be.insert(2, row["Analysis Method"])
                        except:
                            values_Be.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Be.insert(1, row["1SD"])
                            values_Be.insert(2, row["Analysis Method"])

                elif row["Element"] == "Bismuth, Bi" and len(values_Bi) == 3:      
                    if row["Unit"] == "ppm":
                        values_Bi.insert(0, row["Certified Value"])                  
                        values_Bi.insert(1, row["1SD"])
                        values_Bi.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "ppb":
                        try:
                            values_Bi.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Bi.insert(1, (float(row["1SD"])*0.001))
                            values_Bi.insert(2, row["Analysis Method"])
                        except:
                            values_Bi.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Bi.insert(1, row["1SD"])
                            values_Bi.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "wt.%":
                        try:
                            values_Bi.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Bi.insert(1, (float(row["1SD"])*10000))
                            values_Bi.insert(2, row["Analysis Method"])
                        except:
                            values_Bi.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Bi.insert(1, row["1SD"])
                            values_Bi.insert(2, row["Analysis Method"])

                elif row["Element"] == "Carbon, C" and len(values_C) == 3:      
                    if row["Unit"] == "ppm":
                        values_C.insert(0, row["Certified Value"])                  
                        values_C.insert(1, row["1SD"])
                        values_C.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "ppb":
                        try:
                            values_C.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_C.insert(1, (float(row["1SD"])*0.001))
                            values_C.insert(2, row["Analysis Method"])
                        except:
                            values_C.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_C.insert(1, row["1SD"])
                            values_C.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "wt.%":
                        try:
                            values_C.insert(0, (float(row["Certified Value"])*10000))                  
                            values_C.insert(1, (float(row["1SD"])*10000))
                            values_C.insert(2, row["Analysis Method"])
                        except:
                            values_C.insert(0, (float(row["Certified Value"])*10000))                  
                            values_C.insert(1, row["1SD"])
                            values_C.insert(2, row["Analysis Method"])

                elif row["Element"] == "Calcium, Ca" and len(values_Ca) == 3:      
                    if row["Unit"] == "ppm":
                        values_Ca.insert(0, row["Certified Value"])                  
                        values_Ca.insert(1, row["1SD"])
                        values_Ca.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "ppb":
                        try:
                            values_Ca.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Ca.insert(1, (float(row["1SD"])*0.001))
                            values_Ca.insert(2, row["Analysis Method"])
                        except:
                            values_Ca.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Ca.insert(1, row["1SD"])
                            values_Ca.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "wt.%":
                        try:
                            values_Ca.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Ca.insert(1, (float(row["1SD"])*10000))
                            values_Ca.insert(2, row["Analysis Method"])
                        except:
                            values_Ca.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Ca.insert(1, row["1SD"])
                            values_Ca.insert(2, row["Analysis Method"])

                elif row["Element"] == "Cadmium, Cd" and len(values_Cd) == 3:      
                    if row["Unit"] == "ppm":
                        values_Cd.insert(0, row["Certified Value"])                  
                        values_Cd.insert(1, row["1SD"])
                        values_Cd.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "ppb":
                        try:
                            values_Cd.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Cd.insert(1, (float(row["1SD"])*0.001))
                            values_Cd.insert(2, row["Analysis Method"])
                        except:
                            values_Cd.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Cd.insert(1, row["1SD"])
                            values_Cd.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "wt.%":
                        try:
                            values_Cd.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Cd.insert(1, (float(row["1SD"])*10000))
                            values_Cd.insert(2, row["Analysis Method"])
                        except:
                            values_Cd.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Cd.insert(1, row["1SD"])
                            values_Cd.insert(2, row["Analysis Method"])

                elif row["Element"] == "Cerium, Ce" and len(values_Ce) == 3:      
                    if row["Unit"] == "ppm":
                        values_Ce.insert(0, row["Certified Value"])                  
                        values_Ce.insert(1, row["1SD"])
                        values_Ce.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "ppb":
                        try:
                            values_Ce.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Ce.insert(1, (float(row["1SD"])*0.001))
                            values_Ce.insert(2, row["Analysis Method"])
                        except:
                            values_Ce.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Ce.insert(1, row["1SD"])
                            values_Ce.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "wt.%":
                        try:
                            values_Ce.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Ce.insert(1, (float(row["1SD"])*10000))
                            values_Ce.insert(2, row["Analysis Method"])
                        except:
                            values_Ce.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Ce.insert(1, row["1SD"])
                            values_Ce.insert(2, row["Analysis Method"])

                elif row["Element"] == "Chlorine, Cl" and len(values_Cl) == 3:      
                    if row["Unit"] == "ppm":
                        values_Cl.insert(0, row["Certified Value"])                  
                        values_Cl.insert(1, row["1SD"])
                        values_Cl.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "ppb":
                        try:
                            values_Cl.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Cl.insert(1, (float(row["1SD"])*0.001))
                            values_Cl.insert(2, row["Analysis Method"])
                        except:
                            values_Cl.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Cl.insert(1, row["1SD"])
                            values_Cl.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "wt.%":
                        try:
                            values_Cl.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Cl.insert(1, (float(row["1SD"])*10000))
                            values_Cl.insert(2, row["Analysis Method"])
                        except:
                            values_Cl.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Cl.insert(1, row["1SD"])
                            values_Cl.insert(2, row["Analysis Method"])

                elif row["Element"] == "Cobalt, Co" and len(values_Co) == 3:      
                    if row["Unit"] == "ppm":
                        values_Co.insert(0, row["Certified Value"])                  
                        values_Co.insert(1, row["1SD"])
                        values_Co.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "ppb":
                        try:
                            values_Co.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Co.insert(1, (float(row["1SD"])*0.001))
                            values_Co.insert(2, row["Analysis Method"])
                        except:
                            values_Co.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Co.insert(1, row["1SD"])
                            values_Co.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "wt.%":
                        try:
                            values_Co.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Co.insert(1, (float(row["1SD"])*10000))
                            values_Co.insert(2, row["Analysis Method"])
                        except:
                            values_Co.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Co.insert(1, row["1SD"])
                            values_Co.insert(2, row["Analysis Method"])

                elif row["Element"] == "Chromium, Cr" and len(values_Cr) == 3:      
                    if row["Unit"] == "ppm":
                        values_Cr.insert(0, row["Certified Value"])                  
                        values_Cr.insert(1, row["1SD"])
                        values_Cr.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "ppb":
                        try:
                            values_Cr.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Cr.insert(1, (float(row["1SD"])*0.001))
                            values_Cr.insert(2, row["Analysis Method"])
                        except:
                            values_Cr.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Cr.insert(1, row["1SD"])
                            values_Cr.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "wt.%":
                        try:
                            values_Cr.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Cr.insert(1, (float(row["1SD"])*10000))
                            values_Cr.insert(2, row["Analysis Method"])
                        except:
                            values_Cr.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Cr.insert(1, row["1SD"])
                            values_Cr.insert(2, row["Analysis Method"])

                elif row["Element"] == "Caesium, Cs" and len(values_Cs) == 3:      
                    if row["Unit"] == "ppm":
                        values_Cs.insert(0, row["Certified Value"])                  
                        values_Cs.insert(1, row["1SD"])
                        values_Cs.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "ppb":
                        try:
                            values_Cs.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Cs.insert(1, (float(row["1SD"])*0.001))
                            values_Cs.insert(2, row["Analysis Method"])
                        except:
                            values_Cs.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Cs.insert(1, row["1SD"])
                            values_Cs.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "wt.%":
                        try:
                            values_Cs.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Cs.insert(1, (float(row["1SD"])*10000))
                            values_Cs.insert(2, row["Analysis Method"])
                        except:
                            values_Cs.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Cs.insert(1, row["1SD"])
                            values_Cs.insert(2, row["Analysis Method"])

                elif row["Element"] == "Copper, Cu" and len(values_Cu) == 3:      
                    if row["Unit"] == "ppm":
                        values_Cu.insert(0, row["Certified Value"])                  
                        values_Cu.insert(1, row["1SD"])
                        values_Cu.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "ppb":
                        try:
                            values_Cu.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Cu.insert(1, (float(row["1SD"])*0.001))
                            values_Cu.insert(2, row["Analysis Method"])
                        except:
                            values_Cu.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Cu.insert(1, row["1SD"])
                            values_Cu.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "wt.%":
                        try:
                            values_Cu.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Cu.insert(1, (float(row["1SD"])*10000))
                            values_Cu.insert(2, row["Analysis Method"])
                        except:
                            values_Cu.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Cu.insert(1, row["1SD"])
                            values_Cu.insert(2, row["Analysis Method"])

                elif row["Element"] == "Dysprosium, Dy" and len(values_Dy) == 3:      
                    if row["Unit"] == "ppm":
                        values_Dy.insert(0, row["Certified Value"])                  
                        values_Dy.insert(1, row["1SD"])
                        values_Dy.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "ppb":
                        try:
                            values_Dy.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Dy.insert(1, (float(row["1SD"])*0.001))
                            values_Dy.insert(2, row["Analysis Method"])
                        except:
                            values_Dy.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Dy.insert(1, row["1SD"])
                            values_Dy.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "wt.%":
                        try:
                            values_Dy.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Dy.insert(1, (float(row["1SD"])*10000))
                            values_Dy.insert(2, row["Analysis Method"])
                        except:
                            values_Dy.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Dy.insert(1, row["1SD"])
                            values_Dy.insert(2, row["Analysis Method"])

                elif row["Element"] == "Erbium, Er" and len(values_Er) == 3:      
                    if row["Unit"] == "ppm":
                        values_Er.insert(0, row["Certified Value"])                  
                        values_Er.insert(1, row["1SD"])
                        values_Er.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "ppb":
                        try:
                            values_Er.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Er.insert(1, (float(row["1SD"])*0.001))
                            values_Er.insert(2, row["Analysis Method"])
                        except:
                            values_Er.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Er.insert(1, row["1SD"])
                            values_Er.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "wt.%":
                        try:
                            values_Er.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Er.insert(1, (float(row["1SD"])*10000))
                            values_Er.insert(2, row["Analysis Method"])
                        except:
                            values_Er.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Er.insert(1, row["1SD"])
                            values_Er.insert(2, row["Analysis Method"])

                elif row["Element"] == "Europium, Eu" and len(values_Eu) == 3:      
                    if row["Unit"] == "ppm":
                        values_Eu.insert(0, row["Certified Value"])                  
                        values_Eu.insert(1, row["1SD"])
                        values_Eu.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "ppb":
                        try:
                            values_Eu.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Eu.insert(1, (float(row["1SD"])*0.001))
                            values_Eu.insert(2, row["Analysis Method"])
                        except:
                            values_Eu.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Eu.insert(1, row["1SD"])
                            values_Eu.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "wt.%":
                        try:
                            values_Eu.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Eu.insert(1, (float(row["1SD"])*10000))
                            values_Eu.insert(2, row["Analysis Method"])
                        except:
                            values_Eu.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Eu.insert(1, row["1SD"])
                            values_Eu.insert(2, row["Analysis Method"])

                elif row["Element"] == "Iron, Fe" and len(values_Fe) == 3:      
                    if row["Unit"] == "ppm":
                        values_Fe.insert(0, row["Certified Value"])                  
                        values_Fe.insert(1, row["1SD"])
                        values_Fe.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "ppb":
                        try:
                            values_Fe.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Fe.insert(1, (float(row["1SD"])*0.001))
                            values_Fe.insert(2, row["Analysis Method"])
                        except:
                            values_Fe.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Fe.insert(1, row["1SD"])
                            values_Fe.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "wt.%":
                        try:
                            values_Fe.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Fe.insert(1, (float(row["1SD"])*10000))
                            values_Fe.insert(2, row["Analysis Method"])
                        except:
                            values_Fe.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Fe.insert(1, row["1SD"])
                            values_Fe.insert(2, row["Analysis Method"])

                elif row["Element"] == "Gallium, Ga" and len(values_Ga) == 3:      
                    if row["Unit"] == "ppm":
                        values_Ga.insert(0, row["Certified Value"])                  
                        values_Ga.insert(1, row["1SD"])
                        values_Ga.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "ppb":
                        try:
                            values_Ga.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Ga.insert(1, (float(row["1SD"])*0.001))
                            values_Ga.insert(2, row["Analysis Method"])
                        except:
                            values_Ga.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Ga.insert(1, row["1SD"])
                            values_Ga.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "wt.%":
                        try:
                            values_Ga.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Ga.insert(1, (float(row["1SD"])*10000))
                            values_Ga.insert(2, row["Analysis Method"])
                        except:
                            values_Ga.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Ga.insert(1, row["1SD"])
                            values_Ga.insert(2, row["Analysis Method"])

                elif row["Element"] == "Gadolinium, Gd" and len(values_Gd) == 3:      
                    if row["Unit"] == "ppm":
                        values_Gd.insert(0, row["Certified Value"])                  
                        values_Gd.insert(1, row["1SD"])
                        values_Gd.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "ppb":
                        try:
                            values_Gd.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Gd.insert(1, (float(row["1SD"])*0.001))
                            values_Gd.insert(2, row["Analysis Method"])
                        except:
                            values_Gd.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Gd.insert(1, row["1SD"])
                            values_Gd.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "wt.%":
                        try:
                            values_Gd.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Gd.insert(1, (float(row["1SD"])*10000))
                            values_Gd.insert(2, row["Analysis Method"])
                        except:
                            values_Gd.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Gd.insert(1, row["1SD"])
                            values_Gd.insert(2, row["Analysis Method"])

                elif row["Element"] == "Germanium, Ge" and len(values_Ge) == 3:      
                    if row["Unit"] == "ppm":
                        values_Ge.insert(0, row["Certified Value"])                  
                        values_Ge.insert(1, row["1SD"])
                        values_Ge.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "ppb":
                        try:
                            values_Ge.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Ge.insert(1, (float(row["1SD"])*0.001))
                            values_Ge.insert(2, row["Analysis Method"])
                        except:
                            values_Ge.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Ge.insert(1, row["1SD"])
                            values_Ge.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "wt.%":
                        try:
                            values_Ge.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Ge.insert(1, (float(row["1SD"])*10000))
                            values_Ge.insert(2, row["Analysis Method"])
                        except:
                            values_Ge.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Ge.insert(1, row["1SD"])
                            values_Ge.insert(2, row["Analysis Method"])

                elif row["Element"] == "Hafnium, Hf" and len(values_Hf) == 3:      
                    if row["Unit"] == "ppm":
                        values_Hf.insert(0, row["Certified Value"])                  
                        values_Hf.insert(1, row["1SD"])
                        values_Hf.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "ppb":
                        try:
                            values_Hf.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Hf.insert(1, (float(row["1SD"])*0.001))
                            values_Hf.insert(2, row["Analysis Method"])
                        except:
                            values_Hf.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Hf.insert(1, row["1SD"])
                            values_Hf.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "wt.%":
                        try:
                            values_Hf.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Hf.insert(1, (float(row["1SD"])*10000))
                            values_Hf.insert(2, row["Analysis Method"])
                        except:
                            values_Hf.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Hf.insert(1, row["1SD"])
                            values_Hf.insert(2, row["Analysis Method"])

                elif row["Element"] == "Mercury, Hg" and len(values_Hg) == 3:      
                    if row["Unit"] == "ppm":
                        values_Hg.insert(0, row["Certified Value"])                  
                        values_Hg.insert(1, row["1SD"])
                        values_Hg.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "ppb":
                        try:
                            values_Hg.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Hg.insert(1, (float(row["1SD"])*0.001))
                            values_Hg.insert(2, row["Analysis Method"])
                        except:
                            values_Hg.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Hg.insert(1, row["1SD"])
                            values_Hg.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "wt.%":
                        try:
                            values_Hg.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Hg.insert(1, (float(row["1SD"])*10000))
                            values_Hg.insert(2, row["Analysis Method"])
                        except:
                            values_Hg.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Hg.insert(1, row["1SD"])
                            values_Hg.insert(2, row["Analysis Method"])

                elif row["Element"] == "Holmium, Ho" and len(values_Ho) == 3:      
                    if row["Unit"] == "ppm":
                        values_Ho.insert(0, row["Certified Value"])                  
                        values_Ho.insert(1, row["1SD"])
                        values_Ho.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "ppb":
                        try:
                            values_Ho.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Ho.insert(1, (float(row["1SD"])*0.001))
                            values_Ho.insert(2, row["Analysis Method"])
                        except:
                            values_Ho.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Ho.insert(1, row["1SD"])
                            values_Ho.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "wt.%":
                        try:
                            values_Ho.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Ho.insert(1, (float(row["1SD"])*10000))
                            values_Ho.insert(2, row["Analysis Method"])
                        except:
                            values_Ho.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Ho.insert(1, row["1SD"])
                            values_Ho.insert(2, row["Analysis Method"])

                elif row["Element"] == "Indium, In" and len(values_In) == 3:      
                    if row["Unit"] == "ppm":
                        values_In.insert(0, row["Certified Value"])                  
                        values_In.insert(1, row["1SD"])
                        values_In.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "ppb":
                        try:
                            values_In.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_In.insert(1, (float(row["1SD"])*0.001))
                            values_In.insert(2, row["Analysis Method"])
                        except:
                            values_In.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_In.insert(1, row["1SD"])
                            values_In.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "wt.%":
                        try:
                            values_In.insert(0, (float(row["Certified Value"])*10000))                  
                            values_In.insert(1, (float(row["1SD"])*10000))
                            values_In.insert(2, row["Analysis Method"])
                        except:
                            values_In.insert(0, (float(row["Certified Value"])*10000))                  
                            values_In.insert(1, row["1SD"])
                            values_In.insert(2, row["Analysis Method"])

                elif row["Element"] == "Iridium, Ir" and len(values_Ir) == 3:      
                    if row["Unit"] == "ppm":
                        values_Ir.insert(0, row["Certified Value"])                  
                        values_Ir.insert(1, row["1SD"])
                        values_Ir.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "ppb":
                        try:
                            values_Ir.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Ir.insert(1, (float(row["1SD"])*0.001))
                            values_Ir.insert(2, row["Analysis Method"])
                        except:
                            values_Ir.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Ir.insert(1, row["1SD"])
                            values_Ir.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "wt.%":
                        try:
                            values_Ir.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Ir.insert(1, (float(row["1SD"])*10000))
                            values_Ir.insert(2, row["Analysis Method"])
                        except:
                            values_Ir.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Ir.insert(1, row["1SD"])
                            values_Ir.insert(2, row["Analysis Method"])

                elif row["Element"] == "Potassium, K" and len(values_K) == 3:      
                    if row["Unit"] == "ppm":
                        values_K.insert(0, row["Certified Value"])                  
                        values_K.insert(1, row["1SD"])
                        values_K.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "ppb":
                        try:
                            values_K.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_K.insert(1, (float(row["1SD"])*0.001))
                            values_K.insert(2, row["Analysis Method"])
                        except:
                            values_K.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_K.insert(1, row["1SD"])
                            values_K.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "wt.%":
                        try:
                            values_K.insert(0, (float(row["Certified Value"])*10000))                  
                            values_K.insert(1, (float(row["1SD"])*10000))
                            values_K.insert(2, row["Analysis Method"])
                        except:
                            values_K.insert(0, (float(row["Certified Value"])*10000))                  
                            values_K.insert(1, row["1SD"])
                            values_K.insert(2, row["Analysis Method"])

                elif row["Element"] == "Lanthanum, La" and len(values_La) == 3:      
                    if row["Unit"] == "ppm":
                        values_La.insert(0, row["Certified Value"])                  
                        values_La.insert(1, row["1SD"])
                        values_La.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "ppb":
                        try:
                            values_La.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_La.insert(1, (float(row["1SD"])*0.001))
                            values_La.insert(2, row["Analysis Method"])
                        except:
                            values_La.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_La.insert(1, row["1SD"])
                            values_La.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "wt.%":
                        try:
                            values_La.insert(0, (float(row["Certified Value"])*10000))                  
                            values_La.insert(1, (float(row["1SD"])*10000))
                            values_La.insert(2, row["Analysis Method"])
                        except:
                            values_La.insert(0, (float(row["Certified Value"])*10000))                  
                            values_La.insert(1, row["1SD"])
                            values_La.insert(2, row["Analysis Method"])

                elif row["Element"] == "Lithium, Li" and len(values_Li) == 3:      
                    if row["Unit"] == "ppm":
                        values_Li.insert(0, row["Certified Value"])                  
                        values_Li.insert(1, row["1SD"])
                        values_Li.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "ppb":
                        try:
                            values_Li.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Li.insert(1, (float(row["1SD"])*0.001))
                            values_Li.insert(2, row["Analysis Method"])
                        except:
                            values_Li.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Li.insert(1, row["1SD"])
                            values_Li.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "wt.%":
                        try:
                            values_Li.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Li.insert(1, (float(row["1SD"])*10000))
                            values_Li.insert(2, row["Analysis Method"])
                        except:
                            values_Li.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Li.insert(1, row["1SD"])
                            values_Li.insert(2, row["Analysis Method"])

                elif row["Element"] == "Lutetium, Lu" and len(values_Lu) == 3:      
                    if row["Unit"] == "ppm":
                        values_Lu.insert(0, row["Certified Value"])                  
                        values_Lu.insert(1, row["1SD"])
                        values_Lu.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "ppb":
                        try:
                            values_Lu.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Lu.insert(1, (float(row["1SD"])*0.001))
                            values_Lu.insert(2, row["Analysis Method"])
                        except:
                            values_Lu.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Lu.insert(1, row["1SD"])
                            values_Lu.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "wt.%":
                        try:
                            values_Lu.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Lu.insert(1, (float(row["1SD"])*10000))
                            values_Lu.insert(2, row["Analysis Method"])
                        except:
                            values_Lu.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Lu.insert(1, row["1SD"])
                            values_Lu.insert(2, row["Analysis Method"])

                elif row["Element"] == "Magnesium, Mg" and len(values_Mg) == 3:      
                    if row["Unit"] == "ppm":
                        values_Mg.insert(0, row["Certified Value"])                  
                        values_Mg.insert(1, row["1SD"])
                        values_Mg.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "ppb":
                        try:
                            values_Mg.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Mg.insert(1, (float(row["1SD"])*0.001))
                            values_Mg.insert(2, row["Analysis Method"])
                        except:
                            values_Mg.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Mg.insert(1, row["1SD"])
                            values_Mg.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "wt.%":
                        try:
                            values_Mg.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Mg.insert(1, (float(row["1SD"])*10000))
                            values_Mg.insert(2, row["Analysis Method"])
                        except:
                            values_Mg.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Mg.insert(1, row["1SD"])
                            values_Mg.insert(2, row["Analysis Method"])

                elif row["Element"] == "Manganese, Mn" and len(values_Mn) == 3:      
                    if row["Unit"] == "ppm":
                        values_Mn.insert(0, row["Certified Value"])                  
                        values_Mn.insert(1, row["1SD"])
                        values_Mn.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "ppb":
                        try:
                            values_Mn.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Mn.insert(1, (float(row["1SD"])*0.001))
                            values_Mn.insert(2, row["Analysis Method"])
                        except:
                            values_Mn.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Mn.insert(1, row["1SD"])
                            values_Mn.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "wt.%":
                        try:
                            values_Mn.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Mn.insert(1, (float(row["1SD"])*10000))
                            values_Mn.insert(2, row["Analysis Method"])
                        except:
                            values_Mn.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Mn.insert(1, row["1SD"])
                            values_Mn.insert(2, row["Analysis Method"])

                elif row["Element"] == "Molybdenum, Mo" and len(values_Mo) == 3:      
                    if row["Unit"] == "ppm":
                        values_Mo.insert(0, row["Certified Value"])                  
                        values_Mo.insert(1, row["1SD"])
                        values_Mo.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "ppb":
                        try:
                            values_Mo.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Mo.insert(1, (float(row["1SD"])*0.001))
                            values_Mo.insert(2, row["Analysis Method"])
                        except:
                            values_Mo.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Mo.insert(1, row["1SD"])
                            values_Mo.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "wt.%":
                        try:
                            values_Mo.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Mo.insert(1, (float(row["1SD"])*10000))
                            values_Mo.insert(2, row["Analysis Method"])
                        except:
                            values_Mo.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Mo.insert(1, row["1SD"])
                            values_Mo.insert(2, row["Analysis Method"])

                elif row["Element"] == "Sodium, Na" and len(values_Na) == 3:      
                    if row["Unit"] == "ppm":
                        values_Na.insert(0, row["Certified Value"])                  
                        values_Na.insert(1, row["1SD"])
                        values_Na.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "ppb":
                        try:
                            values_Na.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Na.insert(1, (float(row["1SD"])*0.001))
                            values_Na.insert(2, row["Analysis Method"])
                        except:
                            values_Na.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Na.insert(1, row["1SD"])
                            values_Na.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "wt.%":
                        try:
                            values_Na.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Na.insert(1, (float(row["1SD"])*10000))
                            values_Na.insert(2, row["Analysis Method"])
                        except:
                            values_Na.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Na.insert(1, row["1SD"])
                            values_Na.insert(2, row["Analysis Method"])

                elif row["Element"] == "Niobium, Nb" and len(values_Nb) == 3:      
                    if row["Unit"] == "ppm":
                        values_Nb.insert(0, row["Certified Value"])                  
                        values_Nb.insert(1, row["1SD"])
                        values_Nb.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "ppb":
                        try:
                            values_Nb.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Nb.insert(1, (float(row["1SD"])*0.001))
                            values_Nb.insert(2, row["Analysis Method"])
                        except:
                            values_Nb.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Nb.insert(1, row["1SD"])
                            values_Nb.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "wt.%":
                        try:
                            values_Nb.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Nb.insert(1, (float(row["1SD"])*10000))
                            values_Nb.insert(2, row["Analysis Method"])
                        except:
                            values_Nb.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Nb.insert(1, row["1SD"])
                            values_Nb.insert(2, row["Analysis Method"])

                elif row["Element"] == "Neodymium, Nd" and len(values_Nd) == 3:      
                    if row["Unit"] == "ppm":
                        values_Nd.insert(0, row["Certified Value"])                  
                        values_Nd.insert(1, row["1SD"])
                        values_Nd.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "ppb":
                        try:
                            values_Nd.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Nd.insert(1, (float(row["1SD"])*0.001))
                            values_Nd.insert(2, row["Analysis Method"])
                        except:
                            values_Nd.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Nd.insert(1, row["1SD"])
                            values_Nd.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "wt.%":
                        try:
                            values_Nd.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Nd.insert(1, (float(row["1SD"])*10000))
                            values_Nd.insert(2, row["Analysis Method"])
                        except:
                            values_Nd.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Nd.insert(1, row["1SD"])
                            values_Nd.insert(2, row["Analysis Method"])

                elif row["Element"] == "Nickel, Ni" and len(values_Ni) == 3:      
                    if row["Unit"] == "ppm":
                        values_Ni.insert(0, row["Certified Value"])                  
                        values_Ni.insert(1, row["1SD"])
                        values_Ni.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "ppb":
                        try:
                            values_Ni.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Ni.insert(1, (float(row["1SD"])*0.001))
                            values_Ni.insert(2, row["Analysis Method"])
                        except:
                            values_Ni.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Ni.insert(1, row["1SD"])
                            values_Ni.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "wt.%":
                        try:
                            values_Ni.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Ni.insert(1, (float(row["1SD"])*10000))
                            values_Ni.insert(2, row["Analysis Method"])
                        except:
                            values_Ni.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Ni.insert(1, row["1SD"])
                            values_Ni.insert(2, row["Analysis Method"])

                elif row["Element"] == "Osmium, Os" and len(values_Os) == 3:      
                    if row["Unit"] == "ppm":
                        values_Os.insert(0, row["Certified Value"])                  
                        values_Os.insert(1, row["1SD"])
                        values_Os.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "ppb":
                        try:
                            values_Os.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Os.insert(1, (float(row["1SD"])*0.001))
                            values_Os.insert(2, row["Analysis Method"])
                        except:
                            values_Os.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Os.insert(1, row["1SD"])
                            values_Os.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "wt.%":
                        try:
                            values_Os.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Os.insert(1, (float(row["1SD"])*10000))
                            values_Os.insert(2, row["Analysis Method"])
                        except:
                            values_Os.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Os.insert(1, row["1SD"])
                            values_Os.insert(2, row["Analysis Method"])

                elif row["Element"] == "Phosphorus, P" and len(values_P) == 3:      
                    if row["Unit"] == "ppm":
                        values_P.insert(0, row["Certified Value"])                  
                        values_P.insert(1, row["1SD"])
                        values_P.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "ppb":
                        try:
                            values_P.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_P.insert(1, (float(row["1SD"])*0.001))
                            values_P.insert(2, row["Analysis Method"])
                        except:
                            values_P.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_P.insert(1, row["1SD"])
                            values_P.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "wt.%":
                        try:
                            values_P.insert(0, (float(row["Certified Value"])*10000))                  
                            values_P.insert(1, (float(row["1SD"])*10000))
                            values_P.insert(2, row["Analysis Method"])
                        except:
                            values_P.insert(0, (float(row["Certified Value"])*10000))                  
                            values_P.insert(1, row["1SD"])
                            values_P.insert(2, row["Analysis Method"])

                elif row["Element"] == "Lead, Pb" and len(values_Pb) == 3:      
                    if row["Unit"] == "ppm":
                        values_Pb.insert(0, row["Certified Value"])                  
                        values_Pb.insert(1, row["1SD"])
                        values_Pb.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "ppb":
                        try:
                            values_Pb.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Pb.insert(1, (float(row["1SD"])*0.001))
                            values_Pb.insert(2, row["Analysis Method"])
                        except:
                            values_Pb.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Pb.insert(1, row["1SD"])
                            values_Pb.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "wt.%":
                        try:
                            values_Pb.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Pb.insert(1, (float(row["1SD"])*10000))
                            values_Pb.insert(2, row["Analysis Method"])
                        except:
                            values_Pb.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Pb.insert(1, row["1SD"])
                            values_Pb.insert(2, row["Analysis Method"])

                elif row["Element"] == "Palladium, Pd" and len(values_Pd) == 3:      
                    if row["Unit"] == "ppm":
                        values_Pd.insert(0, row["Certified Value"])                  
                        values_Pd.insert(1, row["1SD"])
                        values_Pd.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "ppb":
                        try:
                            values_Pd.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Pd.insert(1, (float(row["1SD"])*0.001))
                            values_Pd.insert(2, row["Analysis Method"])
                        except:
                            values_Pd.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Pd.insert(1, row["1SD"])
                            values_Pd.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "wt.%":
                        try:
                            values_Pd.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Pd.insert(1, (float(row["1SD"])*10000))
                            values_Pd.insert(2, row["Analysis Method"])
                        except:
                            values_Pd.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Pd.insert(1, row["1SD"])
                            values_Pd.insert(2, row["Analysis Method"])

                elif row["Element"] == "Praseodymium, Pr" and len(values_Pr) == 3:      
                    if row["Unit"] == "ppm":
                        values_Pr.insert(0, row["Certified Value"])                  
                        values_Pr.insert(1, row["1SD"])
                        values_Pr.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "ppb":
                        try:
                            values_Pr.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Pr.insert(1, (float(row["1SD"])*0.001))
                            values_Pr.insert(2, row["Analysis Method"])
                        except:
                            values_Pr.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Pr.insert(1, row["1SD"])
                            values_Pr.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "wt.%":
                        try:
                            values_Pr.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Pr.insert(1, (float(row["1SD"])*10000))
                            values_Pr.insert(2, row["Analysis Method"])
                        except:
                            values_Pr.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Pr.insert(1, row["1SD"])
                            values_Pr.insert(2, row["Analysis Method"])

                elif row["Element"] == "Platinum, Pt" and len(values_Pt) == 3:      
                    if row["Unit"] == "ppm":
                        values_Pt.insert(0, row["Certified Value"])                  
                        values_Pt.insert(1, row["1SD"])
                        values_Pt.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "ppb":
                        try:
                            values_Pt.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Pt.insert(1, (float(row["1SD"])*0.001))
                            values_Pt.insert(2, row["Analysis Method"])
                        except:
                            values_Pt.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Pt.insert(1, row["1SD"])
                            values_Pt.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "wt.%":
                        try:
                            values_Pt.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Pt.insert(1, (float(row["1SD"])*10000))
                            values_Pt.insert(2, row["Analysis Method"])
                        except:
                            values_Pt.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Pt.insert(1, row["1SD"])
                            values_Pt.insert(2, row["Analysis Method"])

                elif row["Element"] == "Rubidium, Rb" and len(values_Rb) == 3:      
                    if row["Unit"] == "ppm":
                        values_Rb.insert(0, row["Certified Value"])                  
                        values_Rb.insert(1, row["1SD"])
                        values_Rb.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "ppb":
                        try:
                            values_Rb.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Rb.insert(1, (float(row["1SD"])*0.001))
                            values_Rb.insert(2, row["Analysis Method"])
                        except:
                            values_Rb.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Rb.insert(1, row["1SD"])
                            values_Rb.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "wt.%":
                        try:
                            values_Rb.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Rb.insert(1, (float(row["1SD"])*10000))
                            values_Rb.insert(2, row["Analysis Method"])
                        except:
                            values_Rb.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Rb.insert(1, row["1SD"])
                            values_Rb.insert(2, row["Analysis Method"])

                elif row["Element"] == "Rhenium, Re" and len(values_Re) == 3:      
                    if row["Unit"] == "ppm":
                        values_Re.insert(0, row["Certified Value"])                  
                        values_Re.insert(1, row["1SD"])
                        values_Re.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "ppb":
                        try:
                            values_Re.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Re.insert(1, (float(row["1SD"])*0.001))
                            values_Re.insert(2, row["Analysis Method"])
                        except:
                            values_Re.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Re.insert(1, row["1SD"])
                            values_Re.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "wt.%":
                        try:
                            values_Re.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Re.insert(1, (float(row["1SD"])*10000))
                            values_Re.insert(2, row["Analysis Method"])
                        except:
                            values_Re.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Re.insert(1, row["1SD"])
                            values_Re.insert(2, row["Analysis Method"])

                elif row["Element"] == "Rhodium, Rh" and len(values_Rh) == 3:      
                    if row["Unit"] == "ppm":
                        values_Rh.insert(0, row["Certified Value"])                  
                        values_Rh.insert(1, row["1SD"])
                        values_Rh.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "ppb":
                        try:
                            values_Rh.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Rh.insert(1, (float(row["1SD"])*0.001))
                            values_Rh.insert(2, row["Analysis Method"])
                        except:
                            values_Rh.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Rh.insert(1, row["1SD"])
                            values_Rh.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "wt.%":
                        try:
                            values_Rh.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Rh.insert(1, (float(row["1SD"])*10000))
                            values_Rh.insert(2, row["Analysis Method"])
                        except:
                            values_Rh.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Rh.insert(1, row["1SD"])
                            values_Rh.insert(2, row["Analysis Method"])

                elif row["Element"] == "Ruthenium, Ru" and len(values_Ru) == 3:      
                    if row["Unit"] == "ppm":
                        values_Ru.insert(0, row["Certified Value"])                  
                        values_Ru.insert(1, row["1SD"])
                        values_Ru.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "ppb":
                        try:
                            values_Ru.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Ru.insert(1, (float(row["1SD"])*0.001))
                            values_Ru.insert(2, row["Analysis Method"])
                        except:
                            values_Ru.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Ru.insert(1, row["1SD"])
                            values_Ru.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "wt.%":
                        try:
                            values_Ru.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Ru.insert(1, (float(row["1SD"])*10000))
                            values_Ru.insert(2, row["Analysis Method"])
                        except:
                            values_Ru.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Ru.insert(1, row["1SD"])
                            values_Ru.insert(2, row["Analysis Method"])

                elif row["Element"] == "Sulphur, S" and len(values_S) == 3:      
                    if row["Unit"] == "ppm":
                        values_S.insert(0, row["Certified Value"])                  
                        values_S.insert(1, row["1SD"])
                        values_S.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "ppb":
                        try:
                            values_S.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_S.insert(1, (float(row["1SD"])*0.001))
                            values_S.insert(2, row["Analysis Method"])
                        except:
                            values_S.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_S.insert(1, row["1SD"])
                            values_S.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "wt.%":
                        try:
                            values_S.insert(0, (float(row["Certified Value"])*10000))                  
                            values_S.insert(1, (float(row["1SD"])*10000))
                            values_S.insert(2, row["Analysis Method"])
                        except:
                            values_S.insert(0, (float(row["Certified Value"])*10000))                  
                            values_S.insert(1, row["1SD"])
                            values_S.insert(2, row["Analysis Method"])

                elif row["Element"] == "Antimony, Sb" and len(values_Sb) == 3:      
                    if row["Unit"] == "ppm":
                        values_Sb.insert(0, row["Certified Value"])                  
                        values_Sb.insert(1, row["1SD"])
                        values_Sb.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "ppb":
                        try:
                            values_Sb.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Sb.insert(1, (float(row["1SD"])*0.001))
                            values_Sb.insert(2, row["Analysis Method"])
                        except:
                            values_Sb.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Sb.insert(1, row["1SD"])
                            values_Sb.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "wt.%":
                        try:
                            values_Sb.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Sb.insert(1, (float(row["1SD"])*10000))
                            values_Sb.insert(2, row["Analysis Method"])
                        except:
                            values_Sb.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Sb.insert(1, row["1SD"])
                            values_Sb.insert(2, row["Analysis Method"])

                elif row["Element"] == "Scandium, Sc" and len(values_Sc) == 3:      
                    if row["Unit"] == "ppm":
                        values_Sc.insert(0, row["Certified Value"])                  
                        values_Sc.insert(1, row["1SD"])
                        values_Sc.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "ppb":
                        try:
                            values_Sc.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Sc.insert(1, (float(row["1SD"])*0.001))
                            values_Sc.insert(2, row["Analysis Method"])
                        except:
                            values_Sc.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Sc.insert(1, row["1SD"])
                            values_Sc.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "wt.%":
                        try:
                            values_Sc.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Sc.insert(1, (float(row["1SD"])*10000))
                            values_Sc.insert(2, row["Analysis Method"])
                        except:
                            values_Sc.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Sc.insert(1, row["1SD"])
                            values_Sc.insert(2, row["Analysis Method"])

                elif row["Element"] == "Selenium, Se" and len(values_Se) == 3:      
                    if row["Unit"] == "ppm":
                        values_Se.insert(0, row["Certified Value"])                  
                        values_Se.insert(1, row["1SD"])
                        values_Se.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "ppb":
                        try:
                            values_Se.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Se.insert(1, (float(row["1SD"])*0.001))
                            values_Se.insert(2, row["Analysis Method"])
                        except:
                            values_Se.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Se.insert(1, row["1SD"])
                            values_Se.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "wt.%":
                        try:
                            values_Se.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Se.insert(1, (float(row["1SD"])*10000))
                            values_Se.insert(2, row["Analysis Method"])
                        except:
                            values_Se.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Se.insert(1, row["1SD"])
                            values_Se.insert(2, row["Analysis Method"])

                elif row["Element"] == "Silicon, Si" and len(values_Si) == 3:      
                    if row["Unit"] == "ppm":
                        values_Si.insert(0, row["Certified Value"])                  
                        values_Si.insert(1, row["1SD"])
                        values_Si.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "ppb":
                        try:
                            values_Si.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Si.insert(1, (float(row["1SD"])*0.001))
                            values_Si.insert(2, row["Analysis Method"])
                        except:
                            values_Si.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Si.insert(1, row["1SD"])
                            values_Si.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "wt.%":
                        try:
                            values_Si.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Si.insert(1, (float(row["1SD"])*10000))
                            values_Si.insert(2, row["Analysis Method"])
                        except:
                            values_Si.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Si.insert(1, row["1SD"])
                            values_Si.insert(2, row["Analysis Method"])

                elif row["Element"] == "Samarium, Sm" and len(values_Sm) == 3:      
                    if row["Unit"] == "ppm":
                        values_Sm.insert(0, row["Certified Value"])                  
                        values_Sm.insert(1, row["1SD"])
                        values_Sm.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "ppb":
                        try:
                            values_Sm.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Sm.insert(1, (float(row["1SD"])*0.001))
                            values_Sm.insert(2, row["Analysis Method"])
                        except:
                            values_Sm.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Sm.insert(1, row["1SD"])
                            values_Sm.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "wt.%":
                        try:
                            values_Sm.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Sm.insert(1, (float(row["1SD"])*10000))
                            values_Sm.insert(2, row["Analysis Method"])
                        except:
                            values_Sm.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Sm.insert(1, row["1SD"])
                            values_Sm.insert(2, row["Analysis Method"])

                elif row["Element"] == "Tin, Sn" and len(values_Sn) == 3:      
                    if row["Unit"] == "ppm":
                        values_Sn.insert(0, row["Certified Value"])                  
                        values_Sn.insert(1, row["1SD"])
                        values_Sn.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "ppb":
                        try:
                            values_Sn.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Sn.insert(1, (float(row["1SD"])*0.001))
                            values_Sn.insert(2, row["Analysis Method"])
                        except:
                            values_Sn.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Sn.insert(1, row["1SD"])
                            values_Sn.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "wt.%":
                        try:
                            values_Sn.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Sn.insert(1, (float(row["1SD"])*10000))
                            values_Sn.insert(2, row["Analysis Method"])
                        except:
                            values_Sn.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Sn.insert(1, row["1SD"])
                            values_Sn.insert(2, row["Analysis Method"])

                elif row["Element"] == "Strontium, Sr" and len(values_Sr) == 3:      
                    if row["Unit"] == "ppm":
                        values_Sr.insert(0, row["Certified Value"])                  
                        values_Sr.insert(1, row["1SD"])
                        values_Sr.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "ppb":
                        try:
                            values_Sr.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Sr.insert(1, (float(row["1SD"])*0.001))
                            values_Sr.insert(2, row["Analysis Method"])
                        except:
                            values_Sr.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Sr.insert(1, row["1SD"])
                            values_Sr.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "wt.%":
                        try:
                            values_Sr.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Sr.insert(1, (float(row["1SD"])*10000))
                            values_Sr.insert(2, row["Analysis Method"])
                        except:
                            values_Sr.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Sr.insert(1, row["1SD"])
                            values_Sr.insert(2, row["Analysis Method"])

                elif row["Element"] == "Tantalum, Ta" and len(values_Ta) == 3:      
                    if row["Unit"] == "ppm":
                        values_Ta.insert(0, row["Certified Value"])                  
                        values_Ta.insert(1, row["1SD"])
                        values_Ta.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "ppb":
                        try:
                            values_Ta.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Ta.insert(1, (float(row["1SD"])*0.001))
                            values_Ta.insert(2, row["Analysis Method"])
                        except:
                            values_Ta.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Ta.insert(1, row["1SD"])
                            values_Ta.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "wt.%":
                        try:
                            values_Ta.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Ta.insert(1, (float(row["1SD"])*10000))
                            values_Ta.insert(2, row["Analysis Method"])
                        except:
                            values_Ta.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Ta.insert(1, row["1SD"])
                            values_Ta.insert(2, row["Analysis Method"])

                elif row["Element"] == "Terbium, Tb" and len(values_Tb) == 3:      
                    if row["Unit"] == "ppm":
                        values_Tb.insert(0, row["Certified Value"])                  
                        values_Tb.insert(1, row["1SD"])
                        values_Tb.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "ppb":
                        try:
                            values_Tb.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Tb.insert(1, (float(row["1SD"])*0.001))
                            values_Tb.insert(2, row["Analysis Method"])
                        except:
                            values_Tb.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Tb.insert(1, row["1SD"])
                            values_Tb.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "wt.%":
                        try:
                            values_Tb.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Tb.insert(1, (float(row["1SD"])*10000))
                            values_Tb.insert(2, row["Analysis Method"])
                        except:
                            values_Tb.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Tb.insert(1, row["1SD"])
                            values_Tb.insert(2, row["Analysis Method"])

                elif row["Element"] == "Tellurium, Te" and len(values_Te) == 3:      
                    if row["Unit"] == "ppm":
                        values_Te.insert(0, row["Certified Value"])                  
                        values_Te.insert(1, row["1SD"])
                        values_Te.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "ppb":
                        try:
                            values_Te.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Te.insert(1, (float(row["1SD"])*0.001))
                            values_Te.insert(2, row["Analysis Method"])
                        except:
                            values_Te.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Te.insert(1, row["1SD"])
                            values_Te.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "wt.%":
                        try:
                            values_Te.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Te.insert(1, (float(row["1SD"])*10000))
                            values_Te.insert(2, row["Analysis Method"])
                        except:
                            values_Te.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Te.insert(1, row["1SD"])
                            values_Te.insert(2, row["Analysis Method"])

                elif row["Element"] == "Thorium, Th" and len(values_Th) == 3:      
                    if row["Unit"] == "ppm":
                        values_Th.insert(0, row["Certified Value"])                  
                        values_Th.insert(1, row["1SD"])
                        values_Th.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "ppb":
                        try:
                            values_Th.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Th.insert(1, (float(row["1SD"])*0.001))
                            values_Th.insert(2, row["Analysis Method"])
                        except:
                            values_Th.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Th.insert(1, row["1SD"])
                            values_Th.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "wt.%":
                        try:
                            values_Th.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Th.insert(1, (float(row["1SD"])*10000))
                            values_Th.insert(2, row["Analysis Method"])
                        except:
                            values_Th.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Th.insert(1, row["1SD"])
                            values_Th.insert(2, row["Analysis Method"])

                elif row["Element"] == "Titanium, Ti" and len(values_Ti) == 3:      
                    if row["Unit"] == "ppm":
                        values_Ti.insert(0, row["Certified Value"])                  
                        values_Ti.insert(1, row["1SD"])
                        values_Ti.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "ppb":
                        try:
                            values_Ti.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Ti.insert(1, (float(row["1SD"])*0.001))
                            values_Ti.insert(2, row["Analysis Method"])
                        except:
                            values_Ti.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Ti.insert(1, row["1SD"])
                            values_Ti.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "wt.%":
                        try:
                            values_Ti.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Ti.insert(1, (float(row["1SD"])*10000))
                            values_Ti.insert(2, row["Analysis Method"])
                        except:
                            values_Ti.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Ti.insert(1, row["1SD"])
                            values_Ti.insert(2, row["Analysis Method"])

                elif row["Element"] == "Thallium, Tl" and len(values_Tl) == 3:      
                    if row["Unit"] == "ppm":
                        values_Tl.insert(0, row["Certified Value"])                  
                        values_Tl.insert(1, row["1SD"])
                        values_Tl.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "ppb":
                        try:
                            values_Tl.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Tl.insert(1, (float(row["1SD"])*0.001))
                            values_Tl.insert(2, row["Analysis Method"])
                        except:
                            values_Tl.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Tl.insert(1, row["1SD"])
                            values_Tl.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "wt.%":
                        try:
                            values_Tl.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Tl.insert(1, (float(row["1SD"])*10000))
                            values_Tl.insert(2, row["Analysis Method"])
                        except:
                            values_Tl.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Tl.insert(1, row["1SD"])
                            values_Tl.insert(2, row["Analysis Method"])

                elif row["Element"] == "Thulium, Tm" and len(values_Tm) == 3:      
                    if row["Unit"] == "ppm":
                        values_Tm.insert(0, row["Certified Value"])                  
                        values_Tm.insert(1, row["1SD"])
                        values_Tm.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "ppb":
                        try:
                            values_Tm.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Tm.insert(1, (float(row["1SD"])*0.001))
                            values_Tm.insert(2, row["Analysis Method"])
                        except:
                            values_Tm.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Tm.insert(1, row["1SD"])
                            values_Tm.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "wt.%":
                        try:
                            values_Tm.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Tm.insert(1, (float(row["1SD"])*10000))
                            values_Tm.insert(2, row["Analysis Method"])
                        except:
                            values_Tm.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Tm.insert(1, row["1SD"])
                            values_Tm.insert(2, row["Analysis Method"])

                elif row["Element"] == "Uranium, U" and len(values_U) == 3:      
                    if row["Unit"] == "ppm":
                        values_U.insert(0, row["Certified Value"])                  
                        values_U.insert(1, row["1SD"])
                        values_U.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "ppb":
                        try:
                            values_U.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_U.insert(1, (float(row["1SD"])*0.001))
                            values_U.insert(2, row["Analysis Method"])
                        except:
                            values_U.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_U.insert(1, row["1SD"])
                            values_U.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "wt.%":
                        try:
                            values_U.insert(0, (float(row["Certified Value"])*10000))                  
                            values_U.insert(1, (float(row["1SD"])*10000))
                            values_U.insert(2, row["Analysis Method"])
                        except:
                            values_U.insert(0, (float(row["Certified Value"])*10000))                  
                            values_U.insert(1, row["1SD"])
                            values_U.insert(2, row["Analysis Method"])

                elif row["Element"] == "Vanadium, V" and len(values_V) == 3:      
                    if row["Unit"] == "ppm":
                        values_V.insert(0, row["Certified Value"])                  
                        values_V.insert(1, row["1SD"])
                        values_V.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "ppb":
                        try:
                            values_V.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_V.insert(1, (float(row["1SD"])*0.001))
                            values_V.insert(2, row["Analysis Method"])
                        except:
                            values_V.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_V.insert(1, row["1SD"])
                            values_V.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "wt.%":
                        try:
                            values_V.insert(0, (float(row["Certified Value"])*10000))                  
                            values_V.insert(1, (float(row["1SD"])*10000))
                            values_V.insert(2, row["Analysis Method"])
                        except:
                            values_V.insert(0, (float(row["Certified Value"])*10000))                  
                            values_V.insert(1, row["1SD"])
                            values_V.insert(2, row["Analysis Method"])

                elif row["Element"] == "Tungsten, W" and len(values_W) == 3:      
                    if row["Unit"] == "ppm":
                        values_W.insert(0, row["Certified Value"])                  
                        values_W.insert(1, row["1SD"])
                        values_W.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "ppb":
                        try:
                            values_W.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_W.insert(1, (float(row["1SD"])*0.001))
                            values_W.insert(2, row["Analysis Method"])
                        except:
                            values_W.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_W.insert(1, row["1SD"])
                            values_W.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "wt.%":
                        try:
                            values_W.insert(0, (float(row["Certified Value"])*10000))                  
                            values_W.insert(1, (float(row["1SD"])*10000))
                            values_W.insert(2, row["Analysis Method"])
                        except:
                            values_W.insert(0, (float(row["Certified Value"])*10000))                  
                            values_W.insert(1, row["1SD"])
                            values_W.insert(2, row["Analysis Method"])

                elif row["Element"] == "Yttrium, Y" and len(values_Y) == 3:      
                    if row["Unit"] == "ppm":
                        values_Y.insert(0, row["Certified Value"])                  
                        values_Y.insert(1, row["1SD"])
                        values_Y.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "ppb":
                        try:
                            values_Y.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Y.insert(1, (float(row["1SD"])*0.001))
                            values_Y.insert(2, row["Analysis Method"])
                        except:
                            values_Y.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Y.insert(1, row["1SD"])
                            values_Y.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "wt.%":
                        try:
                            values_Y.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Y.insert(1, (float(row["1SD"])*10000))
                            values_Y.insert(2, row["Analysis Method"])
                        except:
                            values_Y.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Y.insert(1, row["1SD"])
                            values_Y.insert(2, row["Analysis Method"])

                elif row["Element"] == "Ytterbium, Yb" and len(values_Yb) == 3:      
                    if row["Unit"] == "ppm":
                        values_Yb.insert(0, row["Certified Value"])                  
                        values_Yb.insert(1, row["1SD"])
                        values_Yb.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "ppb":
                        try:
                            values_Yb.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Yb.insert(1, (float(row["1SD"])*0.001))
                            values_Yb.insert(2, row["Analysis Method"])
                        except:
                            values_Yb.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Yb.insert(1, row["1SD"])
                            values_Yb.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "wt.%":
                        try:
                            values_Yb.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Yb.insert(1, (float(row["1SD"])*10000))
                            values_Yb.insert(2, row["Analysis Method"])
                        except:
                            values_Yb.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Yb.insert(1, row["1SD"])
                            values_Yb.insert(2, row["Analysis Method"])

                elif row["Element"] == "Zinc, Zn" and len(values_Zn) == 3:      
                    if row["Unit"] == "ppm":
                        values_Zn.insert(0, row["Certified Value"])                  
                        values_Zn.insert(1, row["1SD"])
                        values_Zn.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "ppb":
                        try:
                            values_Zn.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Zn.insert(1, (float(row["1SD"])*0.001))
                            values_Zn.insert(2, row["Analysis Method"])
                        except:
                            values_Zn.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Zn.insert(1, row["1SD"])
                            values_Zn.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "wt.%":
                        try:
                            values_Zn.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Zn.insert(1, (float(row["1SD"])*10000))
                            values_Zn.insert(2, row["Analysis Method"])
                        except:
                            values_Zn.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Zn.insert(1, row["1SD"])
                            values_Zn.insert(2, row["Analysis Method"])

                elif row["Element"] == "Zirconium, Zr" and len(values_Zr) == 3:      
                    if row["Unit"] == "ppm":
                        values_Zr.insert(0, row["Certified Value"])                  
                        values_Zr.insert(1, row["1SD"])
                        values_Zr.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "ppb":
                        try:
                            values_Zr.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Zr.insert(1, (float(row["1SD"])*0.001))
                            values_Zr.insert(2, row["Analysis Method"])
                        except:
                            values_Zr.insert(0, (float(row["Certified Value"])*0.001))                  
                            values_Zr.insert(1, row["1SD"])
                            values_Zr.insert(2, row["Analysis Method"])
                    elif row["Unit"] == "wt.%":
                        try:
                            values_Zr.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Zr.insert(1, (float(row["1SD"])*10000))
                            values_Zr.insert(2, row["Analysis Method"])
                        except:
                            values_Zr.insert(0, (float(row["Certified Value"])*10000))                  
                            values_Zr.insert(1, row["1SD"])
                            values_Zr.insert(2, row["Analysis Method"])

    global outputArray
    outputArray = crmNum + values_Geology[0:2] + spacer + values_Ag [0:3] + values_Al[0:3] + values_As[0:3] + values_Au[0:3] + values_B[0:3] + values_Ba[0:3] + values_Be[0:3] + values_Bi[0:3] + values_C[0:3] + values_Ca[0:3] + values_Cd[0:3] + values_Ce[0:3] + values_Cl[0:3] + values_Co[0:3] + values_Cr[0:3] + values_Cs[0:3] + values_Cu[0:3] + values_Dy[0:3] + values_Er[0:3] + values_Eu[0:3] + values_Fe[0:3] + values_Ga[0:3] + values_Gd[0:3] + values_Ge[0:3] + values_Hf[0:3] + values_Hg[0:3] + values_Ho[0:3] + values_In[0:3] + values_Ir[0:3] + values_K[0:3] + values_La[0:3] + values_Li[0:3] + values_Lu[0:3] + values_Mg[0:3] + values_Mn[0:3] + values_Mo[0:3] + values_Na[0:3] + values_Nb[0:3] + values_Nd[0:3] + values_Ni[0:3] + values_Os[0:3] + values_P[0:3] + values_Pb[0:3] + values_Pd[0:3] + values_Pr[0:3] + values_Pt[0:3] + values_Rb[0:3] + values_Re[0:3] + values_Rh[0:3] + values_Ru[0:3] + values_S[0:3] + values_Sb[0:3] + values_Sc[0:3] + values_Se[0:3] + values_Si[0:3] + values_Sm[0:3] + values_Sn[0:3] + values_Sr[0:3] + values_Ta[0:3] + values_Tb[0:3] + values_Te[0:3] + values_Th[0:3] + values_Ti[0:3] + values_Tl[0:3] + values_Tm[0:3] + values_U[0:3] + values_V[0:3] + values_W[0:3] + values_Y[0:3] + values_Yb[0:3] + values_Zn[0:3] + values_Zr[0:3]


def writeCSV():                             # Writes data in outputArray to output.csv

    with open('output.csv', mode='w') as output_file:
        writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(outputArray)
    print("output.csv was written successfully.")


getInput()
fillValues(crmID)
writeCSV()
input("Press Enter to continue...")

    

