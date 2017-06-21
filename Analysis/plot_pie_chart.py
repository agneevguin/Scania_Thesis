import numpy as np
import matplotlib.pyplot as plt

BACKGROUND = (0,0,0)
ASPHALT = (105,105,105)
GRAVEL_H = (112,128,144)
GRAVEL_L = (192,192,192)
GRAVEL_N = (176,196,222)
MUD = (139,69,19)
MUD_N = (210,105,30)
SAND = (244,164,96)
SAND_N = (210,180,140)
WATER = (106,90,205)
WATER_N = (0,0,255)
SKY = (135,206,235)
VEGETATION = (0,100,0)
GRASS = (255,255,0)
GRASS_N = (154,205,50)
SNOW = (245,222,179)
SNOW_N = (255,255,224)

def mypie(slices,labels,colors):

    colordict={}
    for l,c in zip(labels,colors):
        print l,c
        colordict[l]=c

    fig = plt.figure(figsize=[10, 10])
    ax = fig.add_subplot(111)
    explode = (0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.05)#[::-1]
    pie_wedge_collection = ax.pie(slices, explode=explode, labels=labels, labeldistance=1.05, shadow = False, startangle = 90)#, autopct=make_autopct(slices)) , autopct='%1.1f%%'
    #patches, texts = ax.pie(slices, colors=colors, startangle=90)
    for pie_wedge in pie_wedge_collection[0]:
        #pie_wedge.set_edgecolor('white')
        pie_wedge.set_facecolor(colordict[pie_wedge.get_label()])
        #pie_wedge.set_facecolor({[1,1,1,1],[0,0,0,1]})
    titlestring = 'TEST SET\n16 classes, 9548 images'

    ax.set_title(titlestring)

    # sort_legend = True
    # if sort_legend:
    #     patches, labels, dummy =  zip(*sorted(zip(patches, labels, y),
	   #                                        key=lambda x: x[2],
	   #                                        reverse=True))
    plt.legend(labels=['%s, %1.1f %%' % (l, s) for l, s in zip(labels, slices)], bbox_to_anchor=(.85, 0.85, 0.25, 0.25)) #loc = 'lower left',

    return fig,ax,pie_wedge_collection

slices = [23.0835300808,5.0054532632,5.9420024041,4.0772629693,2.9854200632,1.3499223066,1.0885539337,1.1884853285,6.1775192138,0.6524547779,0.240995932,12.2123234079,6.5262162508,6.1775192138,0.9236346024,22.3687062518]
cmap = plt.cm.prism
colors = cmap(np.linspace(0., 1., len(slices)))
colors = [[105./255,105./255,105./255,1],[112./255,128./255,144./255,1],[192./255,192./255,192./255,1],[139./255,69./255,19./255,1],[244./255,164./255,96./255,1],[106./255,90./255,205./255,1],[255./255,255./255,0,1],[245./255,222./255,179./255,1],[176./255,196./255,222./255,1],[210./255,105./255,30./255,1],[210./255,180./255,140./255,1],[135./255,206./255,235./255,1],[0,100./255,0,1],[154./255,205./255,50./255,1],[255./255,255./255,224./255,1],[0,0,0,1]]#[::-1]
labels = [u'Asphalt', u'Gravel_H', u'Gravel_L', u'Mud', u'Sand', u'Water', u'Grass', u'Snow', u'Gravel_N', u'Mud_N', u'Sand_N', u'Sky', u'Vegetation', u'Grass_N', u'Snow_N', u'Background']#[::-1]

fig,ax,pie_wedge_collection = mypie(slices,labels,colors)

plt.show()