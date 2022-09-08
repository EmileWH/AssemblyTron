bash -c "scp -r /mnt/c/Users/Public/Documents/opentrons/src/AssemblyTron/Cloning/* root@robot:/data/user_storage/Cloning/"
bash -c "scp -r /mnt/c/Users/Public/Documents/opentrons/src/AssemblyTron/Restriction/* root@robot:/data/user_storage/Restriction/"
bash -c "scp -r root@robot:/data/user_storage/*/*/output_*.csv /mnt/c/Users/Public/Documents/opentrons/src/AssemblyTron/outputs"

bash -c "scp -r /mnt/c/Users/Public/Documents/opentrons/src/AssemblyTron/Golden_Gate/* root@robot:/data/user_storage/Golden_Gate/"
bash -c "scp -r /mnt/c/Users/Public/Documents/opentrons/src/AssemblyTron/robotpaths.csv root@robot:/data/user_storage/"

bash -c "scp -r /mnt/c/Users/Public/Documents/opentrons/src/AssemblyTron/output_new_pcrwell_location.csv root@robot:/data/user_storage/"
bash -c "scp -r /mnt/c/Users/Public/Documents/opentrons/src/AssemblyTron/Cloning/Input.csv root@robot:/data/user_storage/Cloning/"

bash -c "scp -r /mnt/c/Users/Public/Documents/opentrons/src/AssemblyTron/Golden_Gate/Input.csv root@robot:/data/user_storage/Golden_Gate/"

bash -c "scp -r /mnt/c/Users/Public/Documents/opentrons/src/AssemblyTron/output_*.csv root@robot:/data/user_storage/"
bash -c "scp -r root@robot:/data/user_storage/output_*.csv /mnt/c/Users/Public/Documents/opentrons/src/AssemblyTron/"

bash -c "scp -r /mnt/c/Users/Public/Documents/opentrons/src/AssemblyTron/Protocols/Plate_Replication/*.csv root@robot:/data/user_storage/Protocols/Plate_Replication/"

pause