import time
import logging
import pandas as pd
class FileUpload(View):
    '''
    using pandas and django bulk create inserting csv data to DB took 0.89000 
    '''
    def post(self, request):
        try:
            start_time = time.time()
            df = pd.read_csv(request.FILES["csv_file"])
            regulatory_list = []
            for i in range(len(df)):
                d = df.loc[i, :]
                is_mandatory = True if d[3] == 1 else False

                regulatory_list.append(CustomerRegulatoryList(Industry_type_id=d[2], regulatory_name=d[1],
                                                              is_mandatory=is_mandatory))
            CustomerRegulatoryList.objects.bulk_create(regulatory_list)

            logging.info("--- %s seconds ---" % (time.time() - start_time))

        except:
            print str(sys.exc_info())

        return HttpResponse("<h1>saved</h1>")

fileupload=FileUpload.as_view()

###########################################################################################

class FileUpload(View):
    '''
    using pandas and django create insert csv data into DB took 12.000001  
    '''
    def post(self, request):
        try:
            start_time = time.time()
            df = pd.read_csv(request.FILES["csv_file"])
            
            for i in range(len(df)):
                d = df.loc[i, :]
                is_mandatory = True if d[3] == 1 else False

                CustomerRegulatoryList.objects.create(Industry_type_id=d[2], regulatory_name=d[1],
                                                      is_mandatory=is_mandatory)
            logging.info("--- %s seconds ---" % (time.time() - start_time))

        except:
            print str(sys.exc_info())

        return HttpResponse("<h1>saved</h1>")

fileupload=FileUpload.as_view()

