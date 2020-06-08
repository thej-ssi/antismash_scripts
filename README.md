# antismash_scripts


## How to run

1. Gather assemblies in fasta_folderfolder
2. run:
/srv/data/tools/git.repositories/antismash_scripts/batch_prokka.py fasta_folder prokka_output_folder
3. wait for prokka to finish on all isolates, then run:
. activate env_antismash
/srv/data/tools/git.repositories/antismash_scripts/batch_antismash.py prokka_output_folder antismash_output_folder
