from get_wb import get_wb_info

if __name__ == "__main__":
    while True:
        article_id = input("Введите артикул (или '0' для выхода): ")
        if article_id.lower() == "0":
            break

        result = get_wb_info(article_id)
        print(result)

