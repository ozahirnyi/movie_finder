from rest_framework.renderers import BaseRenderer, JSONRenderer


class NdjsonRenderer(BaseRenderer):
    media_type = 'application/x-ndjson'
    format = 'ndjson'
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        if data is None:
            return b''
        if isinstance(data, (bytes, bytearray)):
            return data
        if isinstance(data, str):
            return data.encode(self.charset)
        return data


STREAM_RENDERERS = [NdjsonRenderer, JSONRenderer]
