# antismash_scripts


## How to run

1. Gather assemblies in fasta_folderfolder
2. run prokka on all isolates using:</br>
/srv/data/tools/git.repositories/antismash_scripts/batch_prokka.py fasta_folder prokka_output_folder
3. wait for prokka to finish on all isolates, then run antismash on all isolates usig:</br>
. activate env_antismash</br>
/srv/data/tools/git.repositories/antismash_scripts/batch_antismash_prokkaout.py prokka_output_folder antismash_output_folder
