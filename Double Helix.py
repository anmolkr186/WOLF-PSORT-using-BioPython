
# Project made by Team Double Helix


import urllib.request   
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML 
import time
from selenium import webdriver
from tkinter import *
import tkinter as tk


window = Tk()
window.title("Sub-localization Predictor Software")
window.geometry('600x300')
lbl = Label(window, text="ENTER ACCESSION NUMBER")
lbl1 = Label(window, text="ENTER PROTEIN SEQUENCE")


#resu.grid(column=0, row=2)
lbl.grid(column=25, row=25)
lbl1.grid(column=25, row=26)
txt = Entry(window,width=20)
txt1 = Entry(window,width=20)
txt2 = Entry(window,width=20)
txt.grid(column=26, row=25)
txt1.grid(column=26, row=26)
#txt2.grid(column=1, row=2)


def clicked1():
	#res = txt.get()
	#resu.configure(text= res)
    acc = txt.get()
    link= "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=protein&id="+ acc +"&rettype=fasta&retmode=text"
    data = urllib.request.urlopen(link)
    seq  = str(data.read())
    abc= seq.split()
    seq = abc[len(abc)-1]
    # print(seq)
    x =seq.find("\\")
    seq = seq [x+2:len(seq)-1]
    seq = seq.replace("\\n","")
    print(seq)
    app = ExampleApp(seq)
    app.mainloop()

def clicked2():
    #res = txt.get()
    #resu.configure(text= res)
    seq = txt1.get()
    print(seq)
    app = ExampleApp(seq)
    app.mainloop()
        
        
btn = Button(window, text="Find using accession Number", command=clicked1)
btn.grid(column=28, row=25)
btn = Button(window, text="Find using sequence", command=clicked2)
btn.grid(column=28, row=26)

class ExampleApp(tk.Tk):
    def __init__(self,seq):
        tk.Tk.__init__(self)

        # link= "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=protein&id=AAB30058.2&rettype=fasta&retmode=text"
        # data = urllib.request.urlopen(link)
        # seq  = str(data.read())
        # seqfinal  = seq[2:len(seq)-1]
        # print(seqfinal.replace("\\n",""))

        save_file1 = open("seq.fasta","w")
        save_file1.write(seq)
        save_file1.close()

        sequence_data = open("seq.fasta").read() 
        result = NCBIWWW.qblast("blastp", "pdb", sequence_data)
        save_file = open("blast.xml","w")
        save_file.write(result.read())
        save_file.close()
        result.close()


        blast = NCBIXML.parse(open('blast.xml','r'))
        ac_id = ""
        for record in blast:
            if record.alignments:
                ac_id =record.alignments[0].accession
                print("Accesion ID: " +  ac_id)
                print("E-Score: " +  str(record.alignments[0].hsps[0].expect))
                print("Score: " +  str(record.alignments[0].hsps[0].score))
                break


        link2= "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=protein&id="+str(ac_id)+"&rettype=fasta&retmode=text"
        print(link2)

        data2 = urllib.request.urlopen(link2)
        seq2  = str(data2.read())
        seqfinal2  = seq2[2:len(seq2)-1]
        seqfinal2 = seqfinal2.replace('\\n','')
        #print(seqfinal2)

        arr = seqfinal2.split()

        psort_seq = seq

        print(psort_seq)
        
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        #options.add_argument('--window-size=1920x1080')
        #options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(executable_path=r'C:\chromedriver.exe',chrome_options=options)
        driver.get('https://wolfpsort.hgc.jp/')

        animal_checkbox = driver.find_element_by_xpath("/html/body/div/form/table/tbody/tr[1]/td[1]/p[1]/input[1]")
        text_checkbox = driver.find_element_by_xpath("/html/body/div/form/table/tbody/tr[1]/td[1]/p[2]/input[1]")
        submit_checkbox = driver.find_element_by_xpath("/html/body/div/form/table/tbody/tr[2]/td/p/input[1]")
        textarea = driver.find_element_by_xpath("/html/body/div/form/table/tbody/tr[2]/td/p/textarea")

        animal_checkbox.click()
        text_checkbox.click()

        textarea.send_keys(psort_seq)

        submit_checkbox.click()

        time.sleep(20)

        el = driver.find_element_by_xpath("/html/body").text
        qwerty=el.index("details")
        sad=el[qwerty+7:]
        print(sad)

        final_result = sad.split(",")
        org_names = []
        org_names.append("")
        percent = []
        percent.append("")

        for i in final_result:
            sliced_name = i.split(":") 
            org_names.append(sliced_name[0])
            percent.append(sliced_name[1])

        t = SimpleTable(self, len(final_result)+1,2)
        t.pack(side="top", fill="x")

        t.set(0,0,"Organelle Name")
        t.set(0,1,"Localization percentage")

        for i in range(1,len(final_result)+1):
            t.set(i,0,org_names[i])
            t.set(i,1,percent[i])


class SimpleTable(tk.Frame):
    def __init__(self, parent, rows=10, columns=2):
        # use black background so it "peeks through" to 
        # form grid lines
        tk.Frame.__init__(self, parent, background="black")
        self._widgets = []
        for row in range(rows):
            current_row = []
            for column in range(columns):
                label = tk.Label(self, text="%s/%s" % (row, column), 
                                 borderwidth=0, width=50)
                label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                current_row.append(label)
            self._widgets.append(current_row)

        for column in range(columns):
            self.grid_columnconfigure(column, weight=1)


    def set(self, row, column, value):
        widget = self._widgets[row][column]
        widget.configure(text=value)

#if __name__ == "__main__":
 #   app = ExampleApp()
  #  app.mainloop()


mainloop()
window.mainloop()

