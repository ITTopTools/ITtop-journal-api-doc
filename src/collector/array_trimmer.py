def trim_arrays(data, max_items: int = 3):
    """
    Рекурсивно обходит JSON и обрезает все списки до max_items.
    """
    if isinstance(data, dict):
        return {key: trim_arrays(value, max_items) for key, value in data.items()}
    elif isinstance(data, list):
        # Обрезаем список и рекурсивно обрабатываем оставшиеся элементы
        # (вдруг внутри списка объектов есть другие списки)
        return [trim_arrays(item, max_items) for item in data[:max_items]]
    else:
        return data