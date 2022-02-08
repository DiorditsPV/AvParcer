log_name = "dummy"
url = r"https://www.avito.ru/moskva/noutbuki?cd=1&q=macbook+air+m1+-i7+-i9+-i5&user=1"
gridAttrs = {
    'data-marker': 'item',
    'class': 'iva-item-root-_lk9K photo-slider-slider-S15A_ iva-item-list-rfgcH iva-item-redesign-rop6P iva-item-responsive-_lbhG items-item-My3ih items-listItem-Gd1jN js-catalog-item-enum'
}

# =======================================================

underelement = {
    'offer_name': {"itemprop": "name",
                   "class": "title-root-zZCwT iva-item-title-py3i_ title-listRedesign-_rejR title-root_maxHeight-X6PsH text-text-LurtD text-size-s-BxGpL text-bold-SinUO"
                   },
    'price': {"itemprop": "price", "content": True},
    'description': {"class": "iva-item-text-Ge6dR iva-item-description-FDgK4 text-text-LurtD text-size-s-BxGpL"},
    'seller_name': {"class": "style-title-_wK5H text-text-LurtD text-size-s-BxGpL"},
    'seller_url': {"class": "style-link-STE_U", "href": True},
    'seller_rating': {"data-marker": "seller-rating/score", "class": "desktop-1lslbsi"},
    'seller_rewiew': {"data-marker": "seller-rating/summary", "class": "desktop-1c71z48"},

    'public_hours_ago': None,
    'show_phone_button': None,
    'metro_stantion': None,
}
