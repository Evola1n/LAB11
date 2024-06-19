#include <iostream>
#include <string>
using namespace std;
struct Book {
	string name;
	string author;
	float price;
	int amount;
};
int main()
{
	setlocale(LC_ALL, "Russian");
	int n;
	cout << "Введiть кількість книжок: ";
	cin >> n;
	Book* books = new Book[n];
	for (int i = 0; i < n; ++i) {
		cout << "Введіть назву книжнки: ";
		cin >> books[i].name;
		cout << "Введіть автора книжнки: ";
		cin >> books[i].author;
		cout << "Введіть ціну книжнки: ";
		cin >> books[i].price;
		cout << "Введіть кількість книжок на складі: ";
		cin >> books[i].amount;
	}
	for (int i = 0; i < n; ++i) {
		cout << "Назва: " << books[i].name << " Ціна: " << books[i].price << " Автор книжки: " << books[i].author << " Кількість книжок на складі: " << books[i].amount << endl ;
	}
	Book minBook = books[0];
	Book maxBook = books[0];


	for (int i = 0; i < n; ++i) {
		if (minBook.price > books[i].price) {
			minBook = books[i];
		}
	}
	for (int i = 0; i < n; ++i) {
		if (maxBook.price < books[i].price) {
			maxBook = books[i];
		}
	}
	cout << "Книжка з максимальною ціною: " << endl;
	cout << "Назва: " << maxBook.name << " Ціна: " << maxBook.price << " Автор книжки: " << maxBook.author << " Кількість книжок на складі: " << maxBook.amount << endl;
	cout << "Книжка з мінімальною ціною: " << endl;
	cout << "Назва: " << minBook.name << " Ціна: " << minBook.price << " Автор книжки: " << minBook.author << " Кількість книжок на складі: " << minBook.amount << endl;
}
