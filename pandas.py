import pandas as pd 


data = pd.read_csv('D:\\student_inf.csv')
#print(data.columns)

#print(data[data.groupby(['student']).sum()]['student'])
#print(data.groupby(['student']).sum()['student'])


grp_data=data.groupby(['student']).sum()

#print(grp_data.columns)


grp_data=pd.DataFrame(grp_data)
#print(grp_data)
#print (grp_data.columns)

grp_data.to_csv("D:\\grp_student_inf.csv")

grp_data=pd.read_csv("D:\\grp_student_inf.csv")
#print(grp_data.columns)


max_value_df = grp_data['marks'].max()



print(grp_data[grp_data['marks']==max_value_df]["student"])




"""for i in range(len(grp_data)):
    print(i)
    
    print(grp_data.loc[i])"""
    #if (grp_data['marks'][i]==max_value_df):
     #   print(grp_data['student'][i])
    

#for i in grp_data.:
 
    #print(i)
   # if i['marks']==max_value_df:
        
    
