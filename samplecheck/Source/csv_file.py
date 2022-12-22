import csv
def csv_file(filename,rowlist):
    with open(filename,'w') as result:
        writer=csv.writer(result,delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL,lineterminator='\n')
        length_of_value=len(rowlist[0])
        for item in rowlist:
            writer.writerow([item[count] for count in range(length_of_value)])



if __name__ == '__main__':
    MAC_VALUES = "assignment_network.csv"
    row_header =[('Country', 'State', 'City', 'Town')]
    csv_file(MAC_VALUES, row_header)
else:
    pass