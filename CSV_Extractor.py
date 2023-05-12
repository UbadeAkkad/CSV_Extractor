import pandas as pd
import xlsxwriter

def Extractor(filename,field_name_list,output_file_name=""):

    """
    To extract certain fields from a CSV file.

    Arguments:
        filename {string} -- CSV file name without the .csv file extension.
        field_name_list {list} -- List of field names to be extracted from the file.
        output_file_name {string} -- Name of the output sample file, if not assigned the output file will be named "Extracted_{filename}".
    """

    data = pd.read_csv(filename + ".csv")

    if output_file_name == "":
        workbook = xlsxwriter.Workbook("Extracted_" + filename + '.xlsx',{'strings_to_urls': False})
    else:
        workbook = xlsxwriter.Workbook(output_file_name + '.xlsx',{'strings_to_urls': False})

    worksheet = workbook.add_worksheet()

    output_list = []

    for field_name in field_name_list:
        try:
            data_list = data[field_name].to_list()
            data_list.insert(0,field_name)
            output_list.append(data_list)
        except:
            print("field not found! " + field_name)

    for i, field_list in enumerate(output_list):
        for j, line in enumerate(field_list):
            worksheet.write(j, i, line)

    workbook.close()


input_name = input("Enter the file name without .csv: ")
field_name = input("Add a field name: ")
input_field_list = []
input_field_list.append(field_name)

while field_name != "":
    field_name = input("Add an addtional field name or click enter to run: ")
    if field_name !="":
        input_field_list.append(field_name)

Extractor(input_name,input_field_list)
