
import cobra
import riptide
import pandas
import sys

model = cobra.io.load_yaml_model("/home/cjm4yy/Sex_Specific_Liver/RIPTiDe/Individual_Models/Human-GEM.yml")

sample_number = int(sys.argv[1])

solo = {}
with open('GSE130991_Abundance_Female_Unique.tsv', 'r') as transcription:
    for line in transcription:
        line = line.split()
        abunds = float(line[sample_number])
        try:
            ensembl = line[0]
            ensembl = ensembl.strip('"')
            solo[ensembl] = abunds
        except:
            continue
            
print("test")
print(solo['ENSG00000162571'])

Female_Liver = riptide.maxfit_contextualize(model=model, transcriptome=solo, conservative = True, samples = 110, frac_min = 0.3, frac_max = 0.4)

#riptide.save_output(Female_Liver)
Female_Liver_Samples = Female_Liver.flux_samples

sample_number_char = str(sample_number)
file_prefix = "/home/cjm4yy/Sex_Specific_Liver/RIPTiDe/Individual_Models/Samples_Low/Female_Liver_Samples_"
file_ending = ".xlsx"

file_name_real = file_prefix + sample_number_char + file_ending

with pandas.ExcelWriter(file_name_real) as writer:
    Female_Liver_Samples.to_excel(writer)

