import numpy as np
# GSSMD Calculate Overlap of two distributions
########################################################
#   << HOW TO USE >> 
# target = np.random.normal(loc=0,scale=1, size=(100000))
# background = np.random.normal(loc=0,scale=1, size=(100000))
# OVL(target,background)
########################################################
def OVL(target,background):
    #get range of values
    nbins = int(np.round(1+np.log2(np.min([len(target),len(background)]))))
    x_scale=np.concatenate((np.linspace(start=np.min([np.min(target),np.min(background)]), stop=np.max([np.max(target),np.max(background)]),num=nbins), [np.inf]))
    # estimate probability density function
    pdf_t=np.histogram(target,x_scale)
    pdf_b=np.histogram(background,x_scale)  
    # estimate overlap
    combined = []
    combined.append(pdf_t[0]/sum(pdf_t[0]))
    combined.append(pdf_b[0]/sum(pdf_b[0]))
    combined = np.array(combined)
    OVL = np.sum(np.min(combined,axis=0))
    return OVL
