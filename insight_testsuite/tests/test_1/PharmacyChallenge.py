class DrugList:

    
    def reading(self,file_name,header=True):
        
        self.file_name=file_name
        self.header=header
        with open(self.file_name) as infile:
            cost_drug={}
            if self.header:
                next(infile)
            h=0
            for currentline in infile:
                ### store the first name on the list. This method is used since the prescirbers are listed alphabetically ascending
                if h==0:
                    h+=1
                    current_prescriber=currentline.split(',')[1]+' '+currentline.split(',')[2]
                line_in=line_list(currentline)
                ########### There is either a health Care provider or missing First/Last name. Therefore, we skip
                if len(line_in)==4:
                    continue
                else:
                    name,drug,cost=elements(line_in)
                cost_drug,current_prescriber=generate_table(cost_drug,current_prescriber,drug,name,cost)
            st="drug_name,num_prescriber,total_cost"
        return(sort_output(cost_drug,st))
    
    
########### spliting lines into columns of given variables depending on the separator
    
def line_list(givenline):
    
    temp=givenline.split(',"')
    line=[]
    for i in temp:
        if i.find('"')== -1:
            line.append(i.split(','))
        else:
            line.append([i.split('"')[0]])
            i=i.split('"')[1:][0]
            line.append(i.split(',')[:])
    line=sum(line,[])
    try:
        line.remove('')
    except ValueError:
        pass
    return(line)


########### Extract prescriber first+last name, drug cost, and the drug name

def elements(line):
    
    pres_name=line[1]+' '+line[2]
    drug_name=line[-2]
    drug_cost=round(float(line[-1]),2)
    return(pres_name,drug_name,drug_cost)

########### Genertae a list of unique drug names along with total cost and total unique prescribers individuals
   
def generate_table(cost_drug,prescriber,drug,name,cost):
    
    if drug in cost_drug:
        cost_drug[drug][1]+=cost
        if name!=prescriber:
            cost_drug[drug][0]+=1
            prescriber=name
    else:
        cost_drug[drug]=[1]
        cost_drug[drug].append(cost)
    return(cost_drug,prescriber)
   
########### Sort output in Desc of the total cost and if there is a tie,in Asc order of the drug name

def sort_output(drug_list,string):
    
    string_new=string
    sorted_cost=sorted(drug_list.items(), key=lambda item: (-item[1][1],item))
    for drug in sorted_cost:
        string_new = string_new +'\n'+ drug[0] +','+ str(drug[1][0])+','+str(drug[1][1])
    return(string_new)

output=DrugList().reading("../input/itcont.txt")
outputFile = open("../output/top_cost_drug.txt", "w")
outputFile.write(output)
outputFile.close()


      
   
