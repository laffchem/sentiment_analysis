import os
from striprtf.striprtf import rtf_to_text


def convert_rtf_to_txt(filenames: list[str], output_dir: str) -> None:
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for file in filenames:
        with open(file, "r") as f:
            rtf_content = f.read()
            text = rtf_to_text(rtf_content)
            txt_filename = os.path.join(
                output_dir, os.path.splitext(os.path.basename(file))[0] + ".txt"
            )
            with open(txt_filename, "w") as txt_file:
                txt_file.write(text)
            print(f"Converted {file} to {txt_filename}")


filenames = [
    "3MCo-10.RTF",
    "CiscoSystems-10.RTF",
    "McDonalds-2.RTF",
    "TravelersCo-3.RTF",
    "AmazonFiles-10.RTF",
    "CocaCola-10.RTF",
    "MerckCo-10.RTF",
    "UnitedHealth-10.RTF",
    "AmericanExpressFiles-10.RTF",
    "GoldmanSachs-10.RTF",
    "Microsoft-10.RTF",
    "Verizon-10.RTF",
    "AmgenFiles10.RTF",
    "HomeDepot-10.RTF",
    "Nike-10.RTF",
    "Visa-10.RTF",
    "AppleFiles-10.RTF",
    "Honeywell-10.RTF",
    "Nvidia-10.RTF",
    "Walmart-10.RTF",
    "BoeingFiles-10.RTF",
    "IBM-10.RTF",
    "ProcterGamble-10.RTF",
    "WaltDisney-10.RTF",
    "CaterpillarFiles-10.RTF",
    "JohnsonJohnson-10.RTF",
    "Salesforce-10.RTF",
    "Chevron-10.RTF",
    "JPMorganChase-10.RTF",
    "SherwinWilliams-6.RTF",
]

convert_rtf_to_txt(filenames, "data")
