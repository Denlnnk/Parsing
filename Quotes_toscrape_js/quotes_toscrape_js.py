from requests_html import HTMLSession


def get_data():
    session = HTMLSession()
    response = session.get('https://quotes.toscrape.com/js/')

    response.html.render(sleep=1)

    quotes = response.html.find('.quote')

    for quote in quotes:
        title = quote.find('.text', first=True).text
        author = quote.find('.author', first=True).text
        tags = [tag.text for tag in quote.find('.tag')]
        print(title, author, tags)


def main():
    get_data()


if __name__ == '__main__':
    main()
