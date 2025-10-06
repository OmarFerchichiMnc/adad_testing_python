import yaml




with open("/home/Omar.Ferchichi/Desktop/adad_testing_python/adad_testing/src/configuration/config.yaml", "r") as file:
    config = yaml.safe_load(file)


class sale_and_settlement_molecule_correct_files :
    sale_path_for_molecule = config["local_folder"]+config["test_files"]["sale_settlement_molecule"]["correct"]["sale_file_path"]
    sale_file_for_molecule = config["local_folder"]+config["test_files"]["sale_settlement_molecule"]["correct"]["sale_file"]
    sale_file_name = config["test_files"]["sale_settlement_molecule"]["correct"]["sale_file_name"]
    payment_date_range = config["test_files"]["sale_settlement_molecule"]["correct"]["payment_date_range"]

    settlement_path_for_molecule = config["local_folder"]+config["test_files"]["sale_settlement_molecule"]["correct"]["settlement_file_path"]
    settlement_file_for_molecule = config["local_folder"]+config["test_files"]["sale_settlement_molecule"]["correct"]["settlement_file"]
    settlement_file_name = config["test_files"]["sale_settlement_molecule"]["correct"]["settlement_file_name"]
    settlement_date_range = config["test_files"]["sale_settlement_molecule"]["correct"]["settlement_date_range"]
    

print(sale_and_settlement_molecule_correct_files.sale_file_for_molecule)


class adad_paths:
    sales = config["adad_paths"]["sales"]
    setllement = config["adad_paths"]["settlement_global"]