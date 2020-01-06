TEAM DOUBLE HELIX | PROJECT UPDATE 
# Protein sub-Localization prediction through protein sequence analysis	

Protein sorting, the transport of protein after its synthesis, is one of the most complex processes in a cell. Large scale research has been going on in predicting the sub-localization of the proteins based on primary, secondary and tertiary sequencing. 
Our project aims at predicting the  sub-localization of proteins in an organelle of cell using primary sequencing. The Python-based GUI application would be based on Tkinter and BioPython Library. This project gives us insight about the usage of Bioinformatics concepts like multiple sequence alignments, usage of PSI-BLAST as well protein sequence extraction from NCBI. We will be making our local protein database as well with the help of Entrez E-Utilities API services. Apart from that, for running WOLF-PSORT we’ll be making our own scripting API so that we could get the most appropriate matches.

## Taking an input protein sequence
The user will be providing an input into GUI program as a string or he can input the sequence in the form of a FASTA file/ .txt file. The program would parse string according to appropriate delimiters and store it in a hashmap.

## Extraction of Protein sequence from NCBI 
Since our main objective is to do to comparisons through primary sequencing, we need to have a local database of few proteins from each of the organelle which takes into account the homology among different species so that we would have the most accurate results for a wider range of inputs. The local database of proteins is made through scripting using Entrez E-Utilities tool by NCBI. E-utilities use a fixed URL syntax that translates a standard set of input parameters into the values necessary for various NCBI software components to search for and retrieve the requested data from.

## Running BLAST 
With the help of the parsed fasta file, we will do a PSI-BLAST for the protein sequence using the BLAST Common URL API. The NCBI-BLAST Common URL API allows us to run searches remotely.

## Using WOLF-PSORT for localizations
After we obtain the sequence with maximum homology to the input sequence (in case of unknown sequence), we will then script https://wolfpsort.hgc.jp/ for getting the localizations of the homologous sequence. In this way, we would get the final result.

## Prerequisites for running the code
You’d need to install the following python libraries:
BioPython
Selenium
Tkinter

You’d also need to download the chromium driver as per your Chrome Browser version. You must be running the python code in the directory where chromedriver.exe file is downloaded.



