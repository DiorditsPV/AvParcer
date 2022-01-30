from siteParce import AvitoElement
from desc import url, attrs

token = AvitoElement(url, 'iphone')
token.findCascadeElements(attrs)

pickle.dump(token.avBlocks)
