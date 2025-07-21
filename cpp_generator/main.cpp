#include <iostream>
#include <string>
#include <vector>
#include <numeric>
#include <cstdlib>
#include <ctime>
#include <ncurses.h>

// Function to check if a credit card number is valid using the Luhn algorithm
bool isValid(const std::string& number) {
    int nDigits = number.length();
    int nSum = 0;
    bool isSecond = false;
    for (int i = nDigits - 1; i >= 0; i--) {
        int d = number[i] - '0';
        if (isSecond == true)
            d = d * 2;
        nSum += d / 10;
        nSum += d % 10;
        isSecond = !isSecond;
    }
    return (nSum % 10 == 0);
}

// Function to generate a random credit card number
std::string generateCardNumber(const std::string& bin) {
    std::string cardNumber = bin;
    while (cardNumber.length() < 15) {
        cardNumber += std::to_string(rand() % 10);
    }
    int sum = 0;
    bool isSecond = false;
    for (int i = cardNumber.length() - 1; i >= 0; i--) {
        int d = cardNumber[i] - '0';
        if (isSecond) {
            d *= 2;
        }
        sum += d / 10;
        sum += d % 10;
        isSecond = !isSecond;
    }
    int lastDigit = (sum * 9) % 10;
    cardNumber += std::to_string(lastDigit);
    return cardNumber;
}

// Function to generate a random expiration date
std::string generateExpirationDate() {
    time_t t = time(0);
    struct tm* now = localtime(&t);
    int month = rand() % 12 + 1;
    int year = now->tm_year + 1900 + rand() % 5 + 2;
    return (month < 10 ? "0" : "") + std::to_string(month) + "/" + std::to_string(year);
}

// Function to generate a random CVV
std::string generateCVV() {
    int cvv = rand() % 900 + 100;
    return std::to_string(cvv);
}

void printHelp() {
    printw("Usage: cc_generator [options]\n");
    printw("Options:\n");
    printw("  -h, --help\t\tShow this help message\n");
    printw("  -b, --bin <bin>\tSpecify the BIN to use\n");
    printw("  -n, --count <count>\tSpecify the number of cards to generate\n");
    printw("  -e, --exp\t\tInclude expiration date\n");
    printw("  -c, --cvv\t\tInclude CVV\n");
}

int main(int argc, char* argv[]) {
    srand(time(0));
    std::string bin = "";
    int count = 1;
    bool includeExp = false;
    bool includeCvv = false;

    for (int i = 1; i < argc; ++i) {
        std::string arg = argv[i];
        if (arg == "-h" || arg == "--help") {
            initscr();
            printHelp();
            refresh();
            getch();
            endwin();
            return 0;
        } else if (arg == "-b" || arg == "--bin") {
            if (i + 1 < argc) {
                bin = argv[++i];
            } else {
                std::cerr << "Error: --bin option requires a value" << std::endl;
                return 1;
            }
        } else if (arg == "-n" || arg == "--count") {
            if (i + 1 < argc) {
                count = std::stoi(argv[++i]);
            } else {
                std::cerr << "Error: --count option requires a value" << std::endl;
                return 1;
            }
        } else if (arg == "-e" || arg == "--exp") {
            includeExp = true;
        } else if (arg == "-c" || arg == "--cvv") {
            includeCvv = true;
        }
    }

    if (bin.empty()) {
        std::vector<std::string> bins = {"4", "5", "37"};
        bin = bins[rand() % bins.size()];
    }

    initscr();
    start_color();
    init_pair(1, COLOR_GREEN, COLOR_BLACK);
    init_pair(2, COLOR_YELLOW, COLOR_BLACK);
    init_pair(3, COLOR_CYAN, COLOR_BLACK);

    attron(COLOR_PAIR(1));
    printw("Generated Credit Cards:\n");
    attroff(COLOR_PAIR(1));

    for (int i = 0; i < count; ++i) {
        std::string cardNumber = generateCardNumber(bin);
        attron(COLOR_PAIR(2));
        printw("Card Number: ");
        attroff(COLOR_PAIR(2));
        attron(COLOR_PAIR(3));
        printw("%s", cardNumber.c_str());
        attroff(COLOR_PAIR(3));

        if (includeExp) {
            attron(COLOR_PAIR(2));
            printw(" | Expiration Date: ");
            attroff(COLOR_PAIR(2));
            attron(COLOR_PAIR(3));
            printw("%s", generateExpirationDate().c_str());
            attroff(COLOR_PAIR(3));
        }
        if (includeCvv) {
            attron(COLOR_PAIR(2));
            printw(" | CVV: ");
            attroff(COLOR_PAIR(2));
            attron(COLOR_PAIR(3));
            printw("%s", generateCVV().c_str());
            attroff(COLOR_PAIR(3));
        }
        printw("\n");
    }

    refresh();
    getch();
    endwin();

    return 0;
}
