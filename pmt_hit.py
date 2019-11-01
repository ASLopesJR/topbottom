#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pdb
import os

workdir = os.getcwd()
lista_pmts = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
unidades = ['0', '1', '2', '3', '4', '5', '6', '_']
#pdb.set_trace()
pos_x  = [900]
pos_y  = [0]

for index_x in range(len(pos_x)):
    for index_y in range(len(pos_y)):
        print("Validando dados de energia", pos_x[index_x])
        same_event = False
        save = False
        evento = 0
        flag = False
        hits_target_U = 0
        hits_target_D = 0
        hits_evento   = 0
        hit_U = [False]*16
        hit_D = [False]*16
        hits_U = [0]*16
        hits_D = [0]*16
        queryFile = open("%s/SimulationOutput.G4"%workdir,"r")
        file_target_pmts = open("%s/pmts_target.txt"%workdir, "w")
        #file_target_D = open("%s/pmts_hits.txt"%workdir, "w")
        line = queryFile.readline()

        while (line):
            words = line.split(' ')
            if(words[1]=='EVENT'):
                if(flag == True and save == True):
                    #pdb.set_trace()
                    #file_energia.write("%s"%energia)
                    file_target_pmts.write("%d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d\n"%(hits_U[0], hits_U[1], hits_U[2], hits_U[3], hits_U[4], hits_U[5], hits_U[6], hits_U[7], hits_U[8], hits_U[9], hits_U[10], hits_U[11], hits_U[12], hits_U[13], hits_U[14],hits_U[15], hits_D[0], hits_D[1], hits_D[2], hits_D[3], hits_D[4], hits_D[5], hits_D[6], hits_D[7], hits_D[8], hits_D[9], hits_D[10], hits_D[11], hits_D[12], hits_D[13], hits_D[14], hits_D[15]))
                    #file_target_D.write("%d\n"%hits_target_D)
                    #file_hits.write("%s\n"%hits_evento)
                    hits_target_U = 0
                    hits_target_D = 0
                    hits_evento   = 0
                    save  = False
                    hit_U = [False]*16
                    hit_D = [False]*16
                    hits_U = [0]*16
                    hits_D = [0]*16
                else:
                    flag = True
                evento = evento + 1
            #if(words[1]=='PARTICLE'):
            #    ##pdb.set_trace()
            #    energia = words[2]
            if(words[1]=='HITS'):
                save = False
            if(words[1]=='HIT'):
                #pdb.set_trace()
                save = True
                tamanho = len(words)
                last_term = words[tamanho-1]
                pmt_target = list(last_term)
                if(pmt_target[10] == 'U' ):
                    for var in lista_pmts:
                        ##pdb.set_trace()
                        if ((pmt_target[11] == var) and (hit_U[int(var)-1] == False) and (var != '1')):
                            #pdb.set_trace()
                            hits_U[int(var)-1] = hits_U[int(var)-1] + 1
                            break
                        if ((pmt_target[11] == '1') and var == '1'):
                            for unidade in unidades:
                                if((pmt_target[12] == unidade) ):
                                    #pdb.set_trace()
                                    if unidade == '_':
                                        if hit_U[0] == False:
                                            #pdb.set_trace()
                                            hits_U[0] = hits_U[0] + 1
                                            break
                                    elif hit_U[int(unidade)+9] == False:
                                        #pdb.set_trace()
                                        hits_U[int(unidade)+9] = hits_U[int(unidade)+9] + 1
                                        break
                    same_event = True
                if(pmt_target[10] == 'D' ):
                    for var in lista_pmts:
                        if ((pmt_target[11] == var) and (hit_D[int(var)-1] == False) and (var != '1')):
                            #pdb.set_trace()
                            hits_D[int(var)-1] = hits_D[int(var)-1] + 1
                            break
                        if ((pmt_target[11] == '1') and var == '1'):
                            for unidade in unidades:
                                if((pmt_target[12] == unidade) ):
                                    #pdb.set_trace()
                                    if unidade == '_':
                                        if hit_D[0] == False:
                                            #pdb.set_trace()
                                            hits_D[0] = hits_D[0] + 1
                                            break
                                    elif hit_D[int(unidade)+9] == False:
                                        #pdb.set_trace()
                                        hits_D[int(unidade)+9] = hits_D[int(unidade)+9] + 1
                                        break
                    same_event = True
            oldLine = line
            line = queryFile.readline()
            if (same_event == True):
                line = queryFile.readline()
                same_event = False


        ##pdb.set_trace()
        if(save == True):
            #file_energia.write("%s"%energia)
            file_target_pmts.write("%d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d\n"%(hits_U[0], hits_U[1], hits_U[2], hits_U[3], hits_U[4], hits_U[5], hits_U[6], hits_U[7], hits_U[8], hits_U[9], hits_U[10], hits_U[11], hits_U[12], hits_U[13], hits_U[14],hits_U[15], hits_D[0], hits_D[1], hits_D[2], hits_D[3], hits_D[4], hits_D[5], hits_D[6], hits_D[7], hits_D[8], hits_D[9], hits_D[10], hits_D[11], hits_D[12], hits_D[13], hits_D[14], hits_D[15]))
            #file_target_D.write("%d\n"%hits_target_D)
            #file_hits.write("%d\n"%hits_evento)
    #    pdb.set_trace()
        queryFile.close()
        file_target_pmts.close()
        #file_energia.close()
        #file_hits.close()
#try:
    #data = loadtxt("datafiles/hits_targe_U_25k.txt", dtype = int)
    #values = trim_zeros(sort(data))
    #plt.hist(values,bins=720)
    #plt.show()
    #plt.close()
#
    #sns.set_style('whitegrid')
    #sns.kdeplot(values)
    #plt.show()
#except:
    #print("fodeu")
