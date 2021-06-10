# 1
'''
Let's remeber how to use dictionaries.
Task: return a dictionary where 
    * keys are IDs of seqs from an input fasta file (prot.fasta),
    * key's values are seqs itself. 
'''
from pathlib import Path #to indicate the path to our file
path = Path('/home/maria/Documents/Python/02_semester/HWs/05_bio_hw_4/prot.fasta')
inFile = open(path,)


def my_own_fasta_parser(inFile):

    sequences = {}

    with inFile:
        for line in inFile:
            line = line.strip()
            if line.startswith('>'):
                seq_id = line[1:]
            else:
                sequences[seq_id] = line

    return sequences


my_own_fasta_parser(inFile)


# 2
'''
Another super easy task.

We have the same fasta file (prot.fasta).
Now we want to get a list with the ids of protein seqs that have 
a relative frequency higher than a given threshold for a given residue.

And don't forget to use my_own_fasta_parser function from a previous task!
'''
from pathlib import Path #to indicate the path to our file
path = Path('/home/maria/Documents/Python/02_semester/HWs/05_bio_hw_4/prot.fasta')
inFile = open(path,)


def my_own_residue_abundance(input_file, residue, threshold=0.2):
    
    seq_id = []
    sequences = my_own_fasta_parser(inFile)

    for current_id, sequence in sequences.items():
        if sequence.count(residue)/len(sequence) > threshold:
            seq_id.append(current_id)
    
    #for sequence in sequences.items():
    #    if (sequence[1].count(residue)/len(sequence[1])) > threshold:
    #        seq_id.append(sequence[0])

    return seq_id

my_own_residue_abundance(inFile, 'V', 0.09)

# 3
'''
Let's practice in Bio package using.
Task:
1. read fasta file containing several DNA seqs (nucl.fasta)
2. subset seqs that have GC content > 45 and coding protein with aromaticity > 0.01
3. write a new fasta file with those protein(!) seqs
4. return the percentage of seqs that passed your filter
Hint: Bio.SeqIO, Bio.SeqRecord, Bio.SeqUtils
'''
from Bio import SeqIO, SeqUtils
from Bio.SeqUtils.ProtParam import ProteinAnalysis
from Bio.SeqRecord import SeqRecord


#from pathlib import Path 
#input_file = Path('/home/maria/Documents/Python/02_semester/HWs/05_bio_hw_4/nucl.fasta')

def my_own_filtering(input_file, output_file, filt_gc=45, filt_arom=0.01):
    
    sequences = {}
    c = 0
    
    with open(input_file, "r") as content:
        
        for record in SeqIO.parse(content, "fasta"):
            c+=1
            
            # calculate GC content using Bio
            
            calc_gc = SeqUtils.GC(record.seq)
            
            # calculate aromaticity using Bio
            
            prot_seq = record.seq.translate()
            X = ProteinAnalysis(str(prot_seq))
            calc_arom = X.aromaticity()
            
            # so, now you can filter
            if calc_gc >= filt_gc and calc_arom >= filt_arom:
                sequences[record.id] = record.se
    
    # write a new fasta file with aminoacids
    records = []
    for seq_id, seq in sequences.items():
        records.append(SeqRecord(seq.translate(), id=seq_id, description=""))

    write_file = open('my_fasta', 'w')
    SeqIO.write(records, write_file, 'fasta')
    write_file.close()

    # print the percentage
    print(len(records)/c)  

# 4
"""
Continue practicing in Bio package using:
Task:
complete the following code that should be able to return 
the best alignment of two amino acid seqs (pairwise2.align.globalds)
based on BLOSUM62 matrix from Bio.SubsMat.MatrixInfo.
http://rosalind.info/glossary/blosum62/
"""

from Bio import pairwise2
from Bio.SubsMat import MatrixInfo as matlist

def balign(first_seq, second_seq, op_gap = -5, ext_gap = -0.5):

    # Load the matrix
    matrix = matlist.blosum62

    # Generate the alignments
    alns = pairwise2.align.globalds(first_seq, second_seq, matrix,op_gap, ext_gap)

    # Extract the best alignment (first one in the alns list)
    top_aln = alns[0]

    # Print the alignment
    #aln_A, aln_B, score, begin, end = #<<<<<<<<<<...>>>>>>>>>>>
    print(pairwise2.format_alignment(*top_aln)) #<<<<<<<<<<...>>>>>>>>>>>
    return(top_aln)

balign('AGTTTCCCAAA', 'ATTC')


# In[77]:


# 5
""" You have some DNA sequence: AGTACTAGAGCATTCTATGGAG.
Find out which peptides could be created from it and sort them by their length.
Use as much Biopython modules as possible.
"""

from Bio.Seq import Seq
my_rna = Seq("AGTACTAGAGCATTCTATGGAG")
peptides = []

for i in range(len(my_rna)):
    peptide = my_rna[i:].translate(to_stop = True)
    if peptide != '':
        peptides.append(peptide)

for peptide in sorted(peptides, key = len):
    print(peptide)


# 6
""" TASK: Try to create one-line function (without (!!!) using Bio package) 
that returns reverse complementary to a given sequence. 
Hint: using dictionaty & list comprehensions might be helpful.
"""
def rev_compl_one_line(seq):
    return "".join({'A':'T', 'G':'C', 'T':'A', 'C':'G'}.get(el) for el in reversed(seq))

rev_compl_one_line('ATGC')

