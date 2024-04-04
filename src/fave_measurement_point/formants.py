import numpy as np
from dataclasses import dataclass, field

@dataclass
class Point():
    value: float
    time: float
    rel_time: float
    prop_time: float
    index: int


@dataclass
class Formant():
    track: np.array
    time: np.array = field(default=None)

    def __post_init__(self):
        if not self.time:
            idx_time = np.arange(self.track.size)
            self.time = idx_time/idx_time.max()
        
        self.rel_time = self.time - self.time.min()
        self.prop_time = self.rel_time / self.rel_time.max()

    @property
    def max(self):
        max_idx = self.track.argmax()
        max_value = self.track[max_idx]
        max_time = self.time[max_idx]
        max_rel_time = self.rel_time[max_idx]
        max_prop_time = self.prop_time[max_idx]
        return Point(max_value, max_time, max_rel_time, max_prop_time, max_idx)
    
    @property
    def min(self):
        min_idx = self.track.argmin()
        min_value = self.track[min_idx]
        min_time = self.time[min_idx]
        min_rel_time = self.rel_time[min_idx]
        min_prop_time = self.prop_time[min_idx]
        return Point(min_value, min_time, min_rel_time, min_prop_time, min_idx)
    

def nan_array(shape):
    empty = np.empty(shape)
    empty[:] = np.nan

@dataclass
class FormantArray():
    f1 : Formant
    f2 : Formant
    f3 : Formant = field(default=None) 


