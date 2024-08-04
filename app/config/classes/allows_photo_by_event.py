

class AllowsPhotoByEventConfig:
    def __init__(
        self,
        file_name: str,
        with_event_id: bool
    ):
        self.file_name = file_name
        self.with_event_id = with_event_id