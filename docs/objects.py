import fave_measurement_point
import sphobjinv as soi
from pathlib import Path
inv = soi.Inventory(fname_plain = Path("objects.txt"))

for idx in range(len(inv.objects)):
    obj = inv.objects[idx]
    basename = obj.name.split(".")[-1]
    if hasattr(fave_measurement_point, basename):
        obj_dict = obj.json_dict()
        if not "new_fave." + basename in obj_dict:
            obj_dict["name"] = "fave_measurement_point." + basename
            new_obj = soi.DataObjStr(**obj_dict)
            inv.objects.append(new_obj)
            
df = inv.data_file()
dfc = soi.compress(df)
soi.writebytes("objects.inv", dfc)