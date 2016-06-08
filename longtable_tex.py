"""
Adapted from https://gist.github.com/astrolitterbox/8e92f27651608162bc06
It's now basically completely
"""

from __future__ import division
import numpy as np

def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False


def longtable_out(file_name,data,column_names,caption,label='tab1',center=True,sigfigs=3,alignment=None,boldface=False):
'''
@file_name:         The name of the text file to write a LaTeX longtable to.
                    Fairly sure this file must already exist, should probably
                    check this and give it the ability to make file if needed
@data:              The data you wish to appear in the table should be of form 
                    data[row,column].
@column_names:      The names of the columns as strings to use in the table,
                    remember that when writing symbols, etc \ must be \\ else 
                    the string following the '\' will be interpreted oddly.
                    (I'm not trying to patronise anyone that may read this, I
                    just always forget! Also probably no one ever will read 
                    this again, including me.)
@label:             The label to use for referencing the table within the LaTeX
                    document. Defaults to tab1.
@center:            Do you want centering for the table, True/False, defaults 
                    True because I can't imagine I will use False much.
@sigfigs:           How many significant figures would you like? Takes either a
                    single value to use for all numerical values, or an array 
                    of values with the same length as the number of columns. It
                    doesn't matter if you have a column composed of strings, it
                    won't try to round a string.
@alignment:         If no alignment string is specified (None), which is the 
                    default, then a string of purely '|c|' for each column is 
                    used. Should probably update this to allow for purely right
                    or left aligned. 
@boldface:          Do you want the column headers to be bold? This takes True/
                    False, and defaults to False arbitrarily.

longtable_out (hopefully) makes nice longtables, hope it comes in handy!                   
'''
    
    ofile = open(file_name, 'w')
    
    if center==True:
        ofile.write('\\begin{center} \n')
    
    
    if alignment==None:
        alignment = '|c'*len(column_names)+'|'
    
    ofile.write('\\'+'begin{longtable}{'+alignment+'}\n')
    ofile.write('\\'+'caption{'+caption+'}'+' \label{'+label+'} \\\ \n\n')
    
    if boldface==True:
        tick1 = '\\'+'textbf{'
        tick2 = '}'
    elif boldface==False:
        tick1 = ''
        tick2 = ''
    
    header_line = ''
    for i,hedr in enumerate(column_names):
        header_line = '\hline'
    for i,hedr in enumerate(column_names):
        if i==0:
            header_line += ' \\'+'multicolumn{1}{|c|}{'+tick1+hedr+tick2+'}'
        else:
            header_line += '& \\'+'multicolumn{1}{|c|}{'+tick1+hedr+tick2+'}'
    header_line += '\\\ \hline\n'
    
    
    ofile.write(header_line)
    ofile.write('\\'+'endfirsthead \n \n')
    ofile.write('\\'+'multicolumn{'+str(len(column_names))+'}{c}%\n')
    ofile.write('{{\\'+'bfseries \\tablename\ \\thetable{} -- continued from previous page}} \\\ \n')
    ofile.write(header_line)
    ofile.write('\\'+'endhead \n \n')
    ofile.write('\\hline \\multicolumn{'+str(len(column_names))+'}{|r|}{{Continued on next page}} \\\ \\hline \n')
    ofile.write('\\endfoot \n\n')
    ofile.write('\\hline \\hline \n')
    ofile.write('\\endlastfoot \n\n')
        
    for i,obj in enumerate(data):
        curr_obj = ''
        for j,itm in enumerate(obj):
            if isfloat(itm)==True:
                sigfigs1 = np.array([sigfigs])
                if len(sigfigs1)!=1:
                    sigfig_curr = sigfigs[j]
                elif len(sigfigs1)==1:
                    sigfig_curr = sigfigs
                print float(itm),sigfig_curr
                if j!=len(column_names)-1:
                    curr_obj += str(round(float(itm),sigfig_curr))+'&'
                elif j==len(column_names)-1:
                    curr_obj += str(round(float(itm),sigfig_curr))
        ofile.write(curr_obj+'\\\\'+'\n')
    
    ofile.write('\\end{longtable}\n')
    if center==True:
        ofile.write('\\end{center}')
    
    ofile.close()



















    