# antismash_scripts


## How to run

1. Gather assemblies in fasta_folder
2. run prokka on all isolates using:</br>
/srv/data/tools/git.repositories/antismash_scripts/batch_prokka.py fasta_folder prokka_output_folder
3. wait for prokka to finish on all isolates, then run antismash on all isolates:</br>
. activate env_antismash</br>
/srv/data/tools/git.repositories/antismash_scripts/batch_antismash_prokkaout.py prokka_output_folder antismash_output_folder
4. rename bigscape output gbk files:</br>
/srv/data/tools/git.repositories/antismash_scripts/copy_antismash_output.py antismash_output_folder bigscape_input_folder
5. run BiG-SCAPE</br>
python3 /srv/data/tools/git.repositories/BiG-SCAPE/bigscape.py -i bigscape_input_folder -o bigscape_output_folder
