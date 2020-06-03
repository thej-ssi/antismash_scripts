# antismash_scripts


## How to run

1. Gather assemblies in folder
2. Run prokka on all isolates using python3 /srv/data/tools/git.repositories/antismash_scripts/batch_prokka.py input_folder prokka_output_folder
3. Run antismash on all isolates using python3 /srv/data/tools/git.repositories/antismash_scripts/batch_antismash.py prokka_output_folder antismash_output_folder
4. Run summary scripts (one for comparing cluster presence/absence, one for comparing gene cluster phylogenies)
