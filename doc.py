from docx import Document


def save_iterable_to_docx(iterable, docx_name):
    if not len(docx_name):
        raise ValueError('Пустое имя файла')
    document = Document()
    if '.docx' not in docx_name:
        docx_name += '.docx'
    for element in iterable:
        document.add_paragraph(str(element))
    document.save(docx_name)





def main():
    page = 'https://2ch.hk/soc/res/4192723.html'
    # save_girls_to_docx(page, 'test')
    save_iterable_to_docx(['one'], 'name')



if __name__ == "__main__":
    main()
