import shapefile as shp
import matplotlib.pyplot as plt

sf = shp.Reader("cb_2017_25_tract_500k")

plt.figure()
for shape in sf.shapeRecords():
    x = [i[0] for i in shape.shape.points[:]]
    y = [i[1] for i in shape.shape.points[:]]
    plt.plot(x,y)
plt.title('ABTACS')
#plt.show()

plt.savefig('ABTACS.png')