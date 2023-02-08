import cobra
import riptide
import pandas

model = cobra.io.load_yaml_model("C:/Users/cmoor/Documents/Papin Lab/Human1/Human-GEM.yml")

solo2 = {}
with open('C:/Users/cmoor/Documents/Papin Lab/Human1/Liver Riptide/GSE130991_Abundance_Male_Avg.tsv', 'r') as transcription:
    for line in transcription:
        line = line.split()
        abunds = float(line[1])
        try:
            ensembl = line[0]
            ensembl = ensembl.strip('"')
            solo2[ensembl] = abunds
        except:
            continue
            
print(solo2['ENSG00000162571'])


Male_Liver = riptide.maxfit_contextualize(model=model, transcriptome=solo2, conservative = True)

Male_Liver_Samples = Male_Liver.flux_samples

with pandas.ExcelWriter("C:/Users/cmoor/Documents/Papin Lab/Human1/Liver Riptide/Samples/Male_Liver_Avg.xlsx") as writer:
    Male_Liver_Samples.to_excel(writer)



solo2F = {}
with open('C:/Users/cmoor/Documents/Papin Lab/Human1/Liver Riptide/GSE130991_Abundance_Female_Avg.tsv', 'r') as transcription:
    for line in transcription:
        line = line.split()
        abunds = float(line[1])
        try:
            ensembl = line[0]
            ensembl = ensembl.strip('"')
            solo2F[ensembl] = abunds
        except:
            continue
            
print(solo2F['ENSG00000162571'])

Female_Liver = riptide.maxfit_contextualize(model=model, transcriptome=solo2F, conservative = True)

Female_Liver_Samples = Female_Liver.flux_samples

with pandas.ExcelWriter("C:/Users/cmoor/Documents/Papin Lab/Human1/Liver Female_Liver_Avg.xlsx") as writer:
    Female_Liver_Samples.to_excel(writer)