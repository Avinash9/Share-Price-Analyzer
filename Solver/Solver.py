
import sys
import csv
from collections import OrderedDict, namedtuple




class DataInconsistantException(Exception):
    pass


def get_result(file_name):
       '''
       Reading csv file from given path
       retuning orderdict type
       '''
       try:
           with open(file_name) as file_data:
              reader = csv.reader(file_data)
              return calculate_data(reader)
       except IOError, err:
            raise IOError("File dosen't Exist")
  
def get_company_names(raw_data):
       '''
              retrieving all the company names
       '''
       return next(raw_data)[2:]


def calculate_data(reader):
           '''
              doing all the compuation
           '''
           schema = namedtuple('parameters', ['price', 'year', 'month'])
           result = OrderedDict()
           company_names = get_company_names(reader)
           for name in company_names:
               result[name] = schema(0, 'year', 'month')
           for row in reader:
              try:
                  year, month = row[:2] 
                  if year=='' or month=='':
                     raise DataInconsistantException("Please check the data inside the file")
                  for name, price in zip(company_names, map(int, row[2:])): 
                      if result[name].price < price:
                          result[name] = schema(price, year, month)
              except:
                  raise DataInconsistantException("Please check the data inside the file")
           return result

def get_list(output):
    '''
    converting order dict into list
    '''
    output_list=[]
    for key,value in output.iteritems():
       output_list.append('('+key+','+str(value.price )+','+str(value.year)+','+str(value.month)+')')
    print output_list

def main():
    print "Enter the csv file path "
    file_path = raw_input("input: ")
    output=get_result(file_path)
    print "********************OUTPUT***********************"
    print get_list(output)
    print "*************************************************"
         


if __name__ == "__main__":
    main()
