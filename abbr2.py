journal_f=open("J_Medline.txt","r")
lines=journal_f.readlines()
j_dic={}
j_dic2={}
j_dic_r={}
j_name=""
j_abbr=""
n1=0
n2=0
type="normal"
for i in range(len(lines)):
    if lines[i].startswith("JournalTitle"):
        j_name=lines[i].split("JournalTitle:")[1]
        if lines[i+1].startswith("MedAbbr:"):
            j_abbr=lines[i+1].split("MedAbbr:")[1]
            j_dic[j_name.strip()]=j_abbr.strip()
            j_dic_r[j_abbr.strip()]=j_name.strip()
            j_dic2[j_name.strip()]=j_abbr.strip().replace(" ",". ")

f_out=open("ref.txt","w")

title_f=open("Root_Bark_Compare.txt","r")
lines2=title_f.readlines()
if type=="titles":
    print "\nFirst Letter of Journal Title Will be Capitalized\n"
elif type=="normal":
    print "\nFirst letter of journal title will be in small case\n"

for i in range(len(lines2)):
    j_name1=lines2[i].split("\t")[0]
    j_name2=j_name1.strip().replace("\xef\xbb\xbf","")
    try:
        try:
            j_name1=j_dic_r[j_name2]
            j_name3=j_dic2[j_name1]
            if type=="titles":
                print >> f_out, "%s\t%s\t%s." % (j_name1.title(), j_name2, j_name3)
            else:
                print >> f_out, "%s\t%s\t%s." % (j_name1, j_name2, j_name3)
        except:
            j_name1a=j_name2
            j_name2a=j_dic[j_name1a]
            j_name3a=j_dic2[j_name1a]
            if type=="titles":
                print >> f_out, "%s\t%s\t%s." % (j_name1a.title(), j_name2a, j_name3a)
            else:
                print >> f_out, "%s\t%s\t%s." % (j_name1a, j_name2a, j_name3a)
        n1+=1
    except:
        if n2==0:
            print "Names of Missing Journal: \n"
        print j_name2
        n2+=1
print("")
print ("%s out of %s names found.") % (n1,n1+n2)
f_out.close()
