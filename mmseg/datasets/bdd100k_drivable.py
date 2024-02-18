from mmseg.registry import DATASETS
from .basesegdataset import BaseSegDataset


@DATASETS.register_module()
class BDD100KDrivableDataset(BaseSegDataset):

    METAINFO = dict(
        classes=('drivable', 'alternative', 'background'),
        palette=[[86, 94, 219], [219, 211,  86], [0, 0,  0]])

    def __init__(self,
                 img_suffix='.jpg',
                 seg_map_suffix='.png',
                 reduce_zero_label=False,
                 **kwargs) -> None:
        super().__init__(
            img_suffix=img_suffix,
            seg_map_suffix=seg_map_suffix,
            reduce_zero_label=reduce_zero_label,
            **kwargs)
