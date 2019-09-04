journal_f=open("J_Medline.txt","r")
lines=journal_f.readlines()
j_dic={}
j_dic2={}
j_name=""
j_abbr=""
for i in range(len(lines)):
    if lines[i].startswith("JournalTitle"):
        j_name=lines[i].split("JournalTitle:")[1]
        if lines[i+1].startswith("MedAbbr:"):
            j_abbr=lines[i+1].split("MedAbbr:")[1]
            j_dic[j_name.strip()]=j_abbr.strip()
            j_dic2[j_name.strip()]=j_abbr.strip().replace(" ",". ")

f_out=open("ncbi.txt","w")
for key, value in j_dic.iteritems():
     print >> f_out, "%s\t%s\t%s." % (key, value, j_dic2[key])
f_out.close()
