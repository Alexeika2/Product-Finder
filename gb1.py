#Import BioPython instruments.
from Bio import SeqIO 
from Bio import Entrez

fasta_file="OXA_finds.fasta" #Create the FASTA file
output=open(fasta_file,'w') #Open for write
gb_file="OXA_test.gb" #Open up GenBank file
wanted=["Beta-lactamase class D"] #What product do you wanna find?
#parsing genbank file, search for product, and if finds
#We write the sequence in FASTA file,and close the file output.
for record in SeqIO.parse(open(gb_file,"r"),"genbank"):
    print("Name %s, %i features" % (record.id,len(record.features)))
    print(repr(record.seq))
    Entrez.email="alexeika2@yandex.ru" #Change it for your Email
    handle=Entrez.efetch(db='nucleotide',id=record.id,rettype='gb',retmode='text')
    record1=SeqIO.read(handle,'genbank')
    for i,feature in enumerate(record1.features):
        
        if feature.type=='CDS' and 'product' in feature.qualifiers:
            product=feature.qualifiers['product'][0]
            if product in wanted:
                output.write(">%s,%s from %s\n%s\n" % (feature.qualifiers['product'][0],feature.qualifiers['locus_tag'][0],record1.name,feature.extract(record1.seq)))
output.close()
                                                     
