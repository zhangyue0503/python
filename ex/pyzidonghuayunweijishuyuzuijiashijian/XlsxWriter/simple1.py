#coding:utf-8
import xlsxwriter

workbook = xlsxwriter.Workbook('demo2.xlsx')
worksheet = workbook.add_worksheet()

worksheet.set_column('A:A',20)
bold=workbook.add_format({'bold':True})

# worksheet.write('A1','Hello')
# worksheet.write('A2','World',bold)
# worksheet.write('B2',u'中文测试',bold)
#
# worksheet.write(2,0,32)
# worksheet.write(3,0,35.5)
# worksheet.write(4,0,'=SUM(A3:A4)')

worksheet.write(0,0,'Hello')
cell_format = workbook.add_format({'bold':True})

worksheet.set_column(0,1,10,cell_format)
worksheet.set_column('C:D',20)
worksheet.set_column('E:G',None,None,{'hidden':1})

worksheet.set_row(0,40,cell_format)
worksheet.write(1,0,'World')
worksheet.set_row(1,None,None,{'hidden':True})
worksheet.write(2,0,2)
worksheet.write(3,0,3.00001)
worksheet.write(4,0,'=SIN(PI()/4)')
worksheet.write(5,0,'')
worksheet.write(6,0,None)


chart = workbook.add_chart({'type':'column'})

chart.add_series({
    'categories':'=Sheet1!$A$1:$A$5',
    'values':'=Sheet1!$B$1:$B:5',
    'line:':{'color':'red'}
})
chart.set_x_axis({
    'name':'Earnings per Quarter',
    'name_font':{'size':14,'bold':True},
    'num_font':{'italic':True}
})
worksheet.insert_chart('A7',chart)




workbook.close()